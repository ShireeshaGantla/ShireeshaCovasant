from flask import Flask, request, jsonify, render_template
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_mistralai.chat_models import ChatMistralAI
import os
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from flask_cors import CORS
from langchain.schema import BaseChatMessageHistory, HumanMessage, AIMessage
from dotenv import load_dotenv 

#MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY") 
load_dotenv()


app = Flask(__name__)
CORS(app)  

llm = ChatMistralAI(api_key=MISTRAL_API_KEY)  
memory = ConversationBufferMemory(memory_key="history", input_key="input")

#adds memory
prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful assistant"),
    ("{history}"),
    ("human", "{input}"),
])

runnable = prompt | llm | StrOutputParser()
memory = ConversationBufferMemory(return_messages=True)
runnable_with_history = RunnableWithMessageHistory(
    runnable,
    get_session_history=lambda session_id: memory.chat_memory,
    input_messages_key="input",
    history_messages_key="history",
)

history = {}
def get_session_history(session_id:str)-> BaseChatMessageHistory:
    if session_id not in history:
        history[session_id] = ChatMessageHistory()
    return history[session_id]
    
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data['query']
    session_id = data.get("session_id", "test_session")
    print(f"Received query: {query}")
    session_history = get_session_history(session_id)
    
    session_history.add_message(HumanMessage(content=query))
    response = runnable_with_history.invoke({"input": query}, config={"configurable": {"session_id": session_id}})
    print(f"Generated response: {response}")
    session_history.add_message(AIMessage(content=response))
    # print(session_history)
    print(response)
    return jsonify({'result': response}), 200  


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

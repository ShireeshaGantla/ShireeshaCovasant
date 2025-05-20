import React, { useState } from 'react';

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const appendMessage = (sender, text) => {
    // setMessages([...messages, { sender, text }]);
      setMessages((prevMessages) => [...prevMessages, { sender, text }]); 
  };
  const sendMessage = async () => {
    const message = inputValue.trim();
    if (!message) return;

    appendMessage('user', message);
    console.log(message)
    setInputValue('');
    const sessionId = 'data_123_new';
    try {
      const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: message,session_id: sessionId }),
      });
  
      const data = await response.json();
      if (data.result) {
        appendMessage('assistant', data.result);
        console.log(data.result)

      } else if (data.error) {
        appendMessage('assistant', `Error: ${data.error}`);
      }
    } catch (error) {
      appendMessage('assistant', 'Network error: Could not connect to the server.');
      console.error("Fetch error:", error);
    }
  };
  console.log(messages)


  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  };

  return (
    <div>
      <h1>Chat with the AI</h1>
      <div id="chat-area">
        {messages.map((msg, index) => (
          <div key={index} className={msg.sender}>
            <strong>{msg.sender === 'user' ? 'You:' : 'AI:'}</strong> {msg.text}
          
          </div>
        ))}
      </div>
      <div className="input-container"> 
        <input type="text"  id="user-input"  placeholder="Type your message"  value={inputValue}  onChange={handleInputChange}  onKeyPress={handleKeyPress}/>
        <button id="send-button" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

export default Chatbot;

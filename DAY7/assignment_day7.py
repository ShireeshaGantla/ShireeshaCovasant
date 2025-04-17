from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
shared_data = ""

@app.route("/updatefortoday", methods=['GET', 'POST'])
def update_for_today():
    global shared_data
    if request.method == 'POST':
        shared_data = request.form['data']
        return redirect(url_for('share_data'))
    return render_template('update_data.html')
      
@app.route("/share", methods=['GET'] )
def share_data():
    global shared_data
    data_to_show = shared_data  
    return render_template('share_data.html', shared_data=data_to_show)
        
@app.route("/clearnotepadfortoday", methods =['POST','GET'])
def clear_notepad():
    global shared_data
    if request.method == 'POST':
        shared_data = " "
    else :
        shared_data =" "
    return redirect(url_for('update_for_today'))

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request, redirect

import os
from line_breaks import LineBreak
from users import User
from line_break_display import df_display
from IPython.display import HTML


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    #Enter name, last_name, email and password
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']

    user = User(name, last_name, email, password)
    #Uploads user info to users database
    user.register_user()
    

@app.route('/linebreak', methods=['GET', 'POST'])
def device_duration():
    #Enter the line
    line = request.form['line']

    #Enter panel/controller
    controller = request.form['controller']

    line_break = LineBreak()
    df_result = line_break.get_line_break()

    df_display(df_result)
    
    return render_template('output.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyD-47sPSAmudcXX_fWu9WFMogMifj5Lr-I",
  "authDomain": "authentication-lab-5bb0a.firebaseapp.com",
  "projectId": "authentication-lab-5bb0a",
  "storageBucket": "authentication-lab-5bb0a.appspot.com",
  "messagingSenderId": "104514319361",
  "appId": "1:104514319361:web:7bd66c5cbb034d6538bc00",
  "measurementId": "G-4NCJEV0XZ0",
  "databaseURL" : ""
  }
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
    return render_template("signin.html")
    

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
    return render_template("signup.html")
    


    




@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)
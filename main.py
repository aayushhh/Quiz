from flask import Flask, render_template, request, redirect, session
import pyrebase
from functools import wraps
import sys
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)
config = {
    "apiKey": "AIzaSyAi04HoGT46-1s0S18Yf21f05Kbn-mWYNs",
    "authDomain": "quiz-f19f6.firebaseapp.com",
    "databaseURL": "https://quiz-f19f6.firebaseio.com",
    "projectId": "quiz-f19f6",
    "storageBucket": "quiz-f19f6.appspot.com",
    "messagingSenderId": "397514763088",
    "appId": "1:397514763088:web:c476ef5231cfa6da005a55",
    "measurementId": "`G-LLQ692MHGZ"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


# @app.route("/", methods=['GET', 'POST'])
# def basic():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         try:
#             auth.sign_in_with_email_and_password(email, password)
#             return render_template("faculty.html")
#         except:
#             return "Please check your credentials"
#     return render_template("login.html")
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # get the request data
        email = request.form["email"]
        password = request.form["password"]
        try:
            # login the user
            user = auth.sign_in_with_email_and_password(email, password)
            return render_template("faculty.html")
            # set the session
            user_id = user['idToken']
            user_email = email
            session['usr'] = user_id
            session["email"] = user_email
            return redirect("f")

        except:
            return"Invalid credentials. Please try again"

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
      #get the request form data
      email = request.form["email"]
      password = request.form["password"]
      try:
        #create the user
        auth.create_user_with_email_and_password(email, password);
        #login the user right away
        user = auth.sign_in_with_email_and_password(email, password)
        #session
        user_id = user['idToken']
        user_email = email
        session['usr'] = user_id
        session["email"] = user_email
        return redirect("/")
      except:
        return render_template("login.html", message="The email is already taken, try another one, please" )

    return render_template("register.html")

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         name = db.push['name']
#         email = db.push['email']
#         password = db.push['password']
#         confirm_password = db.push['password']
#         if password==confirm_password:
#             try:
#                 auth.create_user_with_email_and_password(name,email,password)
#                 return render_template("login.html")
#             except:
#                 auth.sign_in_with_email_and_password(email,password)
#     return render_template("register.html")




if __name__ == '__main__':
    app.run(debug=True)
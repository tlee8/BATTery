

from flask import Flask, render_template, session, request, url_for, redirect, flash
import os
import json, urllib


app = Flask(__name__)
app.secret_key = os.urandom(32)

badcreds = False #boolean for login creds

@app.route("/")
def hello():
    ''' Immediately redirects to login page; users must be logged in to use
    '''
    if ( (session.get('username') == "battery") ):
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))
    #return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    ''' Allows user to login

    Users must log in to access website
    If a user does not have an account, they may sign up for one
    '''
    print(badcreds)
    return render_template("login.html", wrong = badcreds)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    try:
        session.pop('username')
        return redirect(url_for("login"))
    except:
        return redirect(url_for("login"))

@app.route("/home", methods=["POST", "GET"])
def home():
    ''' Displays information from all APIs to logged in users
    '''
    return render_template("home.html", title = "DAILY BATT", user = session.get('username'))

@app.route("/auth", methods = ["POST"])
def auth():

    if ((request.form['username'] == "battery") and
        (request.form['password'] == "timiscool")):
        session['username'] = "battery"
        badcreds = False
        return redirect(url_for("home"))
    else:
        badcreds = True
        print("noooooo")
        print(badcreds)
        return redirect(url_for("login"))


    #return render_template("login.html")'''

if __name__== "__main__":
    app.debug = True
    app.run()

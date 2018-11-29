

from flask import Flask, render_template, session, request, url_for, redirect, flash
import os
import json, urllib


app = Flask(__name__)


@app.route("/")
def hello():
    if ( (session.get('username') == "battery") &&
         (session.get('password') == "timiscool") ):
        return render_template("home.html",
                                user = "battery")
    else:
        return render_template("login.html")
    ''' Immediately redirects to login page; users must be logged in to use
    '''
    #return redirect(url_for("login"))


@app.route("/home", methods=["POST", "GET"])
def home():
    ''' Displays information from all APIs to logged in users
    '''
    return render_template("home.html", title = "DAILY BATT")

@app.route("/login", methods = ["POST"])
def login():
    if ((request.form['username'] == "battery") &
        (request.form['password'] == "timiscool")):
        session['username'] = "battery"
        return render_template("home.html",
                                user = "battery")
    elif ((request.form['username']) == "battery"):
        return render_template("wrongcreds.html",
                                user = request.form['username'],
                                pwd = request.form['password'],
                                error = "Your password was incorrect")
    elif ((request.form['password']) == "timiscool"):
        return render_template("wrongcreds.html",
                                user = request.form['username'],
                                pwd = request.form['password'],
                                error = "Your username was incorrect")
    else:
        return render_template("wrongcreds.html",
                                user = request.form['username'],
                                pwd = request.form['password'],
                                error = "Your password and password were both incorrect!")
    ''' Allows user to login

    Users must log in to access website
    If a user does not have an account, they may sign up for one
    '''

    @app.route("/logout")
    def logout():
        try:
            session.pop('username')
            return redirect( urlfor( "hello" ) )
        except:
            return redirect( urlfor( "hello" ) )
    #return render_template("login.html")'''

if __name__== "__main__":
    app.debug = True
    app.run()

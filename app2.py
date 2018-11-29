

from flask import Flask, render_template, session, request, url_for, redirect, flash
import os
import json, urllib

import sqlite3 #imports sqlite
DB_FILE="data/quackamoo.db"

app = Flask(__name__)


@app.route("/")
def hello():
    ''' Immediately redirects to login page; users must be logged in to use
    '''
    #return redirect(url_for("login"))
    if 'username' in session:
        return render_template("home.html", title = "DAILY BATT")
    return render_template("login.html")

@app.route("/home", methods=["POST", "GET"])
def home():
    ''' Displays information from all APIs to logged in users
    '''
    return render_template("home.html", title = "DAILY BATT")

@app.route("/login")
def login():
    ''' Allows user to login

    Users must log in to access website
    If a user does not have an account, they may sign up for one
    '''
    DB_FILE="data/BATT.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() 
    username=request.form['username']
    command = 'SELECT password FROM users WHERE users.username = "{0}"'.format(username)
    c.execute(command)
    password = c.fetchone()#gets the password for the user if the user is in db
    return render_template("login.html")

if __name__== "__main__":
    app.debug = True
    app.run()

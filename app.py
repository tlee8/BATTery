

from flask import Flask, render_template, session, request, url_for, redirect, flash
import os
import json, urllib


app = Flask(__name__)


@app.route("/")
def hello():
    ''' Immediately redirects to login page; users must be logged in to use
    '''
    return redirect(url_for("login"))


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
    return render_template("login.html")

if __name__== "__main__":
    app.debug = True
    app.run()

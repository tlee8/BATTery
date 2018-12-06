import json
import urllib
import random
import os
import ssl

from flask import Flask, render_template, session, request, url_for, redirect, flash

from util import dataaccess, apeye

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context



app = Flask(__name__)
app.secret_key = os.urandom(32)


#hardcoded info for home page
news =  apeye.news()
articles = {}
for i in range(10):
    articles[i]= [news['articles'][i]['title'], news['articles'][i]['description'], news['articles'][i]['content'], news['articles'][i]['urlToImage'], i, i+1]

#word = "College"
#definition = "The reason for my eternal suffering"
weather = apeye.weather()["currently"]["summary"]
temperature = apeye.weather()["currently"]["temperature"]

words, defs = apeye.word()
x = random.randint(1, len(words)) - 1
word = words[x]
definition = defs[x]

s = apeye.number()

dogPic = apeye.dogIm()
catPic = apeye.catIm()

@app.route("/")
def hello():
    ''' Immediately redirects to login page; users must be logged in to use
    '''
    if session.get('username'):
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
    return render_template("login.html")

@app.route("/logout", methods=["POST", "GET"])
def logout():
    try:
        session.pop('username')
        flash("You have successfully logged out")
        return redirect(url_for("login"))
    except:
        flash("You have successfully logged out")
        return redirect(url_for("login"))

@app.route("/home", methods=["POST", "GET"])
def home():
    ''' Displays information from all APIs to logged in users
    '''
    if "username" not in session:
        return redirect(url_for("login"))
    #sources = dataaccess.getPrefs(session.get('username'))[0]
    #news = apeye.news(sources)
    #articles = {}
    #for i in range(10):
        #articles[i]= [news['articles'][i]['title'], news['articles'][i]['description'], news['articles'][i]['content'], news['articles'][i]['urlToImage'], i, i+1]

    '''dailies = dataaccess.getPrefs(session.get('username'))[1]
    if "Weather" in dailies:
        weather = apeye.weather()["currently"]["summary"]
        temperature = apeye.weather()["currently"]["temperature"]
    if "Dog" in dailies:
        dogPic = apeye.dogIm()
    if "Cat" in dailies:
        catPic = apeye.catIm()
    if "Word" in dailies:
        words, defs = apeye.word()
        x = random.randint(1, len(words)) - 1
        word = words[x]
        definition = defs[x]
    if "Date" in dailies:
        s = apeye.number()

    '''
    return render_template("home.html", title = "DAILY BATT", user = session.get('username'), articles = articles, word = word, definition = definition, weather = weather, temperature = temperature)

@app.route("/article", methods=["POST", "GET"])
def article():
    if "username" not in session:
        return redirect(url_for("login"))
    title = request.args["title"]
    print(title)
    for article in articles:
        if title == articles[article][0]:
            print(article)
            return render_template("article.html", article = articles[article])

@app.route("/auth", methods = ["POST"])
def auth():
    if  dataaccess.loginuser(request.form['username'], request.form['password']):
        session['username'] = request.form['username']
        flash("Welcome " + session['username'] + "! You have successfully logged in.")
        return redirect(url_for("home"))
    else:
        flash("Your login credentials were incorrect.")
        return redirect(url_for("login"))

@app.route("/register", methods = ["POST", "GET"])
def register():
    return render_template("register.html")

@app.route("/regauth", methods = ["POST"])
def regauth():
    if not request.form['password'] == request.form['password2']:
        flash("Your passwords do not match")
        return redirect(url_for("register"))
    if dataaccess.registeruser(request.form['username'], request.form['password']):
        flash("You have successfully created an account")
        return redirect(url_for("login"))
    flash("The username you entered is taken.")
    return redirect(url_for("register"))

@app.route("/popularposts", methods=["GET"])
def popposts():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("popularposts.html", comments = comments)

@app.route("/mystuff")
def mystuff():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("mystuff.html")

@app.route("/preferences")
def preferences():
    #sources = dataaccess.getPrefs(session.get('username'))[0]
    #dailies = dataaccess.getPrefs(session.get('username'))[1]
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("preferences.html", pref = True) #, sources = sources, dailies = dailies )

@app.route("/updatepref", methods = ["POST"])
def updatepref():
    if "username" not in session:
        return redirect(url_for("login"))
    sources = request.form.getlist('sources')
    dailies = request.form.getlist('dailies')
    #dataaccess.setPrefs(session.get('username'), sources, dailies)
    flash("You have successfully updated your preferences")
    return redirect(url_for("home"))



if __name__== "__main__":
    app.debug = True
    app.run()

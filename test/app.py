import json, urllib
from flask import Flask, render_template, request, flash
from util import newss

app = Flask(__name__)

@app.route("/")
def root():
    url = "https://ipapi.co/json/"
    f = urllib.request.urlopen(url).read()
    d = json.loads(f)
    lon = d["longitude"]
    lat = d["latitude"]

    url2 = "https://api.darksky.net/forecast/a8cad3df213e3cf847b714ab33140b16/"+str(lat)+","+str(lon)
    req = urllib.request.urlopen(url2)
    file = req.read()
    dict = json.loads(file)

    return render_template("index.html",
        timezone = dict["timezone"],
        summary = dict["currently"]["summary"],
        icon = dict["currently"]["icon"],
        temp = dict["currently"]["temperature"],
        precipProb=dict["currently"]["precipProbability"])

@app.route("/news")
def news():
    dictionary = newss.top_headlines('bbc-news')
    article  = dictionary['articles'][0]['content']
    url = dictionary['articles'][0]['url']
    link = dictionary['articles'][0]['urlToImage']
    return render_template('news.html', content = article, url = url, link = link)

PRE = 'https://dictionaryapi.com/api/v3/references/collegiate/json/test?key='
KEY = 'd9878c3e-8acf-4e8c-b9b0-cf3d24927177'
URL = PRE + KEY

@app.route('/word')
def display():
    x = urllib.request.urlopen(URL)
    str = x.read()
    list = json.loads(str)
    list = list[2:]
    return render_template('demo.html', l = list)


if __name__ == "__main__":
    app.debug = True
app.run()

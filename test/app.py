import json
import urllib

from flask import Flask, render_template, request, flash

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
    

if __name__ == "__main__":
    app.debug = True
app.run()

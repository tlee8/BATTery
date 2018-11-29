

from flask import Flask, render_template
import json, urllib


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("test.html", title = "DAILY BATT")

if __name__== "__main__":
    app.debug = True
    app.run()

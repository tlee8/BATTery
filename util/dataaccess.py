#BATTery

import sqlite3
from datetime import date
from util import db_builder

db_builder.main()

def registeruser(user, pwd):
    DB_FILE="data/BATT.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT username FROM users WHERE username = \'"+user+"\'"
    c.execute(command)
    rows = c.fetchone()
    if rows:
        return False;
    params = (user, pwd)
    c.execute("INSERT INTO users VALUES (?,?)", params)
    db.commit() #save changes
    db.close()  #close database
    return True

def loginuser(user, pwd):
    DB_FILE="data/BATT.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT username, password FROM users WHERE username = ? AND password = ?"
    params = (user, pwd)
    c.execute(command, params)
    rows = c.fetchone()
    return rows

def saveday(cat, dog, meme, recipe, date_fact, word, weather):
        date = date.today().isoformat()
        params = (date, cat, dog, meme, recipe, date_fact, word, weather)
        c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?)", params)
        db.commit() #save changes
        db.close()  #close database
    
def newday(date):
    DB_FILE = "data/BATT.db"
    date = date.today().isoformat()
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT date FROM daily WHERE date = {0}".format(date)
    c.execute(command)
    if rows:
        return False
    else:
        return True

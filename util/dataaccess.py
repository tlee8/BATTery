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

'''
def saveday(cat, dog, word, defi, weather, temperature):
        date = date.today().isoformat()
        params = (date, cat, dog, word, defi, weather, temperature)
        c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)", params)
        db.commit() #save changes
        db.close()  #close database

def newday():
    DB_FILE = "data/BATT.db"
    date = date.today().isoformat()
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT date FROM daily WHERE date = {0}".format(date)
    c.execute(command)
    rows = c.fetchone()
    if rows:
        return False
    else:
        return True

def update():
    if newday:
        weather = apeye.weather()["currently"]["summary"]
        temperature = apeye.weather()["currently"]["temperature"]
        words, defs = apeye.word()
        x = random.randint(1, len(words)) - 1
        word = words[x]
        definition = defs[x]
        saveday("","","",word,definition,)
'''
def setPrefs(user,sources,dailies):
    DB_FILE = "data/BATT.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    params = (user,sources,dailies)
    command = "INSERT INTO pref VALUES (?,?,?)"
    c.execute(command,params)
    db.commit()#save changes
    db.close()  #close database
    return True

def getPrefs(user):
    DB_FILE = "data/BATT.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT source FROM pref WHERE user = '{0}'".format(user)
    c.execute(command)
    sources= []
    for row in c.fetchall():
        sources.append(row[0])
    command = "SELECT daily FROM pref WHERE user = '{0}'".format(user)
    c.execute(command)
    dailies = []
    for row in c.fetchone():
        dailies.append(row)
    return sources, dailies

#def main():
#    setPrefs("battery", "CNN", "article")
#    print(getPrefs("battery"))
#main()

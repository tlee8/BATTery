#BATTery

import sqlite3
from datetime import date
#from util         fix when push
from util import db_builder
import os

db_builder.main()

def registeruser(user, pwd):
    db_builder.main()
    DB_FILE="data//BATT.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT username FROM users WHERE username = \'"+user+"\'"
    c.execute(command)
    rows = c.fetchone()
    if rows:
        return False;
    params = (user, pwd)
    with sqlite3.connect(DB_FILE) as x:
        x.execute("INSERT INTO users VALUES (?,?)", params)
    origSetPref(user)
    db.commit() #save changes
    #db.close()  #close database
    return True

def loginuser(user, pwd):
    db_builder.main()
    DB_FILE="data//BATT.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT username, password FROM users WHERE username = ? AND password = ?"
    params = (user, pwd)
    c.execute(command, params)
    rows = c.fetchone()
    db.commit() #save changes
    #db.close()  #close database
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
def setPref(user,text,types):
    #db_builder.main()

    DB_FILE = "data//BATT.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    params = (user,text,types)
    command = "INSERT INTO pref VALUES (?,?,?)"
    c.execute(command,params)
    db.commit()#save changes
    #db.close()  #close database
    return True

def setPrefs(user, sources, dailies):
    #db_builder.main()

    DB_FILE = "../data/BATT.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    command = "DELETE FROM pref where user = '{0}'".format(user)
    with sqlite3.connect(DB_FILE) as x:
        x.execute(command)
    for source in sources:
        setPref(user, source, "source")
    for daily in dailies:
        setPref(user, daily, "daily")
    c.execute(command,params)
    db.commit()#save changes
    #db.close()  #close database
    return True


def getPrefs(user):
    #db_builder.main()
    DB_FILE = "data//BATT.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    db_builder.main()
    command = "SELECT * FROM pref WHERE user = '{0}' ".format(user)
    c.execute(command)
    if (not c.fetchone()):
        #sources = ['ars-technica', 'abc-news', 'bbc-news', 'business-insider','buzzfeed', 'cbs-news', 'el-mundo', 'the-new-york-times', 'national-geographic', 'the-wall-street-journal', 'the-washington-post']
        #dailies = ['Word', 'Date', 'Cat', 'Dog', 'Weather']

        #setPref(user, sources, dailies)

        setPref(user,"ABC News", "source")
        setPref(user,"Ars Technica", "source")
        setPref(user,"BBC News", "source")
        setPref(user,"Business Insider", "source")
        setPref(user,"Buzzfeed", "source")
        setPref(user,"El Mundo", "source")
        setPref(user,"National Geographic", "source")
        setPref(user,"New York Times", "source")
        setPref(user,"Wall Street Journal", "source")
        setPref(user,"National Geographic", "source")
        setPref(user,"CBS News", "source")
        setPref(user,"Word of the Day", "daily")
        setPref(user,"Weather", "daily")
        setPref(user,"Date Fact", "daily")

    command = "SELECT preffered,type FROM pref WHERE user = '{0}'".format(user)
    c.execute(command)
    ans = {}
    ans['source']=[]
    ans['daily'] = []
    for row in c.fetchall():
        ans[row[1]].append(row[0])
    c.execute(command)

    db.commit() #save changes
    #db.close()  #close database
    return ans[sources], ans[dailies]

def origSetPref(user):
    setPref(user,"ABC News", "source")
    setPref(user,"Ars Technica", "source")
    setPref(user,"BBC News", "source")
    setPref(user,"Business Insider", "source")
    setPref(user,"Buzzfeed", "source")
    setPref(user,"El Mundo", "source")
    setPref(user,"National Geographic", "source")
    setPref(user,"New York Times", "source")
    setPref(user,"Wall Street Journal", "source")
    setPref(user,"National Geographic", "source")
    setPref(user,"CBS News", "source")
    setPref(user,"Word of the Day", "daily")
    setPref(user,"Weather", "daily")
    setPref(user,"Date Fact", "daily")


#def main():
#    setPref("battery", "CNN", "source")
#    print(getPrefs("battery"))
#main()

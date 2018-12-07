#BATTery
#Thomas Lee (PM)
#Britni Canale
#Ahnaf Kazi
#Tim Marder
#p06

'''This script extracts data from multiple APIs for use in application'''

import json, urllib, datetime, random

with open("data/keys.json") as APIkeys:
    keys = json.loads(APIkeys.read())

newsKey = keys["newsKey"]
wordKey = keys["wordKey"]

def weather(key):
    '''Extracts data from DarkSky API'''
    url = "https://ipapi.co/json/"
    f = urllib.request.urlopen(url).read()
    d = json.loads(f)
    lon = d["longitude"]
    lat = d["latitude"]

    url2 = "https://api.darksky.net/forecast/a8cad3df213e3cf847b714ab33140b16/"+str(lat)+","+str(lon)
    req = urllib.request.urlopen(url2)
    file = req.read()
    weatherDict = json.loads(file)
    return weatherDict["currently"][key]


def news():
    '''Extracts data from NewsAPI'''

    ''' Code to be implemented when database is functional
    newsDict = {}
    sources = ['ars-technica', 'abc-news', 'bbc-news', 'business-insider','buzzfeed', 'cbs-news', 'el-mundo', 'the-new-york-times', 'national-geographic', 'the-wall-street-journal', 'the-washington-post']
    for src in prefs:
        if src in sources:
            url = ('https://newsapi.org/v2/top-headlines?'
               'sources=' + src + '&'
                   'apiKey=' + newsKey)
            response = urllib.request.urlopen(url).read()
            temp = json.loads(response)
            for key in temp:
                newsDict[key] = temp[key]
    '''


    src = "bbc-news"
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=' + src + '&'
           'apiKey=' + newsKey)
    response = urllib.request.urlopen(url).read()
    newsDict = json.loads(response)
    articles = {}
    for i in range(10):
        articles[i]= [newsDict['articles'][i]['title'], newsDict['articles'][i]['description'], newsDict['articles'][i]['content'], newsDict['articles'][i]['urlToImage'], newsDict['articles'][i]['url'], i, i+1]
    return articles


def word():
    '''Extracts data from dictionary api'''

    URL = 'https://dictionaryapi.com/api/v3/references/collegiate/json/test?key=' + wordKey
    x = urllib.request.urlopen(URL)
    str = x.read()
    list = json.loads(str)
    list = list[2:]
    words = []
    defs = []

    for d in list:
        words.append(d["hwi"]["hw"])
        defs.append(d["def"][0]["sseq"][0][0][1]["dt"][0][1].strip("{bc}a_link|"))

    x = random.randint(1, len(words)) - 1
    return words[x], defs[x]


def number():
    '''Extracts date fact from numbers API'''

    now = datetime.datetime.now()
    month = now.month
    day = now.day

    url = 'http://numbersapi.com/' + str(month) + '/' + str(day) + '/date'
    s = urllib.request.urlopen(url)
    s = s.read()
    s = str(s)[2:-1]

    return s


def dog():
    '''Extracts dog of the day from Dog API'''

    url = "https://random.dog/woof.json"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)

    dogPic = d['url']

    print(dogPic)
    return dogPic

def dogIm():
    '''Takes dog of the day and makes into proper file extension'''
    im = dog()
    print(im)
    if im[-3:] == 'jpg' or im[-3:] == "JPG":
        return im
    else:
        dogIm()


def cat():
    '''Extracts cat of the day from Cat API'''

    url = "https://aws.random.cat/meow"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)

    catPic = d['file']

    print(catPic)
    return catPic

def catIm():
    '''Takes cat of the day and makes into proper file extension'''
    im = cat()
    print (im)
    if im[-3:] == 'jpg' or im[-3:] == "JPG":
        return im
    else:
        catIm()

import json, urllib, datetime

with open("data/keys.json") as APIkeys:
    keys = json.loads(APIkeys.read())

newsKey = keys["newsKey"]
wordKey = keys["wordKey"]
recipeKey = keys["recipeKey"]

def weather():
    url = "https://ipapi.co/json/"
    f = urllib.request.urlopen(url).read()
    d = json.loads(f)
    lon = d["longitude"]
    lat = d["latitude"]

    url2 = "https://api.darksky.net/forecast/a8cad3df213e3cf847b714ab33140b16/"+str(lat)+","+str(lon)
    req = urllib.request.urlopen(url2)
    file = req.read()
    weatherDict = json.loads(file)

    return weatherDict

def news():
    src = 'bbc-news'
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=' + src + '&'
           'apiKey=' + newsKey)
    response = urllib.request.urlopen(url).read()
    newsDict = json.loads(response)
    return newsDict

def word():
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

    return words, defs

def number():
    now = datetime.datetime.now()
    month = now.month
    day = now.day

    url = 'http://numbersapi.com/' + str(month) + '/' + str(day) + '/date'
    s = urllib.request.urlopen(url)
    s = s.read()
    s = str(s)[2:-1]

    return s

def dog():
    url = "https://random.dog/woof.json"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)

    dogPic = d['url']

    return dogPic

def dogIm():
    im = dog()
    if im[-3:] == 'jpg' or im[-3:] == "JPG":
        return im
    else:
        dogIm()

def cat():
    url = "https://aws.random.cat/meow"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)

    catPic = d['file']

    return catPic

def catIm():
    im = cat()
    if im[-3:] == 'jpg' or im[-3:] == "JPG":
        return im
    else:
        catIm()

def recipe():
    url = 'https://www.food2fork.com/api/get?key='
    url += recipeKey

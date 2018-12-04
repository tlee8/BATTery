import json, urllib



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
    API_KEY = "2ed9d542b2084d9181d7df321aae80b5"
    src = 'bbc-news'
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=' + src + '&'
       'apiKey=' + API_KEY)
    response = urllib.request.urlopen(url).read()
    newsDict = json.loads(response)
    return newsDict

def word():
    key = "d9878c3e-8acf-4e8c-b9b0-cf3d24927177"
    url = "https://www.dictionaryapi.com/api/v3/references/sd4/json/[word]?key=" + key
    response = urllib.request.urlopen(url).read()

import json, urllib

def dog():
    url = "https://random.dog/woof.json"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)

    dogPic = d['url']

    print (dogPic)

dog()
dog()
dog()

import json, urllib

API_KEY = "2ed9d542b2084d9181d7df321aae80b5"

def top_headlines(src):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=' + src + '&'
       'apiKey=' + API_KEY)
    response = urllib.request.urlopen(url)
    return json.loads(response.read())

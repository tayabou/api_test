'''
Created on 2014/12/31

@author: yatatomo
'''
import json
from requests_oauthlib import OAuth1Session

if __name__ == '__main__':

    CONSUMER_KEY = 'shJ3e537FPtlrHXVtlFOUZ30v'
    CONSUMER_SECRET = 'nKK53BqWb484lr9GQMDC1rDdfc4koSCm53yhX1iO6De78Lx4Fb'
    ACCESS_TOKEN = '134000246-SIxetzdAeaH7LKq3kP5UqjcNSTEclUzAckjjbVGc'
    ACCESS_TOKEN_SECRET = 'gaQC7E3hboANaunpCKkNob7jFRtYNtTL4HdmKbf8datzj'
    
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
   
    params = {} 
    session = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    res = session.get(url, params = params)

    if res.status_code == 200:
        timeline = json.loads(res.text)
        for tweet in timeline:
            print(tweet["text"])
    else:
        print("Error: %d" % res.status_code)

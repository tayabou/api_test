'''
Created on 2014/12/28

@author: yatatomo
'''

import json
from requests_oauthlib import OAuth1Session
from root.nested.twitterparams import TwitterParam

if __name__ == '__main__':
    url = "https://api.twitter.com/1.1/statuses/update.json"
    
    params = {"status" : "ロード・オブ・ザ・リング見ながらTest"}
    
    twParams = TwitterParam()

    twitter = OAuth1Session(twParams.get_consumer_key(),
                             twParams.get_consumer_secret(),
                              twParams.get_access_token(),
                               twParams.get_access_token_secret())

    res = twitter.post(url, params=params)
    
    if res.status_code == 200:
        print("OK")
    else:
        print("Error: %d" % res.status_code)


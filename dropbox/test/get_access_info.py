'''
Created on 2015/01/02

@author: yatatomo
'''
import json
from requests_oauthlib import OAuth1Session

if __name__ == '__main__':

    CONSUMER_KEY = 'lnpio4b46rh22su'
    CONSUMER_SECRET = 'wql74blnvd5oc79'
    ACCESS_TOKEN = 'MXr907K1VyZnfYxy'
    ACCESS_TOKEN_SECRET = 'fsvteTWANyMW11uZ'
    
    #authorize_url = 'https://api.dropbox.com/1/account/info'
    authorize_url = 'https://api.dropbox.com/1/oauth/access_token'

    #params = {"oauth_token" : "fsvteTWANyMW11uZ"}
    params = {}
    session = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    authorize_res = session.post(authorize_url, params = params)

    if authorize_res.status_code == 200:
        print(authorize_res.text)
    else:
        print("Error: %d" % authorize_res.status_code)

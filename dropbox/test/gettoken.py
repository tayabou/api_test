'''
Created on 2015/01/04

@author: yatatoma
'''
import json
from requests_oauthlib import OAuth1Session

if __name__ == '__main__':

    CONSUMER_KEY = 'lnpio4b46rh22su'
    CONSUMER_SECRET = 'wql74blnvd5oc79'
    #ACCESS_TOKEN = '5gL5bsAYUOQAAAAAAAAABezxqShmZeohipHo2uhCkWYyOe4mFUSNgKwU4yk6iJDs'
    #ACCESS_TOKEN_SECRET = 'gaQC7E3hboANaunpCKkNob7jFRtYNtTL4HdmKbf8datzj'
    
    authorize_url = 'https://api.dropbox.com/1/oauth/request_token'

    params = {} 
    session = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET)
    authorize_res = session.post(authorize_url, params = params)

    if authorize_res.status_code == 200:
        print(authorize_res.text)
    else:
        print("Error: %d" % authorize_res.status_code)

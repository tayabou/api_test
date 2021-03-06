'''
Created on 2015/01/01

@author: yatatomo
'''

import json
from requests_oauthlib import OAuth1Session

if __name__ == '__main__':

    CONSUMER_KEY = 'lnpio4b46rh22su'
    CONSUMER_SECRET = 'wql74blnvd5oc79'
    
    authorize_url = 'https://api.dropbox.com/1/oauth/request_token'

    params = {} 
    session = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET)
    request_token_res = session.post(authorize_url, params = params)
    
    access_token = ''
    auth_token_map = {}

    if request_token_res.status_code == 200:
        print(request_token_res.text)
        and_splited_list = request_token_res.text.split('&')
        for and_splited_str in and_splited_list:
            equal_splited_str = and_splited_str.split('=')
            key = equal_splited_str[0]
            value = equal_splited_str[1]
            auth_token_map[key] = value
    else:
        print("Error: %d" % request_token_res.status_code)
    
    #認証用のURLを生成
    authorize_url = 'https://www.dropbox.com/1/oauth/authorize'

    params = {"oauth_token" : auth_token_map["oauth_token"]}
    session = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET)
    authorize_res = session.get(authorize_url, params = params)

    if authorize_res.status_code == 200:
        print("authorize OK.")
        #ファイルにHTMLを出力
        f = open('/Users/yatatomo/Workspace/dropbox_authorize.html', 'w')
        f.write(authorize_res.text)
        f.close()
        
    else:
        print("Error: %d" % authorize_res.status_code)

    access_token_url = 'https://api.dropbox.com/1/oauth/access_token'
    params = {"oauth_token" : auth_token_map["oauth_token"], "oauth_token_secret" : auth_token_map["oauth_token_secret"]}
    session = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, auth_token_map["oauth_token"], auth_token_map["oauth_token_secret"])
    access_token_res = session.post(access_token_url, params=params)

    if access_token_res.status_code == 200:
        print(access_token_res.text)
    else:
        print("Error: %d" % access_token_res.status_code)
    

    access_info_url = 'https://api.dropbox.com/1/account/info'
    params = {"oauth_token" : auth_token_map["oauth_token"], "oauth_token_secret" : auth_token_map["oauth_token_secret"]}
    session = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, auth_token_map["oauth_token"], auth_token_map["oauth_token_secret"])
    access_info_res = session.get(access_info_url, params = params)

    if access_info_res.status_code == 200:
        print(access_info_res.text)
    else:
        print("Error: %d" % access_info_res.status_code)

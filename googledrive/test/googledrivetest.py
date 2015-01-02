'''
Created on 2015/01/02

@author: yatatomo
'''

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

if __name__ == '__main__':
    CLIENT_ID = '184978633898-va6vojtpiuhbo0610d9j0m5hb8eevm2s.apps.googleusercontent.com'
    CLIENT_SECRET = 'NESNMBZEW16AiVyo74xoH56S'
    
    OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
    
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
    
    FILENAME = '/Users/yatatomo/Workspace/sample.zip'
    
    flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE,
                               redirect_uri=REDIRECT_URI)
    
    authorize_url = flow.step1_get_authorize_url()
    print ('Go to following link in your browser:' + authorize_url)
    code = input('Enter verification code:').strip()
    credentials = flow.step2_exchange(code)
    
    http = httplib2.Http()
    http = credentials.authorize(http)
    
    drive_service = build('drive', 'v2', http=http)
    
    media_body = MediaFileUpload(FILENAME, mimetype='application/zip', resumable=True)
    body = {
            'title' : 'My document',
            'description' : 'A test document',
            'mimeType' : 'application/zip'
            }

    file = drive_service.files().insert(body=body, media_body=media_body).execute()
    pprint.pprint(file)

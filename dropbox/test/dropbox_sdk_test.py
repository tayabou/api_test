'''
Created on 2015/01/02

@author: yatatomo
'''

import dropbox

if __name__ == '__main__':

    CONSUMER_KEY = 'lnpio4b46rh22su'
    CONSUMER_SECRET = 'wql74blnvd5oc79'
    
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(CONSUMER_KEY, CONSUMER_SECRET)
    
    authorize_url = flow.start()
    
    print ('1. Go to: ' + authorize_url)
    print ('2. Click "Allow" (you might have to log in first)')
    print ('3. Copy the authorization code.')
    code = input("Enter the authorization code here: ").strip()
    
    access_token, user_id = flow.finish(code)
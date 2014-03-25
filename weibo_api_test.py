# -*- coding: utf-8 -*-

from weibo import APIClient
import json
import requests
import time

APP_KEY = '1598714745' # app key
APP_SECRET = 'e49c519512a95ccaa01c25960edd6f77' # app secret
CALLBACK_URL = 'http://www.amadeus.com' # callback url
#r = requests.post('https://api.weibo.com/oauth2/authorize?client_id=1598714745&redirect_uri=http://www.amadeus.com&response_type=code')

code = 'b3c5514dfa7e6c9413ba698553d44401'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
#r = client.request_access_token(code1)
access_token = '2.00AI_4XFhjCMkB30f4e8ca149eaBKD' #r.access_token
expires_in = '1395860398' #r.expires_in 
client.set_access_token(access_token, expires_in)
client.statuses.upload.post(status=u'测试OAuth 2.0带图片发微博', pic=open('/Users/kyah/Desktop/Aptamil 2-3.jpg'))


'''
print access_token, expires_in
c = 100
while(c):
    try: 
        response = client.statuses.public_timeline.get()
        for st in response.statuses:
            print st.user.name
            response_uid = client.statuses.user_timeline.get( uid = st.user.id,count = 100 )
            for st1 in response_uid.statuses:
                if st1.text.find(u'宝贝') or st1.text.find(u'奶粉') or st1.text.find(u'婴儿'):
                    print "Found Weibo: " + st.text
                    #client.friendships.create.post(uid = st.user.id)
    except:
        c = c-1
        continue
'''

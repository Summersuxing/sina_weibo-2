from weibo import APIClient
import json
import requests

APP_KEY = '1598714745' # app key
APP_SECRET = 'e49c519512a95ccaa01c25960edd6f77' # app secret
CALLBACK_URL = 'http://www.amadeus.com' # callback url
#r = requests.post('https://api.weibo.com/oauth2/authorize?client_id=1598714745&redirect_uri=http://www.amadeus.com&response_type=code')

code = 'b3c5514dfa7e6c9413ba698553d44401'
code1 = 'bc3a5f9ac840f456cbb73aeb75363f83'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
#r = client.request_access_token(code1)
access_token = '2.00AI_4XFhjCMkB30f4e8ca149eaBKD' #r.access_token 
expires_in = '1395860398' #r.expires_in 
client.set_access_token(access_token, expires_in)

api_list = ['statuses/public timeline','statuses/mentions']
print access_token, expires_in


'''
print "-----------------------------------------"
#2/statuses/public timeline
response = client.statuses.public_timeline.get()
for st in response.statuses:
    print st.text

print "-----------------------------------------"
#2/statuses/friends timeline
response = client.statuses.friends_timeline.get()
for st in response.statuses:
    print st.text

print "-----------------------------------------"
#2/statuses/home timeline
response = client.statuses.home_timeline.get()
for st in response.statuses:
    print st.text

print "-----------------------------------------"
#statuses/friends_timeline/ids
response = client.statuses.friends_timeline.ids.get()
for st in response.statuses:
    print st

print "-----------------------------------------"
#statuses/user_timeline

response = client.statuses.user_timeline.get( uid = 208943345 )
for st in response.statuses:
    print st.text

print "-----------------------------------------"
response = client.statuses.repost_timeline.get(id = '1395757029401')
print response
for st in response.reposts:
    print st.text


print "-----------------------------------------"
#statuses/mentions
response = client.statuses.mentions.get()
for st in response.statuses:
    print st.text


print "-----------------------------------------"
#statuses/bilateral_timeline
response = client.statuses.bilateral_timeline.get()
for st in response.statuses:
    print st.id
print "-----------------------------------------"

#statuses/show
response = client.statuses.show.get(id = '3692136988128421')

print response.text

print "-----------------------------------------"

#statuses/repost
response = client.statuses.repost.post(id = 3692136988128421)

print "-----------------------------------------"
response = client.comments.by_me.get()
for st in response.comments:
    print st.text
print "-----------------------------------------"
'''

print "Enter the weibo you want to post: "
weibo = raw_input()
try:
    client.statuses.update.post(status = weibo)
    print "OK"
except:
    print "ERROR"

print "-----------------------------------------"

print "-----------------------------------------"


print "-----------------------------------------"


print "-----------------------------------------"


print "-----------------------------------------"


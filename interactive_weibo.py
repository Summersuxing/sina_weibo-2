from weibo import APIClient
import json
import requests
import time
import webbrowser
import yaml
import sys

import Tkinter, tkFileDialog


APP_KEY = '1598714745' # app key
APP_SECRET = 'e49c519512a95ccaa01c25960edd6f77' # app secret
CALLBACK_URL = 'http://www.amadeus.com' # callback url


code_url = 'https://api.weibo.com/oauth2/authorize?client_id=1598714745&redirect_uri=http://www.amadeus.com&response_type=code'

def login_weibo():
    new = 2
    webbrowser.open(code_url,new=new)
    code = raw_input("After enter username and password, please put the code on the very right part of the redirected url to here: \n")
    return code 


def dump_yaml(filename,data):
    with open(filename, 'w') as outfile:
        outfile.write(yaml.dump(data))

def read_yaml(filename):
    with open(filename, 'r') as f:
        data = yaml.load(f)
    return data

class weibo:
    def __init__(self,client):
        self.client = client
        self.choice_dict = {
                            '1': 'read_timeline',
                            '2': 'read_public_timeline',
                            '3': 'post_weibo'
                            }
        

    def main_manu(self):
        print "**************"
        print "1. Read timeline"
        print "2. Read weibo ramdomly from others"
        print "3. Post weibo"
        print "**************"
        
    def post_manu(self):
        print "*********"
        print "1. Post word only"
        print "2. Post with a picture"
        print "*********"

        
    def read_timeline(self):
        response = self.client.statuses.home_timeline.get()
        for st in response.statuses:
            print st.text

            
    def read_public_timeline(self):
        response = self.client.statuses.public_timeline.get()
        for st in response.statuses:
            print st.text

            
    def post_weibo(self):
        self.post_manu()
        choice = raw_input()
        if choice == '1':
            weibo = raw_input("Enter your weibo here: \n")
            response = self.client.statuses.update.post(status = weibo)
            print "OK"
        elif choice == '2':
            weibo = raw_input("Enter your word here: \n")
            root = Tkinter.Tk()
            root.withdraw()
            pic_dir = tkFileDialog.askopenfilename(parent=root,initialdir="/",title='Please select the picture directory (<5M)')
            response = self.client.statuses.upload.post(status = weibo, pic = open(pic_dir))
            print "OK"

if  __name__ =='__main__':
    print "*****Welcome to tianchiapp interactive weibo tool*****"
    print "*Is this your first time to use tianchiapp?(y/n)*"
    choice = raw_input()

    # create a api client to weibo
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

    if choice == 'y' or choice == 'Y':
        # Open a tab in browser to let user enter weibo username and pswd
        code = login_weibo()
        r = client.request_access_token(code)
        access_token = r.access_token
        expires_in = r.expires_in 
        client.set_access_token(access_token, expires_in)
        
        user_code = {'access_token':access_token,'expires_in':expires_in}
        dump_yaml('user_code.yaml',user_code)
    elif choice == 'n' or choice == 'N':
        user_code = read_yaml('user_code.yaml')
        print user_code
        client.set_access_token(user_code['access_token'], user_code['expires_in'])
    else:
        print "Wrong choice.. exiting.."
        sys.exit(0)

    print "Login done..."
    wb = weibo(client)
    while(True):

        wb.main_manu()
        choice = raw_input("Choose from manu: ")
        try:
            method = getattr(wb,wb.choice_dict[choice])
            if not method:
                raise Exception("Method %s not implemented" % method)
            method()
        except:
            print "Error occur when process choice " + choice
        # dict[choice]: try except
        print "Press enter to exit, C to return main manu..."
        
        choice = raw_input()
        if choice == "C" or choice == 'c':
            continue
        else:
            break

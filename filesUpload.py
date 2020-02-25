import requests
import json
import numpy as np

# user Token
TOKEN = "xxxxxxxxxxxxxx"
# uketsuke joh
CHANNEL = "xxxxxx"

def sendSlack(imgPath, msg, title):
    files = {'file': open(imgPath, 'rb')}
    param = {
	'token':TOKEN,
	'channels':CHANNEL,
	'filename':"filename", #img file name 
	'initial_comment':msg, # messege
	'title':title #imgfile title 
    }
    requests.post(url="https://slack.com/api/files.upload", params=param, files=files)

    

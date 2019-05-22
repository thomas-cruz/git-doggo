import time
import sys
import tweepy
import requests
import json


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


INTERVAL = 60 * 60 * 6  # tweet every 6 hours
Iauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
message_index = 29

while True:
    url = 'https://api.github.com/search/commits?q=doggo&sort=committer-date'
    response = requests.get(url, headers = {"Accept": "application/vnd.github.cloak-preview"}, verify=True)
    parsed_json = json.loads(response.text)
    prev_commit = parsed_json['items'][message_index]['commit']['message']
    while message_index > 0:
    	commit = parsed_json['items'][message_index]['commit']['message']
    	if(commit == prev_commit):
    		message_index = message_index - 1
    		commit = parsed_json['items'][message_index]['commit']['message']
    	print(commit)
    	print (len(parsed_json['items']))
    	print("about to create status...")
    	ad = commit
    	prev_commit = commit
    	try:
    	    api.update_status(ad)
    	    time.sleep(INTERVAL)
    	except:
    	    message_index = message_index - 1
    	    break

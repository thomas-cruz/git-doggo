import time
import sys
import tweepy
import requests
import json


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


INTERVAL = 3600 #tweets every hour
#INTERVAL = 15  # every 15 seconds, for testing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
message_index = 29 #number of commits returned by github api is 30

while True:
    url = 'https://api.github.com/search/commits?q=doggo&sort=committer-date'
    response = requests.get(url, headers = {"Accept": "application/vnd.github.cloak-preview"}, verify=True)
    parsed_json = json.loads(response.text)
    prev_commit = parsed_json['items'][message_index]['commit']['message']
    while message_index > 0: #iterating through commits
    	commit = parsed_json['items'][message_index]['commit']['message']
    	if(commit == prev_commit): #check if last tweet is same as current tweet
    		message_index = message_index - 1
    		commit = parsed_json['items'][message_index]['commit']['message']
    	print(commit)
    	print("about to create status...")
    	prev_commit = commit
    	try: #this is for catching duplicate tweets
    	    api.update_status(commit)
    	    time.sleep(INTERVAL)
    	except: #starts loop again
    	    message_index = message_index - 1
    	    break

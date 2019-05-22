import time
import sys
import tweepy
import requests
from requests.auth import HTTPDigestAuth
import json


# from credentials import *  # use this one for testing

use this for production; set vars in heroku dashboard
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


# INTERVAL = 60 * 60 * 6  # tweet every 6 hours
INTERVAL = 15  # every 15 seconds, for testing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


url = 'https://api.github.com/search/commits?q=doggo&sort=committer-date'
response = requests.get(url, headers = {"Accept": "application/vnd.github.cloak-preview"}, verify=True)
parsed_json = json.loads(response.text)
message_index = 29
while True:
	prev_commit = parsed_json['items'][message_index]['commit']['message']
	commit = parsed_json['items'][message_index]['commit']['message']
	if(commit == prev_commit):
		message_index = message_index - 1
		commit = parsed_json['items'][message_index]['commit']['message']
	print(commit)
	print (len(parsed_json['items']))
	print("about to create status...")
	ad = commit
	api.update_status(ad)
time.sleep(INTERVAL)
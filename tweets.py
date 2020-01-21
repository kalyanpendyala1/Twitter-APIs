
#-----Importing Libraries-----------`   `
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv
import json
import sys



######## twitter client #############
#--------Authentication Variables-------------------
consumer_key = 'Kwz2vDa2ELvLE4PxlT1Fk46X1'
consumer_secret = 'wYc74pP03WKULBK7YoE0yuf2v5wACaWjXfVzFU338IpRY7GhpQ'
access_token = '1040115221770260481-Dkp5awYVXfidVwTGaMFCzG8cZA9R7T'
access_token_secret = 'cI9nwtql9au9QyWZPuDTruuM5WXVCsded5hnCcZbwR442'

#--------------Twitter Authentication------------------
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#-------------variable to store our key word-----------
csvFile = open('test.csv', 'a')
csvWriter = csv.writer(csvFile)
keyword = input("Enter your Search Keyword: ")
n_tweets = int(input('enter the number of tweets: '))
for tweet in tweepy.Cursor(api.search, q=keyword, lang ='en').items(n_tweets):
    csvWriter.writerow([tweet.text.encode('utf-8', 'ignore')])
csvFile.close()
#------------------Twitter Advanced Search------------
"""
Tweets containing all words in any position (“Twitter” and “search”)
Tweets containing exact phrases (“Twitter search”)
Tweets containing any of the words (“Twitter” or “search”)
Tweets excluding specific words (“Twitter” but not “search”)
Tweets with a specific hashtag (#twitte
"""
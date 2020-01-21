

###Sentimental Analysis with Twitter

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv, json

#--------Authentication Variables-------------------
consumer_key = 'Kwz2vDa2ELvLE4PxlT1Fk46X1'
consumer_secret = 'wYc74pP03WKULBK7YoE0yuf2v5wACaWjXfVzFU338IpRY7GhpQ'
access_token = '1040115221770260481-Dkp5awYVXfidVwTGaMFCzG8cZA9R7T'
access_token_secret = 'cI9nwtql9au9QyWZPuDTruuM5WXVCsded5hnCcZbwR442'


#--------------Twitter Authentication------------------
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)




class MyStreamListener(tweepy.StreamListener):
    limit = int(input("Enter the Streaming time Limit: "))

    def __init__(self, time_limit = limit):
        self.start_time = time.time()
        self.limit = time_limit


    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            tweet = data.split(',"text":"')[1].split('","source')[0]
            #tweet = tweet.split('<a href=')[0]
            print(tweet)
            tweet = json.loads(data)
            text = tweet["text"]
            with open('test.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([text])
            return True
        else:

            return False

    def on_status(self, status):
        print(status.text)


    def on_error(self, status):
        print(status)
        return False

twitterStream = Stream(auth, MyStreamListener())
keyword = []
keyword = [input('Enter your Search Keyword or Hashtag: ')]
twitterStream.filter(track=keyword, languages = ['en'])
api = tweepy.API(auth)

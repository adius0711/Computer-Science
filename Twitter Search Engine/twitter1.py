'''
@author: Souvik Das
Institute: University at Buffalo
'''
#!/usr/bin/env python

import tweepy
import json
from time import sleep
import time

def write_config(data):
        with open("data.json", 'w') as json_file:
            json.dump(data, json_file)

class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler("HVQ0uFdMwqvLOQXMAhty5Bhk4", "zPWOPDh13kuoayIVo5PODCXtZQQay3uz5Idg8IGWhlNXcaMD8v")
        self.auth.set_access_token("1432395584380489732-toGacKiRTXw0xybLzpJGuLWGtWNkaX", "TcV45CaWvwOQKGnapmBTd8N3Q9eYFGAQuXD8YpngQIthq")
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def _meet_basic_tweet_requirements(self):
        '''
        Add basic tweet requirements logic, like language, country, covid type etc.
        :return: boolean
        '''
        raise NotImplementedError

    def get_tweets_by_poi_screen_name(self, screen_name,count):
        poi_tweets = []
        for status in tweepy.Cursor(self.api.user_timeline,id = screen_name, tweet_mode="extended").items(count):
            # print(status._json)
            poi_tweets.append(status._json)
        return poi_tweets
        '''
        Use user_timeline api to fetch POI related tweets, some postprocessing may be required.
        :return: List
        '''
        raise NotImplementedError

    def get_tweets_by_lang_and_keyword(self,keyword,count):
        keyword_tweets = []
        for status in tweepy.Cursor(self.api.search, q=keyword, tweet_mode="extended").items(count):
            keyword_tweets.append(status._json)
        return keyword_tweets
            
        '''
        Use search api to fetch keywords and language related tweets, use tweepy Cursor.
        :return: List
        '''
        raise NotImplementedError

    def get_replies(self, user_id, tweet_id):
        # print('to:{}'.format(user_id))
        # print(tweet_id)
        replies=[]
        # time.sleep(600)
        for tweet in tweepy.Cursor(self.api.search,q='to:'+user_id, result_type='recent', timeout=999999, tweet_mode="extended").items(1000):
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if (tweet.in_reply_to_status_id_str==tweet_id):
                    replies.append(tweet._json)
        # write_config({"data": replies})
        return replies
        '''
        Get replies for a particular tweet_id, use max_id and since_id.
        For more info: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines
        :return: List
        '''

# twitter = Twitter()
# # raw_tweets = twitter.get_tweets_by_poi_screen_name('Akki_Gunner04')
# raw_tweets = twitter.get_tweets_by_lang_and_keyword()
# print(raw_tweets)





# '''
# @author: Souvik Das
# Institute: University at Buffalo
# '''

# import tweepy


# class Twitter:
#     def __init__(self):
#         self.auth = tweepy.OAuthHandler("MacliSSKgriseyKjUYIpkUq8x", "HQG6ufwkYaIbGKnjDhEuaIqzk7pqp4isKaZacsMS8OTZ3lPN7P")
#         self.auth.set_access_token("272272010-sDwuIOVCf4Pglq08cuMSkByVK8Ge2s1i6uREaU5B", "G8RucqmIGN5OXQAYoERYWVdc6GU9AfKM0MfGfU6EQOVnj")
#         self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#     def _meet_basic_tweet_requirements(self):
#         '''
#         Add basic tweet requirements logic, like language, country, covid type etc.
#         :return: boolean
#         '''
# #         raise NotImplementedError

#     def get_tweets_by_poi_screen_name(self, screen_name, count):
#         '''
#         Use user_timeline api to fetch POI related tweets, some postprocessing may be required.
#         :return: List
#         '''
#         temptweets = []
#         for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=screen_name, result_type='recent', timeout=999999,tweet_mode='extended').items(500):
#             #if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
#             temptweets.append(tweet._json)
#             print("POI TWEETS")
#             # print(temptweets)
#         return(temptweets)
#         #         raise NotImplementedError

#     def get_tweets_by_lang_and_keyword(self, key_word, lang, count):
#         '''
#         Use search api to fetch keywords and language related tweets, use tweepy Cursor.
#         :return: List
#         '''
#         tempkeytweets = []
#         for tweet in tweepy.Cursor(self.api.search, q = key_word + '-filter:retweets', lang = lang, timeout=999999,tweet_mode='extended').items(count):
#             if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
#                 tempkeytweets.append(tweet._json)
#         return(tempkeytweets)
#         #         raise NotImplementedError

#     def get_replies(self, user_id, tweet_id):
#         '''
#         Get replies for a particular tweet_id, use max_id and since_id.
#         For more info: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines
#         :return: List
#         '''
#         # print('to:{}'.format(user_id))
#         # print(tweet_id)
#         replies = tweepy.Cursor(self.api.search, q='to:'+user_id, result_type='recent', timeout=999999, tweet_mode='extended').items(100)
#         # print(replies)
#         replied_thread = list()
#         for reply in replies:
#             if(reply.in_reply_to_status_id_str == tweet_id):
#                 # print("tweet_id ",reply.in_reply_to_status_id_str)
#                 replied_thread.append(reply._json)
#         # rint(replied_thread)p
#         return replied_thread

#         # replies = []
#         # reply_count = 0
#         # a = json.loads(tweet._json)
#         # x = []
#         # for i in a:
#         # x.append(a[i])

#         # Collect all replies to that handle
#         # for i in x:
#         # for reply in tweepy.Cursor(api.search, q="to:@" + handle, since_id=since_id, tweet_mode="extended").items(max_id):
#         #     reply_count += 1
#         #     print("Downloaded {0} replies for handle {1}".format(reply_count, handle))
#         #     replies.append(reply._json)

#         # return replies
#         # raise NotImplementedError

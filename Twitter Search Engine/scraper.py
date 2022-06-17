'''
@author: Souvik Das
Institute: University at Buffalo
'''

import json
import datetime
from time import time
import time
import pandas as pd
from twitter1 import Twitter
from tweet_preprocessor_shared import TWPreprocessor
from indexer import Indexer

reply_collection_knob = True


def read_config():
    with open("config.json") as json_file:
        data = json.load(json_file)

    return data


def write_config(data):
    with open("config.json", 'w') as json_file:
        json.dump(data, json_file)


def save_file(data, filename):
    df = pd.DataFrame(data)
    df.to_pickle("data/" + filename)


def read_file(type, id):
    return pd.read_pickle(f"data/{type}_{id}.pkl")


def main():
    config = read_config()
    indexer = Indexer()
    twitter = Twitter()
    pois = config["pois"]
    keywords = config["keywords"]
    raw_poi_tweets = []
    timeout = 500
    raw_keywords_tweets = []
    # indexer.do_initial_setup()
    # for i in range(len(pois)):
    #     if pois[i]["finished"] == 0:
    #         print(f"---------- collecting tweets for poi: {pois[i]['screen_name']}")

    #         raw_poi_tweets = twitter.get_tweets_by_poi_screen_name(pois[i]['screen_name'],pois[i]['count'])  # pass args as needed
    #         country = pois[i]['country']
    #         processed_tweets = []
    #         for tw in raw_poi_tweets:
    #             processed_tweets.append(TWPreprocessor.preprocess('poi',tw,country))
    #         # indexer.add_fields()
    #         indexer.create_documents(processed_tweets)
    #         # print(processed_tweets)
    #         pois[i]["finished"] = 1
    #         pois[i]["collected"] = len(processed_tweets)

    #         write_config({
    #             "pois": pois, "keywords": keywords
    #         })

    #         save_file(processed_tweets, f"poi_{pois[i]['id']}.pkl")
    #         print("------------ process complete -----------------------------------")
    #         print(f'Sleeping for {timeout} seconds')
    #         # time.sleep(timeout)

    # for i in range(len(keywords)):
    #     if keywords[i]["finished"] == 0:
    #         print(f"---------- collecting tweets for keyword: {keywords[i]['name']}")

    #         raw_tweets = twitter.get_tweets_by_lang_and_keyword(keywords[i]['name'], keywords[i]['count'])  # pass args as needed

    #         processed_tweets = []
    #         for tw in raw_tweets:
    #             processed_tweets.append(TWPreprocessor.preprocess('keyword',tw,keywords[i]['country']))

    #         indexer.create_documents(processed_tweets)

    #         keywords[i]["finished"] = 1
    #         keywords[i]["collected"] = len(processed_tweets)

    #         write_config({
    #             "pois": pois, "keywords": keywords
    #         })

    #         save_file(processed_tweets, f"keywords_{keywords[i]['id']}.pkl")

    #         print("------------ process complete -----------------------------------")
    #         print(f'Sleeping for {timeout} seconds')
    #         # time.sleep(timeout)

    if reply_collection_knob:
        for i in range(len(pois)):
            if pois[i]['reply_finished'] == 0:
                print(f"---------- collecting reply_tweets for poi: {pois[i]['screen_name']}")
        
                raw_tweets = twitter.get_tweets_by_poi_screen_name(pois[i]['screen_name'],count=2000)  # pass args as needed
                country = pois[i]['country']
                # processed_tweets = []
                print("Done with collecting tweets")
                replies = []
                for tw in raw_tweets:
                    reply = twitter.get_replies(pois[i]['screen_name'], tw['id_str'])
                    # print("*****************************************************************************reply:", reply)
                    replies.append(reply)
                processed_tweets = []
                for r in replies:
                    for x in r:
                        processed_tweets.append(TWPreprocessor.preprocess("reply", x, pois[i]['country']))
                    # print(r['in_reply_to_status_id'])
                # print(replies)

                # for reply_tweets in replies:
                #     processed_tweets.append(TWPreprocessor.preprocess("poi", tw, country))
                # # indexer.add_fields()
                indexer.create_documents(processed_tweets)
                pois[i]["replies_collected"] = len(processed_tweets)
                print("------------ process complete -----------------------------------")
                print(f'Sleeping for {timeout} seconds')
                # time.sleep(timeout)
        # raise NotImplementedError


if __name__ == "__main__":
    main()






















# '''
# @author: Souvik Das
# Institute: University at Buffalo
# '''

# import json
# import datetime
# import re
# import pandas as pd
# from twitter1 import Twitter
# from tweet_preprocessor_shared import TWPreprocessor
# from indexer import Indexer

# reply_collection_knob = True


# def read_config():
#     with open("C:\\Users\\ashwi\\Downloads\\CSE 535 Information Retrieval\\CSE_4535_Fall_2021-master\\CSE_4535_Fall_2021-master\\project4\\config.json") as json_file:
#         data = json.load(json_file)

#     return data


# def write_config(data):
#     with open("config.json", 'w') as json_file:
#         json.dump(data, json_file)


# def save_file(data, filename):
#     df = pd.DataFrame(data)
#     df.to_pickle("data/" + filename)


# def read_file(type, id):
#     return pd.read_pickle(f"data/{type}_{id}.pkl")


# def main():
#     config = read_config()
#     indexer = Indexer()
#     twitter = Twitter()

#     pois = config["pois"]
#     keywords = config["keywords"]
#     raw_tweets = []
#     for i in range(len(pois)):
#         if pois[i]["finished"] == 0:
#             print(f"---------- collecting tweets for poi: {pois[i]['screen_name']}")

#             raw_tweets = twitter.get_tweets_by_poi_screen_name(pois[i]['screen_name'], pois[i]['count'])  # pass args as needed
#             cls = 'poi'
#             # print(raw_tweets)
#             processed_tweets = []
#             for tw in raw_tweets:
#                 print(tw)
#                 processed_tweets.append(TWPreprocessor.preprocess(cls, tw, pois[i]['country']))

#             indexer.create_documents(processed_tweets)

#             pois[i]["finished"] = 1
#             pois[i]["collected"] = len(processed_tweets)

#             write_config({
#                 "pois": pois, "keywords": keywords
#             })

#             save_file(processed_tweets, f"poi_{pois[i]['id']}.pkl")
#             print("------------ process complete -----------------------------------")

#     for i in range(len(keywords)):
#         if keywords[i]["finished"] == 0:
#             print(f"---------- collecting tweets for keyword: {keywords[i]['name']}")

#             raw_tweets = twitter.get_tweets_by_lang_and_keyword(keywords[i]['name'], keywords[i]['lang'], keywords[i]['count'])  # pass args as needed

#             processed_tweets = []
#             for tw in raw_tweets:
#                 processed_tweets.append(TWPreprocessor.preprocess(tw))

#             indexer.create_documents(processed_tweets)

#             keywords[i]["finished"] = 1
#             keywords[i]["collected"] = len(processed_tweets)

#             write_config({
#                 "pois": pois, "keywords": keywords
#             })

#             save_file(processed_tweets, f"keywords_{keywords[i]['id']}.pkl")

#             print("------------ process complete -----------------------------------")

#     if reply_collection_knob:
#         # Write a driver logic for reply collection, use the tweets from the data files for which the replies are to collected.
#         replies = []
#         for t in raw_tweets:
#             reply = twitter.get_replies(t['user']['screen_name'],t['id_str'])
#             replies.append(reply)

#         # Write a driver logic for reply collection, use the tweets from the data files for which the replies are to collected.
#         # print(len(replies))
#         processed_tweets = []
#         for tw in replies:
#             print(tw['in_reply_to_status_id'])
#             processed_tweets.append(TWPreprocessor.preprocess('reply',tw,'country'))

#         indexer.create_documents(processed_tweets)
#         print("------------ process complete -----------------------------------")
#         raise NotImplementedError


# if __name__ == "__main__":
#     main()

'''
@author: Souvik Das
Institute: University at Buffalo
'''

# import demoji, re, datetime
# import preprocessor
# import json
import demoji, re, datetime,time
import preprocessor
from time import mktime
# from datetime import datetime, timedelta

import json
demoji.download_codes()


class TWPreprocessor:
    @classmethod
    def preprocess(self, cls, tweet, country):
        # print(tweet)
        # tweet = json.loads(tw)
        with open("data.json", 'w') as json_file:
            json.dump(tweet, json_file)
        # print('place',tweet['place'])
        processed = {}
        if cls == 'poi':
            processed['poi_name'] = tweet['user']['screen_name']
            processed['poi_id'] = tweet['user']['id']
        processed['verified'] = tweet['user']['verified']
        processed['country'] = country
        processed['id'] = tweet['id_str']
        processed['tweet_text'] = tweet['full_text']
        processed['tweet_lang'] = tweet['lang']
        processed['hashtags'] = _get_entities(tweet,'hashtags')
        processed['mentions'] = _get_entities(tweet, 'mentions')
        processed['tweet_urls'] = _get_entities(tweet,'urls')
        if cls == 'reply':
            processed['replied_to_tweet_id'] = tweet['in_reply_to_status_id']
            processed['replied_to_user_id'] = tweet['in_reply_to_user_id']
        text, emo = _text_cleaner(tweet['full_text'])
        if cls == 'reply':
            processed['reply_text'] = text 
        if tweet['lang'] == 'en':
            processed['text_en'] = text
        elif tweet['lang'] == 'es':
            processed['text_es'] = text
        elif tweet['lang'] == 'hi':
            processed['text_hi'] = text
        processed['tweet_emoticons'] = emo
        processed['tweet_date'] = _get_tweet_date(tweet['created_at']) 
        # if cls == 'reply':
        #     print(processed)
        return processed 
        '''
        Do tweet pre-processing before indexing, make sure all the field data types are in the format as asked in the project doc.
        :param tweet:
        :return: dict
        '''

        raise NotImplementedError


def _get_entities(tweet, type=None):
    result = []
    if type == 'hashtags':
        hashtags = tweet['entities']['hashtags']

        for hashtag in hashtags:
            result.append(hashtag['text'])
    elif type == 'mentions':
        mentions = tweet['entities']['user_mentions']

        for mention in mentions:
            result.append(mention['screen_name'])
    elif type == 'urls':
        urls = tweet['entities']['urls']

        for url in urls:
            result.append(url['url'])

    return result


def _text_cleaner(text):
    emoticons_happy = list([
        ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
        ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
        '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
        'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
        '<3'
    ])
    emoticons_sad = list([
        ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
        ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
        ':c', ':{', '>:\\', ';('
    ])
    all_emoticons = emoticons_happy + emoticons_sad

    emojis = list(demoji.findall(text).keys())
    clean_text = demoji.replace(text, '')

    for emo in all_emoticons:
        if (emo in clean_text):
            clean_text = clean_text.replace(emo, '')
            emojis.append(emo)

    # clean_text = preprocessor.clean(text)
    # preprocessor.set_options(preprocessor.OPT.EMOJI, preprocessor.OPT.SMILEY)
    # emojis= preprocessor.parse(text)

    return clean_text, emojis


def _get_tweet_date(tweet_date):
    return datetime.datetime.strftime(datetime.datetime.strptime(tweet_date,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')


def _hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
            + datetime.timedelta(hours=t.minute // 30))


























# '''
# @author: Souvik Das
# Institute: University at Buffalo
# '''

# import demoji, re, datetime,time
# import preprocessor
# from time import mktime
# from datetime import datetime, timedelta
# import json

# def hour_rounder(t):
#     # Rounds to nearest hour by adding a timedelta hour if minute >= 30
#     return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
#                +timedelta(hours=t.minute//30))


# # demoji.download_codes()
# class TWPreprocessor:
#     @classmethod
#     def preprocess(self, cls, tw, country):
#         # print(tweet)
#         tweet = json.loads(tw)
#         with open("data.json", 'w') as json_file:
#             json.dump(tweet, json_file)
#         processed = {}
#         if cls == 'poi':
#             processed['poi_name'] = tweet['user']['screen_name']
#             processed['poi_id'] = tweet['user']['id']
#         if cls == 'reply':
#             processed['replied_to_tweet_id'] = tweet['in_reply_to_status_id']
#             processed['replied_to_user_id'] = tweet['in_reply_to_user_id']
#         processed['verified'] = tweet['user']['verified']
#         processed['country'] = country
#         processed['id'] = tweet['id_str']
#         processed['tweet_text'] = tweet['full_text']
#         processed['tweet_lang'] = tweet['lang']
#         processed['hashtags'] = _get_entities(tweet,'hashtags')
#         processed['mentions'] = _get_entities(tweet, 'mentions')
#         processed['tweet_urls'] = _get_entities(tweet,'urls')
#         text, emo = _text_cleaner(tweet['full_text'])
#         if cls == 'reply':
#             processed['reply_text'] = text 
#         if tweet['lang'] == 'en':
#             processed['text_en'] = text
#         elif tweet['lang'] == 'es':
#             processed['text_es'] = text
#         elif tweet['lang'] == 'hi':
#             processed['text_hi'] = text
#         processed['tweet_emoticons'] = emo
#         processed['tweet_date'] = _get_tweet_date(tweet['created_at']) 
#         if cls == 'reply':
#             print(processed)
#         return processed

# # class TWPreprocessor:
# #     @classmethod
# #     def preprocess(cls, tweet):
# #         '''
# #         Do tweet pre-processing before indexing, make sure all the field data types are in the format as asked in the project doc.
# #         :param tweet:
# #         :return: dict
# #         '''
        
# # #         Add text_xx part
# # #         print("printing cls")
# # #         print(cls)
# # #         print("printing twweet")
# # #         print(tweet)
# # #         print("====== type ======")
# # #         print(type(tweet))
# # #         a = {"country" : "India"}
        

# #         # def preprocess(self, cls, tw, country):
# #         # print(tweet)
# #         print(tweet)
# #         tweet = json.loads(tweet)
# #         with open("data.json", 'w') as json_file:
# #             json.dump(tweet, json_file)
# #         processed = {}
# #         if cls == 'poi':
# #             processed['poi_name'] = tweet['user']['screen_name']
# #             processed['poi_id'] = tweet['user']['id']
# #         if cls == 'reply':
# #             processed['replied_to_tweet_id'] = tweet['in_reply_to_status_id']
# #             processed['replied_to_user_id'] = tweet['in_reply_to_user_id']
# #         processed['verified'] = tweet['user']['verified']
# #         processed['country'] = country
# #         processed['id'] = tweet['id_str']
# #         processed['tweet_text'] = tweet['full_text']
# #         processed['tweet_lang'] = tweet['lang']
# #         processed['hashtags'] = _get_entities(tweet,'hashtags')
# #         processed['mentions'] = _get_entities(tweet, 'mentions')
# #         processed['tweet_urls'] = _get_entities(tweet,'urls')
# #         text, emo = _text_cleaner(tweet['full_text'])
# #         if cls == 'reply':
# #             processed['reply_text'] = text 
# #         if tweet['lang'] == 'en':
# #             processed['text_en'] = text
# #         elif tweet['lang'] == 'es':
# #             processed['text_es'] = text
# #         elif tweet['lang'] == 'hi':
# #             processed['text_hi'] = text
# #         processed['tweet_emoticons'] = emo
# #         processed['tweet_date'] = _get_tweet_date(tweet['created_at']) 
# #         if cls == 'reply':
# #             processed['reply_text'] = text
# #         return processed













#         handles = {

#             "USA": ["JoeBiden", "CDCgov","VP", "NYGovCuomo", "DonaldJTrumpJr", "POTUS", "XavierBecerra", "AOC", "BernieSanders"],
#             "India": ["AmitShah","MoHFW_INDIA","narendramodi", "RaghusharmaINC", "mansukhmandviya", "NitishKumar", "ArvindKejriwal", "msisodia", "rajnathsingh"],
#             "Mexico": ["lopezobrador_", "SSaludCdMx", "SSalud_mx", "PMunozLedo", "m_ebrard", "Claudiashein", "alejandromurat", "AlfonsoDurazo", "EPN"]}


#         handle_ids = {
#             "JoeBiden":["939091","USA"],
#             "CDCgov" : ["146569971", "USA"],
#             "VP": ["803694179079458816", "USA"],
#             "NYGovCuomo" : ["939091","USA"],
#             "POTUS": ["1349149096909668363", "USA"],
#             "DonaldJTrumpJr": ["939091","USA"],
#             "XavierBecerra": ["565469671","USA"],
#             "AOC": ["138203134","USA"],
#             "BernieSanders": ["216776631","USA"],
    
#             "AmitShah": ["1447949844","INDIA"],
#             "narendramodi":["18839785","INDIA"],
#             "MoHFW_INDIA": ["2596143056","INDIA"],
#             "RaghusharmaINC": ["517767805","INDIA"],
#             "mansukhmandviya":["432697203","INDIA"],
#             "NitishKumar": ["143409075","INDIA"],
#             "ArvindKejriwal": ["405427035","INDIA"],
#             "msisodia": ["30417501","INDIA"],
#             "rajnathsingh": ["1346439824","INDIA"],
    
    
#             "lopezobrador_" : ["82119937", "MEXICO"],
#             "SSaludCdMx" : ["584164599", "MEXICO"],
#             "SSalud_mx" : ["132225222", "MEXICO"],
#             "PMunozLedo" : ["363978511", "MEXICO"],
#             "m_ebrard": ["64798737", "MEXICO"],
#             "Claudiashein" : ["591361197", "MEXICO"],
#             "alejandromurat" : ["90954759", "MEXICO"],
#             "AlfonsoDurazo" : ["211307172", "MEXICO"],
#             "EPN" : ["2897441", "MEXICO"],
#         }
        
#         tweet_dict = {
#             "id" : tweet["id"],
#             "country" : "",
#             "tweet_lang":tweet["lang"],
#             "tweet_text": tweet["full_text"],
#             "text_en": "",
#             "text_hi": "",
#             "text_es": "",
#             "tweet_date": str(tweet["created_at"]),
#             "verified": False,
#             "poi_id": "",
#             "poi_name": ""
#         }
#          # Round-off date
#         ts = time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
#         ts = datetime.fromtimestamp(mktime(ts))
#         ts = hour_rounder(ts)
#         ts = ts.strftime('%Y-%m-%dT%H:%M:%SZ')
#         tweet_dict["tweet_date"] = ts
        
#         if(tweet["lang"] == "en"):
#             tweet_dict["country"] = "USA"
#         elif(tweet["lang"] == "hi"):
#             tweet_dict["country"] = "INDIA"
#         elif(tweet["lang"] == "es"):
#             tweet_dict["country"] = "Mexico"
            
#         if(tweet["lang"] == "en"):
#             tweet_dict["text_en"] = tweet["full_text"]
#         elif(tweet["lang"] == "hi"):
#             tweet_dict["text_hi"] = tweet["full_text"]
#         elif(tweet["lang"] == "es"):
#             tweet_dict["text_es"] = tweet["full_text"]
            
      
#         if("screen_name" in tweet["user"]):
#             if(tweet["user"]["screen_name"] in handle_ids.keys()):
#                 #print(type(tweet["user"]["screen_name"]))
#                 tweet_screen_name = tweet["user"]["screen_name"]
#                 poi_id = handle_ids[tweet_screen_name]
#                 tweet_dict["poi_id"] = poi_id[0]
#                 tweet_dict["poi_name"] = tweet["user"]["screen_name"]
#                 tweet_dict["country"] = handle_ids[tweet["user"]["screen_name"]][1]
#         if tweet_dict["poi_name"] in handle_ids.keys():
#             tweet_dict["verified"] = True       
        
#         return tweet_dict

# #         raise NotImplementedError


# def _get_entities(tweet, type=None):
#     result = []
#     if type == 'hashtags':
#         hashtags = tweet['entities']['hashtags']

#         for hashtag in hashtags:
#             result.append(hashtag['text'])
#     elif type == 'mentions':
#         mentions = tweet['entities']['user_mentions']

#         for mention in mentions:
#             result.append(mention['screen_name'])
#     elif type == 'urls':
#         urls = tweet['entities']['urls']

#         for url in urls:
#             result.append(url['url'])

#     return result


# def _text_cleaner(text):
#     emoticons_happy = list([
#         ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
#         ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
#         '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
#         'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
#         '<3'
#     ])
#     emoticons_sad = list([
#         ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
#         ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
#         ':c', ':{', '>:\\', ';('
#     ])
#     all_emoticons = emoticons_happy + emoticons_sad

#     emojis = list(demoji.findall(text).keys())
#     clean_text = demoji.replace(text, '')

#     for emo in all_emoticons:
#         if (emo in clean_text):
#             clean_text = clean_text.replace(emo, '')
#             emojis.append(emo)

#     clean_text = preprocessor.clean(text)
#     # preprocessor.set_options(preprocessor.OPT.EMOJI, preprocessor.OPT.SMILEY)
#     # emojis= preprocessor.parse(text)

#     return clean_text, emojis


# def _get_tweet_date(tweet_date):
#     return _hour_rounder(datetime.datetime.strptime(tweet_date, '%a %b %d %H:%M:%S +0000 %Y'))


# def _hour_rounder(t):
#     # Rounds to nearest hour by adding a timedelta hour if minute >= 30
#     return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
#             + datetime.timedelta(hours=t.minute // 30))

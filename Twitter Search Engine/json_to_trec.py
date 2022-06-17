# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
#import urllib.request 
# import urllib2
import urllib.request
query = "005 covid"
input_query = query[4:]
print(input_query)
input_query = input_query.strip('\n').replace(':', '')
print(input_query)
encoded_query = urllib.parse.quote(input_query)
print(encoded_query)

# change the url according to your own corename and query
# inurl = 'http://52.201.239.242:8983/solr/IRF21_p3_demo/select?q=*;*&fl=id%2Cscore&wt=json&indent=true&rows=20'
outfn = '5.txt'
IRModel='IRF21P4' #either bm25 or vsm
# inurl = "http://18.207.120.9:8983/solr/VSM/select?fl=id%2Cscore&debugQuery=false&df=text_en&fl=text_en&q.op=OR&q=*US%20air%20dropped%2050%20tons%20of%20Ammo%20on%20Syria*"
inurl = 'http://52.87.175.223:8983/solr/' + IRModel + '/select?fl=id%2Cscore&defType=lucene&q=text_en%3A(' \
                            + encoded_query + ')%20or%20text_hi%3A(' + encoded_query + ')%20or%20text_es%3A(' \
                            + encoded_query + ')%20or%20hashtags%3A(' + encoded_query + ')' + '&rows=100&wt=json'

# http://52.87.175.223:8983/solr/IRF21P4/select?fl=id%2Cscore&defType=lucene&q=text_en%3A(' \
#                             + encoded_query + ')%20or%20text_hi%3A(' + encoded_query + ')%20or%20text_es%3A(' \
#                             + encoded_query + ')%20or%20hashtags%3A(' + encoded_query + ')' + '&rows=100&wt=json'
# change query id and IRModel name accordingly

http://52.87.175.223:8983/solr/VSM/select?fl=id%2Cscore&debugQuery=false&df=text_en&fl=text_en&q.op=OR&q=*US%20air%20dropped%2050%20tons%20of%20Ammo%20on%20Syria*

qid = '005'

outf = open(outfn, 'a+')
# data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
data = urllib.request.urlopen(inurl)
print(data)
docs = json.load(data)['response']['docs']
print(docs)
# the ranking should start from 1 and increase
rank = 1
for doc in docs:
    # if IRModel == "IRF21_p3_demo":
    #     IRModel = "BM25"
    outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
    rank += 1
outf.close()

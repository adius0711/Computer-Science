import flask
from flask import Flask, request
import requests
app = Flask(__name__)

def getData(query,poi,country,lang):
    AWS_IP = '107.20.108.118'
    IRModel = 'IRF21P4'
    new_query = query.replace(" ","%20")
    final_url = f'http://{AWS_IP}:8983/solr/{IRModel}/select?q=text_en%20%3A%20%22{new_query}%22%0Atext_hi%3A%20%22{new_query}%22%0Atext_es%3A%20%22{new_query}%22&q.op=OR&wt=json&df=text_en%2Ctext_hi%2Ctext_es&rows=20'
    if poi:
        poi_join = "%20".join(poi)
        poi_url = f'({poi_join})'
        final_url = final_url+f'&fq=poi_name%3A{poi_url}'
    if country:
        country_join = "%20".join(country)
        country_url = f'({country_join})'
        final_url = final_url+f'&fq=country%3A{country_url}'
    if lang:
        lang_join = "%20".join(lang)
        lang_url = f'({lang_join})'
        final_url = final_url+f'&fq=tweet_lang%3A{lang_url}'
    print(final_url)
    data = requests.get(final_url)
    resp = data.json()
    docs_resp = resp['response']
    print(docs_resp)
    for doc in docs_resp['docs']:
        doc_id = doc['id']
        reply_url = f'http://{AWS_IP}:8983/solr/{IRModel}/select?fq=replied_to_tweet_id%3A{doc_id}&q.op=OR&q=*%3A*&rows=1000'
        reply_data = requests.get(reply_url)
        reply_resp = reply_data.json()
        if reply_resp['response']['docs']:
            doc['replies'] = reply_resp['response']['docs']
        print(doc)
    return docs_resp

    

@app.route("/tweets")
def get_tweets():
    query = request.args.get('query')
    poi = request.args.get('poi').split(",") if request.args.get('poi') else None
    country = request.args.get('country').split(",") if request.args.get('country') else None
    language = request.args.get('lang').split(",") if request.args.get('lang') else None
    print(query)
    # topic = request.args.get('topic').split(",") if request.args.get('topic') else None
    data = getData(query,poi,country,language)
    return data

if __name__ == '__main__':
    app.run(debug=True)
import flask
from flask import Flask, request
import time
import json
import urllib.request
# from project3.bm25_1 import AWS_IP

# from project3.json_to_trec import IRModel


app = Flask(__name__)


class QueryParser():
    def run_queries(queries):
        IRModel = 'IRF21P4'
        AWS_IP = '3.80.28.72'
        query = queries
        input_query = query[4:]
        print(input_query)
        input_query = input_query.strip('\n').replace(':', '')
        print(input_query)
        encoded_query = urllib.parse.quote(input_query)
        print(encoded_query)
        
        #URLs wouldn't be the same they need to be dynamic and as per the request, this will change
        inurl = f'http://{AWS_IP}:8983/solr/' + IRModel + '/select?fl=id%2Cscore&defType=lucene&q=text_en%3A(' \
                            + encoded_query + ')%20or%20text_de%3A(' + encoded_query + ')%20or%20text_ru%3A(' \
                            + encoded_query + ')' + '&rows=20&wt=json'

        data = urllib.request.urlopen(inurl)
        docs = json.load(data)
        #Determine Output fields












app.route("/execute_query", methods=['POST'])
def execute_query():
    """ This function handles the POST request to your endpoint.
        Do NOT change it."""
    output_location = r"C:\Users\ashwi\Downloads\CSE 535 Information Retrieval\CSE_4535_Fall_2021-master\CSE_4535_Fall_2021-master\project4\output"
    start_time = time.time()

    queries = request.json["queries"]
    """ Running the queries against the pre-loaded index. """
    output_dict = runner.run_queries(queries)

    """ Dumping the results to a JSON file. """
    with open(output_location, 'w') as fp:
        json.dump(output_dict, fp)

    response = {
        "Response": output_dict,
        "time_taken": str(time.time() - start_time),
    }
    return flask.jsonify(response)


if __name__ == "__main__":
    """ Driver code for the project, which defines the global variables.
        Do NOT change it."""


    """ Initialize the project runner"""
    runner = QueryParser()

    """ Index the documents from beforehand. When the API endpoint is hit, queries are run against 
        this pre-loaded in memory index. """

    app.run(host="0.0.0.0", port=9999)

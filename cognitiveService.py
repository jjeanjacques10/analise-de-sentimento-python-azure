# -*- coding: utf-8 -*-
import os, json
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

subscription_key = 'a80b7044b2db461aabbbf4d4295e2d84'
endpoint = 'https://twitter-analitics-service.cognitiveservices.azure.com/'

def authenticateClient():
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credentials=credentials)
    return text_analytics_client

def sentiment():
    client = authenticateClient()
    try:
        with open('twitters.json', 'r') as f:
            documents = json.loads(f.read())
        response = client.sentiment(documents=documents)
        sum = 0
        for document in response.documents:
            print("Document Id: ", document.id, ", Sentiment Score: ",
                  "{:.2f}".format(document.score))
            sum += document.score
        print("Média ====== {}".format((sum/len(response.documents))))
    except Exception as err:
        print("Encountered exception. {}".format(err))
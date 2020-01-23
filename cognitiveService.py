# -*- coding: utf-8 -*-
import os, json
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

#Acessando o arquivo com as keys
with open('env.json', 'r') as f:
    content = json.loads(f.read())
f.close()

subscription_key = content['subscription_key']
endpoint = content['endpoint']

def authenticateClient():
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credentials=credentials)
    return text_analytics_client

def sentiment():
    #Criando um client já autenticado
    client = authenticateClient()
    try:
        #Lendo os tweets que foram salvos anteriormente
        with open('twitters.json', 'r') as f:
            tweets = json.loads(f.read())

        #Fazendo a análise dos sentimentos
        response = client.sentiment(documents=tweets)
        sum_total = 0

        for index, document in enumerate(response.documents):
            tweets[index]["score"] = document.score
            sum_total += document.score

        #Calculo e mostro a média de Scores
        average = (sum_total/len(response.documents)) * 100
        print("Média dos Scores: {0:.2f}%".format(average))

        #Retornando os tweets com o score
        return tweets
    except Exception as err:
        print("Encountered exception. {}".format(err))
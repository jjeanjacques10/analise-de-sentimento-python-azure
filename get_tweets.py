# -*- coding: utf-8 -*-
import tweepy, json, os

def get_tweets():
    try:
        #Acessando o arquivo com as keys
        with open('env.json', 'r') as f:
            content = json.loads(f.read())
        f.close()
        
        chave_consumidor = content['chave_consumidor']
        segredo_consumidor = content['segredo_consumidor']
        token_acesso = content['token_acesso']
        token_acesso_segredo = content['token_acesso_segredo']

        #Fazendo a autenticão
        autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
        autenticacao.set_access_token(token_acesso, token_acesso_segredo)

        twitter = tweepy.API(autenticacao)

        #Fazendo as pesquisa (Você pode alterar o language)
        result = twitter.search(q='jeanjacques1999', count=1000, tweet_mode="extended")
        
        data = []
        for tweet in result:
            data.append({'id':str(tweet._json['id']), 'language':'pt', 'text':tweet._json['full_text']})

        return data
    except Exception as e:
        erro = "Encountered exception. {}".format(e)
        return erro 
        

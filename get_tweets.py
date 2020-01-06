import tweepy, json, os

def get_tweets():
    try:
        with open('env.json', 'r') as f:
            content = json.loads(f.read())
        
        chave_consumidor = content['chave_consumidor']
        segredo_consumidor = content['segredo_consumidor']
        token_acesso = content['token_acesso']
        token_acesso_segredo = content['token_acesso_segredo']

        autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
        autenticacao.set_access_token(token_acesso, token_acesso_segredo)

        twitter = tweepy.API(autenticacao)

        #result = twitter.user_timeline(screen_name='bigdatabrasilday', count=1000, tweet_mode="extended")

        result = twitter.search(q='AluraOnline', count=1000, tweet_mode="extended")
        
        data = []
        for tweet in result:
            data.append({'id':str(tweet._json['id']), 'language':'en', 'text':tweet._json['full_text']})

        with open('twitters.json', 'a', encoding='utf-8') as f:
            json.dump(data, f)

        f.close()
        return True
    except Exception as err:
        print("Encountered exception. {}".format(err))


from get_tweets import get_tweets
from cognitiveService import sentiment
import os, json

def main():
    #Coletandos os tweets
    tweet = get_tweets()
    insert_data(tweet)

    if(tweet):
        #Passando em nossa IA para identificar sentimento
        tweet_score = sentiment()
        insert_data(tweet_score)
    else:
        print(tweet)

def insert_data(data):
    #Apagando o arquivo caso ele exista
    dir = os.listdir()
    for file in dir:
        if file == "twitters.json":
            os.remove(file)

    #Inserindo os dados entro do arquivo twitters.json
    with open('twitters.json', 'a', encoding='utf-8') as f:
        json.dump(data, f)
    f.close()

if __name__ == "__main__":
    main()

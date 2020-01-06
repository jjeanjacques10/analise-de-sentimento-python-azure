from get_tweets import get_tweets

tweet = get_tweets()

if(tweet):
    from cognitiveService import sentiment
    sentiment()
else:
    print(tweet)



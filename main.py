from random import randint
import tweepy
import youtube_api

CONSUMER_KEY = 'XXXXXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)  # will use this object to interact with twitter.com
client = tweepy.Client("XXXX")

# ---- WOEID lookups -------                                                                       
# Miami - 2450022                                                                                  
# USA - 23424977                                                                                   
# ATL - 2357024                                                                                    


def get_trends():
    trends = api.get_place_trends(23424977)
    trends_list = []
    count = 0
    for i in trends[0].get("trends"):
        count += 1
        # print(f"{count}. {i.get('name')} with {i.get('tweet_volume')} tweets")                   
        coinflip = randint(0, 1)
        # print(coinflip)                                                                          
        if coinflip == 1:
            trends_list.append(i.get('name'))
    print(trends_list)
    return trends_list


def send_tweets(trending):
    hastags = ""
    video = youtube_api.get_video()
    for i in trending:
        i = i.replace(" ", "")
        if i[0] != "#":
            hastags += f"#{i} "
        else:
            hastags += f"{i} "
        if len(video) + len(hastags) >= 250:
            break
            # tweet = client.create_tweet(text=f"{video} {hastags}")
    print(f"{video} {hastags}")


trends = get_trends()
send_tweets(trends)                                                                                
import tweepy
import time
# what twitter API uses to verify our account
# verify the twitter API using API key and secret
auth = tweepy.OAuthHandler('os.environ.get("API_KEY")', 'os.environ.get("API_KEY_SECRET")')
auth.set_access_token('os.environ.get("ACCESS_TOKEN")', 'os.environ.get("ACCESS_TOKEN_SECRET")')

# using tweepy.API to authenticate and have access to the API
# creates an api object of tweepy for authentication
api = tweepy.API(auth)

# give informations about me
user = api.me()
print(user.followers_count) # print the number of followers I have

# go through the server and paginate
# try and keep hitting the twitter API until it reaches RateLimitError
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300) # pause this for a couple milliseconds after hitting ratelimiterror
    except StopIteration:
        return

# print all of my followers
# .Cursor is a twitter generator that loops through the iterations and would return RateLimitError when it reaches a certain amount of request too fast
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name) # print all my followers
    break
    

# Generous Bot that follows back other followers
# grab all the followers in my page
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Andrei': # if the user that follows me is named "DatBigNoob"
        follower.follow() # allow me to follow the user
        break

search_string = 'python'
numberOfTweets = 2

# search a specific tweet, searching based on the term search_string and liking the tweet
# loop through how many items 
for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numberOfTweets)):
    try:
        tweet.favorite()
        print('I liked that tweet')
    # if it raises a TweepError
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:   
        break

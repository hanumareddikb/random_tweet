"""This project selects twitter user randomly and tweet him,
    -first we have to intall python-twitter using command:- pip3 install python-twitter
    -we can connect to twitter using Api"""

import twitter
import random

# get twitter followers
api = twitter.Api(consumer_key=' ',
                consumer_secret=' ',
                access_token_key=' ',
                access_token_secret=' ')

followers = api.GetFollowers()

# pick one at random
random_index = random.randint(0, len(followers)-1)
random_follower = followers[random_index]
print(random_follower.screen_name)

# tweet at the random
tweet = f"@{random_follower.screen_name} you are the random follower for today"
api.PostUpdate(tweet)

# to know what is twitted to whom?
print(tweet)
print("Thanks for the tweet")
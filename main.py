from twython import Twython

with open('C:\\Users\\Admin\\Desktop\\twitter api.txt') as cred:
    cred_file = cred.read().splitlines()

twitter = Twython(app_key=cred_file[1], app_secret=cred_file[4])
tag = "#celebrity"
result = twitter.search(q=tag, tweet_mode="extended")
print(result)

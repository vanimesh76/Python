import tweepy

ckey="HhWUjXBm1NJExWPvHZoW3eoLk"
csecret="tv0fl3w4ZVf1Pr3pswcMCMFn1j7pbkYDtmF1WMQf6F6NsyzF4m"
atoken="2788308300-QACrn5MxOt95ZYwsbNzoGnGn02cyZDHPhYn3R5j"
asecret="X4of0LonjMYaYAXT5aDFBx2hIWI9CMUMLKkWOzZVtZHx4"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

user = api.get_user('twitter')
public_tweets = api.home_timeline()
saveFile=open('twitDB179.txt','a')
for tweet in public_tweets:
    
    
    #print tweet
    try:
        saveFile.write(tweet.text)
        saveFile.write('\n')
        saveFile.write('\n')
        #saveFile.close()
    except BaseException, e:
        print 'failed ondata,',str(e)
    #print tweet.text
saveFile.close()

readfile = open('twitDB179.txt','r')
savefile1 = open('new.txt','a')
for line in readfile:
    tweety = line.split('https')[0]
    savefile1.write(tweety)
    savefile1.write('\n')
savefile1.close()
readfile.close()


print api
print user.followers_count
for friend in user.friends():
   #print friend.screen_name

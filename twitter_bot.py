import tweepy
from tkinter import *

consumer_key = 'CDXHAiHWH3ct6HuqhLvmkyoTa'
consumer_secret = 'CtHMEsVVe2pg7qgOM4X3at5E60zM8AUIrJuAR9pLykKAKEBhE3'
access_token = '1127629771284697089-T0W1yakzn9KFbEZS50y5IwIvmjwNTr'
access_token_secret = 'gTYDtcSjY4APWNZ6viwhOYCb8T0qDNehWETq3cKjkzH2Z'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# User Location
user = api.me()
print(user.name)


root = Tk()
label1 = Label( root, text="Search")
E1 = Entry(root, bd =5)
label2 = Label( root, text="Number of Tweets")
E2 = Entry(root, bd =5)
label3 = Label( root, text="Response")
E3 = Entry(root, bd =5)
label4 = Label( root, text="Reply?")
E4 = Entry(root, bd =5)
label5 = Label( root, text="Retweet?")
E5 = Entry(root, bd =5)
label6 = Label( root, text="Favorite?")
E6 = Entry(root, bd =5)
label7 = Label( root, text="Follow?")
E7 = Entry(root, bd =5)
label8 = Label( root, text="unretweet")
E8 = Entry(root, bd =5)


def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()


def getE4():
    return E4.get()

def getE5():
    return E5.get()

def getE6():
    return E6.get()

def getE7():
    return E7.get()



def mainFunction():
    # Checking the working program
    getE1()
    search = getE1()
    
    getE2()
    numberOfTweets = getE2()
    try:
        numberOfTweets = int(numberOfTweets)
    except ValueError:
      pass 
   
    
    
    getE3()
    phrase = getE3()
    
    getE4()
    reply = getE4()
    
    getE5()
    retweet = getE5()
    
    getE6()
    favorite = getE6()

    getE7()
    follow = getE7()

  

    if reply == "yes":
       for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print ("Replied with " + phrase)
            
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    if favorite == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Favorite
                tweet.favorite()
                print('Favorited the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if follow == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Follow
                tweet.user.follow()
                print('Followed the user')
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break     

    if retweet == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Retweet
                tweet.retweet()
                print(tweet)
                print('Retweeted the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

   

submit = Button(root, text ="Submit", command = mainFunction)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()

submit.pack(side =BOTTOM)
root.mainloop()  





from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey= "4AXdoe6af8pbNdOj2biewWOAW"
csecret= "Emm0Vp6Wwj7fUo0qL5QAc83DZPar8p1HKIZNbIQg290D5SYQpT"
atoken= "758300058450141184-Zj90kbnZiPvFnkJ2azIUNquQfXwaUZQ"
asecret= "7M3RAxETmyUjRw6IkwO6wX7UxMGlDtRf4ddKgrMjjHvXK"
print("\n Welcome to Sentiment Analysis Process on Live Twitter Data \n")
class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)
            
            tweet = ascii(all_data["text"])
            sentiment_value, confidence = s.sentiment(tweet)
            print((tweet, sentiment_value, confidence))
    
            if confidence*100 >= 80:
                output = open("twitter-out.txt", "a")
                
                outputfile = open(fof, "a")
                output.write(sentiment_value)
                outputfile.write(tweet)
                output.write("\n")
                outputfile.write("\n")
                output.close()
                outputfile.close()
            
            return True
        except:
            return True

    def on_error(self, status):
        print (status)
fof = input("\n This process saves your live streaming data offline for user analysis. Name the file where you want to save the data without any extension\n")
fof1=fof
fof += '.txt'
fof1 +='_sentiment.txt'
print("\n All the Streaming data will be stored on your local disk under the name \n",fof)
print("\n The Sentiment for each tweet is stored under another file named as \n",fof1)
search = input("\n Please type the keyword you want to perform the sentiment analysis on \n")
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[search])

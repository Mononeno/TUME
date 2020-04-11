import pandas as pd
import string

#Load data
filename = ""
data = pd.read_csv(filename)

cleaned_tweets = []

#Function to remove emoji
def deEmojify(x):
    return x.encode('ascii', 'ignore').decode('ascii')

#Fuction to clean links, hahstags, mentions, RT-string, punctuation, &-marks
#and emojis from the tweet text
def clean_tweet(x):
    cleaned_tweet = []
    x = deEmojify(x) 
    words = x.split()
    for word in words:
        if not word.startswith('http') and not word.startswith('#') \
                              and not word.startswith('@') \
                              and not word.startswith('RT') \
                              and not word.startswith('&amp'):
                                  word = word.translate\
                                  (str.maketrans('', '', string.punctuation))
                                  cleaned_tweet.append(word) 

    cleaned_tweets.append(" ".join(cleaned_tweet).lower())

#Apply preprocessing
data['text'].apply(lambda tweet : clean_tweet(tweet))
data['cleaned_tweet'] = cleaned_tweets

#Remove duplicate tweets
data = data.drop_duplicates(subset=['cleaned_tweet'])

#Save file
output = ""
data.to_csv(output, index = False)
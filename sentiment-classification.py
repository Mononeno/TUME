import joblib
import pandas as pd
from ttp import ttp as prep

#Decoding of sentiments
def sentiments(labels):
    sentiments = []
    
    for label in labels:
        if label == 0:
            sentiments.append("negative")
        if label == 1:
            sentiments.append("neutral")
        if label == 2:
            sentiments.append("positive")
    return sentiments

filename = ""
model = ""

#Load data and classifier model
data = pd.read_csv(filename)
loaded_model = joblib.load(model)

#Classify data
predictions = loaded_model.predict(data['processed_tweet'])

#Decode classification results
data['sentiment'] = pd.Series(sentiments(predictions))

#Code from the assignment script, props to Aku Hiltunen
parser = prep.Parser()

mentions = {'user': [], 'times mentioned': [], 'positivity': [],\
            'negativity': [], 'neutrality': []}
hashtags = {'hashtag': [], 'times used': [], 'positivity': [],\
            'negativity': [], 'neutrality': []}

for row in data.itertuples():
    tweet = parser.parse(row.text.encode('utf-8').decode('utf-8'))
    sentiment = row.sentiment
    
    for mention in tweet.users:
      ignore = 0
      user_to = mention.lower()

      for index, user in enumerate(mentions['user']):
          if user_to == user:
              mentions['times mentioned'][index] += 1
              if sentiment == 'positive':
                  mentions['positivity'][index] += 1
              elif sentiment == 'negative':
                  mentions['negativity'][index] += 1
              else:
                  mentions['neutrality'][index] += 1
              ignore += 1
              break

      if ignore == 0:
        mentions['user'].append(user_to)
        mentions['times mentioned'].append(1)
        if sentiment == 'positive':
            mentions['positivity'].append(1)
            mentions['negativity'].append(0)
            mentions['neutrality'].append(0)
        elif sentiment == 'negative':
            mentions['positivity'].append(0)
            mentions['negativity'].append(1)
            mentions['neutrality'].append(0)
        else:
            mentions['positivity'].append(0)
            mentions['negativity'].append(0)
            mentions['neutrality'].append(1)
    
    for tag in tweet.tags:
      ignore = 0
      hashtag = tag.lower()
      for index, thing in enumerate(hashtags['hashtag']):
          if hashtag == thing:
              hashtags['times used'][index] += 1
              if sentiment == 'positive':
                  hashtags['positivity'][index] += 1
              elif sentiment == 'negative':
                  hashtags['negativity'][index] += 1
              else:
                  hashtags['neutrality'][index] += 1
              ignore += 1
              break

      if ignore == 0:
          hashtags['hashtag'].append(hashtag)
          hashtags['times used'].append(1)
          if sentiment == 'positive':
              hashtags['positivity'].append(1)
              hashtags['negativity'].append(0)
              hashtags['neutrality'].append(0)
          elif sentiment == 'negative':
              hashtags['positivity'].append(0)
              hashtags['negativity'].append(1)
              hashtags['neutrality'].append(0)
          else:
              hashtags['positivity'].append(0)
              hashtags['negativity'].append(0)
              hashtags['neutrality'].append(1)
              
mentions_df = pd.DataFrame(data=mentions)
hashtags_df = pd.DataFrame(data=hashtags)

analysed_name = "covid-sentiments.csv"
mentions_name = "sentiment-mentions.csv"
hashtags_name = "sentiment-hashtags.csv"

data.to_csv(analysed_name, sep=',', encoding='utf-8')
mentions_df.to_csv(mentions_name, sep=',', encoding='utf-8')
hashtags_df.to_csv(hashtags_name, sep=',', encoding='utf-8')
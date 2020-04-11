from ttp import ttp as prep
import pandas as pd
import joblib

mentions = {'user': [], 'times mentioned': [], 'anger': [], 'sadness': [] \
            , 'fear': [], 'disgust':[],  'guilt':[], 'joy':[], 'shame':[]}
hashtags = {'hashtag': [], 'times used': [], 'anger': [], 'sadness': [] \
            , 'fear': [], 'disgust':[],  'guilt':[], 'joy':[], 'shame':[]}

parser = prep.Parser()

#Function to decode labels to emotions
def emotions(labels):
    emotions = []
    
    for label in labels:
        if label == 0:
            emotions.append("anger")
        if label == 1:
            emotions.append("disgust")
        if label == 2:
            emotions.append("fear")
        if label == 3:
            emotions.append("guilt")
        if label == 4:
            emotions.append("joy")
        if label == 5:
            emotions.append("sadness")
        if label == 6:
            emotions.append("shame")
    return emotions


filename = ""
model = ""

#Load data and classifier model
data = pd.read_csv(filename)
loaded_model = joblib.load(model)

#Classify data
predictions = loaded_model.predict(data['processed_tweet'])

#Decode classification results
data['emotion'] = pd.Series(emotions(predictions))


"""
Code to build emotion related hashtag and mention datasets with the same 
principle as in the script given in the assignment. Props to Aku Hiltunen
"""


for row in data.itertuples():
  tweet = parser.parse(row.text.encode('utf-8').decode('utf-8'))
  user_from = row.from_user.lower()
  sentiment = str(row.emotion)

  for mention in tweet.users:
      ignore = 0
      user_to = mention.lower()
      print(mentions['user'])
      
      for index, user in enumerate(mentions['user']):
          if user_to == user:
              mentions['times mentioned'][index] += 1
              if sentiment == 'anger':
                  mentions['anger'][index] += 1
              if sentiment == 'sadness':
                  mentions['sadness'][index] += 1
              if sentiment == 'fear':
                  mentions['fear'][index] += 1
              if sentiment == 'disgust':
                  mentions['disgust'][index] += 1
              if sentiment == 'guilt':
                  mentions['guilt'][index] += 1
              if sentiment == 'joy':
                  mentions['joy'][index] += 1
              if sentiment == 'shame':
                  mentions['shame'][index] += 1
              ignore += 1
              break

      if ignore == 0:
        mentions['user'].append(user_to)
        mentions['times mentioned'].append(1)
        if sentiment == 'anger':
            mentions['anger'].append(1)
            mentions['sadness'].append(0)
            mentions['shame'].append(0)
            mentions['fear'].append(0)
            mentions['disgust'].append(0)
            mentions['guilt'].append(0)
            mentions['joy'].append(0)
        if sentiment == 'sadness':
            mentions['anger'].append(0)
            mentions['sadness'].append(1)
            mentions['shame'].append(0)
            mentions['fear'].append(0)
            mentions['disgust'].append(0)
            mentions['guilt'].append(0)
            mentions['joy'].append(0)
        if sentiment == 'shame':
            mentions['anger'].append(0)
            mentions['sadness'].append(0)
            mentions['shame'].append(1)
            mentions['fear'].append(0)
            mentions['disgust'].append(0)
            mentions['guilt'].append(0)
            mentions['joy'].append(0)
        if sentiment == 'fear':
            mentions['anger'].append(0)
            mentions['sadness'].append(0)
            mentions['shame'].append(0)
            mentions['fear'].append(1)
            mentions['disgust'].append(0)
            mentions['guilt'].append(0)
            mentions['joy'].append(0)
        if sentiment == 'disgust':
            mentions['anger'].append(0)
            mentions['sadness'].append(0)
            mentions['shame'].append(0)
            mentions['fear'].append(0)
            mentions['disgust'].append(1)
            mentions['guilt'].append(0)
            mentions['joy'].append(0)
        if sentiment == 'guilt':
            mentions['anger'].append(0)
            mentions['sadness'].append(0)
            mentions['shame'].append(0)
            mentions['fear'].append(0)
            mentions['disgust'].append(0)
            mentions['guilt'].append(1)
            mentions['joy'].append(0)
        if sentiment == 'joy':
            mentions['anger'].append(1)
            mentions['sadness'].append(0)
            mentions['shame'].append(0)
            mentions['fear'].append(0)
            mentions['disgust'].append(0)
            mentions['guilt'].append(0)
            mentions['joy'].append(1)

  for tag in tweet.tags:
      ignore = 0
      hashtag = tag.lower()

      for index, thing in enumerate(hashtags['hashtag']):
          if hashtag == thing:
              hashtags['times used'][index] += 1
              if sentiment == 'anger':
                  hashtags['anger'][index] += 1
              if sentiment == 'sadness':
                  hashtags['sadness'][index] += 1
              if sentiment == 'fear':
                  hashtags['fear'][index] += 1
              if sentiment == 'disgust':
                  hashtags['disgust'][index] += 1
              if sentiment == 'guilt':
                  hashtags['guilt'][index] += 1
              if sentiment == 'joy':
                  hashtags['joy'][index] += 1
              if sentiment == 'shame':
                  hashtags['shame'][index] += 1
              ignore += 1
              break

      if ignore == 0:
          hashtags['hashtag'].append(hashtag)
          hashtags['times used'].append(1)
          if sentiment == 'anger':
            hashtags['anger'].append(1)
            hashtags['sadness'].append(0)
            hashtags['shame'].append(0)
            hashtags['fear'].append(0)
            hashtags['disgust'].append(0)
            hashtags['guilt'].append(0)
            hashtags['joy'].append(0)
          if sentiment == 'sadness':
            hashtags['anger'].append(0)
            hashtags['sadness'].append(1)
            hashtags['shame'].append(0)
            hashtags['fear'].append(0)
            hashtags['disgust'].append(0)
            hashtags['guilt'].append(0)
            hashtags['joy'].append(0)
          if sentiment == 'shame':
            hashtags['anger'].append(0)
            hashtags['sadness'].append(0)
            hashtags['shame'].append(1)
            hashtags['fear'].append(0)
            hashtags['disgust'].append(0)
            hashtags['guilt'].append(0)
            hashtags['joy'].append(0)
          if sentiment == 'fear':
            hashtags['anger'].append(0)
            hashtags['sadness'].append(0)
            hashtags['shame'].append(0)
            hashtags['fear'].append(1)
            hashtags['disgust'].append(0)
            hashtags['guilt'].append(0)
            hashtags['joy'].append(0)
          if sentiment == 'disgust':
            hashtags['anger'].append(0)
            hashtags['sadness'].append(0)
            hashtags['shame'].append(0)
            hashtags['fear'].append(0)
            hashtags['disgust'].append(1)
            hashtags['guilt'].append(0)
            hashtags['joy'].append(0)
          if sentiment == 'guilt':
            hashtags['anger'].append(0)
            hashtags['sadness'].append(0)
            hashtags['shame'].append(0)
            hashtags['fear'].append(0)
            hashtags['disgust'].append(0)
            hashtags['guilt'].append(1)
            hashtags['joy'].append(0)
          if sentiment == 'joy':
            hashtags['anger'].append(1)
            hashtags['sadness'].append(0)
            hashtags['shame'].append(0)
            hashtags['fear'].append(0)
            hashtags['disgust'].append(0)
            hashtags['guilt'].append(0)
            hashtags['joy'].append(1)


df2 = pd.DataFrame(data=mentions)
df3 = pd.DataFrame(data=hashtags)

output1 = "covid-emotions.csv"
output2 = "emotion-mentions.csv"
output3 = "emotion-hashtags.csv"

data.to_csv(output1, sep=',', encoding='utf-8')
df2.to_csv(output2, sep=',', encoding='utf-8')
df3.to_csv(output3, sep=',', encoding='utf-8')
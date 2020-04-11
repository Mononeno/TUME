import pandas as pd
from wordcloud import WordCloud, get_single_color_func
import matplotlib.pyplot as plt

#Class for custom group color formation 
class GroupedColorFunc(object):
    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

#Loading of hashtag polarity dataset
polarity_filename = ""
polarity = pd.read_csv(polarity_filename)

#Loading of hashtag emotion dataset
emotion_filename = ""
emotion = pd.read_csv(emotion_filename)

#Emotion wordcloud formation
shame = []
disgust = []
joy = []
sadness = []
fear = []
guilt = []
anger= []

default_color = 'grey'

wc = WordCloud(width=1600, height=800, collocations=False, relative_scaling=0,\
               max_font_size = 100,background_color = 'white', \
               ).generate(' '.join(emotion.hashtag).lower())

#Categorization of hashtags
for item in emotion.itertuples():
     if item.anger != 0:
         anger.append(item.hashtag)
     if item.shame != 0:
         shame.append(item.hashtag)
     if item.disgust != 0:
         disgust.append(item.hashtag)
     if item.joy != 0:
         joy.append(item.hashtag)
     if item.sadness != 0:
         sadness.append(item.hashtag)
     if item.fear != 0:
         fear.append(item.hashtag)
     if item.guilt != 0:
         guilt.append(item.hashtag)

#Colors for classes
color_to_words = {
    'dodgerblue':anger ,
    'blue': disgust,
    'orangered': fear,
    'indigo': guilt,
    'fuchsia':joy,
    'blueviolet':sadness,
    'gold':shame
}

grouped_color_func = GroupedColorFunc(color_to_words, default_color)
wc.recolor(color_func=grouped_color_func)

plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig('emotions-wordcloud.png')

#Negative polarity wordcloud formation
neg_tweets = polarity[polarity.negativity != 0 ]
neg_string = []

for t in neg_tweets.hashtag:
    neg_string.append(t)
neg_string = pd.Series(neg_string).str.cat(sep=' ')

wordcloud = WordCloud(width=1600, height=800, max_font_size=200, \
                      background_color='white').generate(neg_string)

plt.figure(figsize=(12,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("negative_hashtags.png")


#Positive wordcloud formation
pos_tweets = polarity[polarity.positivity != 0]
pos_string = []

for t in pos_tweets.hashtag:
    pos_string.append(t)
pos_string = pd.Series(pos_string).str.cat(sep=' ')
wordcloud = WordCloud(width=1600, height=800, max_font_size=200 \
                      , background_color='white' \
                      , colormap='magma').generate(pos_string)
plt.figure(figsize=(12,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("positive_hashtags.png")
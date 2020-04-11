import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer

#Loading nltk corpuses
nltk.download('words')
nltk.download('stopwords')
nltk.download('wordnet')

#Function for checking if string has numbers
def hasNumbers(inputString):
     return any(char.isdigit() for char in inputString)

#Load data
filename = ""
data = pd.read_csv(filename)

#Load abbrevation textfile
with open('abbrevation.txt') as file:
    abbrevations = dict(line.strip().split('=') for line in file)

#Save corpuses to variables
english_words = set(nltk.corpus.words.words())
english_stopwords = set(nltk.corpus.stopwords.words('english'))

#Initialize tokenizers
wordnet_lemmatizer = WordNetLemmatizer()
tokenizer = TweetTokenizer()

no_abbrevations = []
processed_tweets = []

#Change of abbrevations to sentences and the removal of strings with numbers
for tweet in data['cleaned_tweet']:
    abbrevationeless = []
    numberless = []
    tokens = word_tokenize(str(tweet))
    
    for token in tokens:
        if str(token).upper() in abbrevations.keys():
            abbrevationeless.append(abbrevations[str(token).upper()].lower())
        else:
            abbrevationeless.append(token)
            
    for tkn in abbrevationeless:
        if hasNumbers(tkn):
            pass
        else:
            numberless.append(tkn)
            
    no_abbrevations.append(" ".join(numberless))
  
data['no_abbrevations'] = no_abbrevations
cleaned_tweets = data['no_abbrevations']

#Loop to further process the data via removal of stopwords, non-english words
#and the lemmatization of words
for tweet in cleaned_tweets:
    word_tokens = tokenizer.tokenize(str(tweet))
    word_tokens_lower_english = \
    [t for t in word_tokens if t in english_words or not t.isalpha()]
    word_tokens_no_stops = \
    [t for t in word_tokens_lower_english if not t in english_stopwords]
    word_tokens_no_stops_lemmatized = \
    [wordnet_lemmatizer.lemmatize(t) for t in word_tokens_no_stops]
    if len(word_tokens_no_stops_lemmatized) <=2:
        processed_tweets.append(" ")
    else:
        clean_text = " ".join(word_tokens_no_stops_lemmatized)
        processed_tweets.append(clean_text)
    
data['processed_tweet'] = processed_tweets

#removal of sentences shorter than 3 words
data = data[data['processed_tweet'].apply(lambda x: len(str(x)) > 3)]

output = ""
data.to_csv(output, index=False)

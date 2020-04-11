import pandas as pd
import networkx as nx
import string

#Function to remove punctuation from hashtags
def remove_punc(hash_list):
    no_punc= []
    for word in hash_list:
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = '#' + word
        no_punc.append(word)
    no_punc_lists.append(no_punc)

#Load data
filename = ""
df = pd.read_csv(filename)

no_punc_lists = []

#Collect hashtags
df['hashtags'] = df['text'].map(lambda s: \
  [i  for i in s.split() if i.startswith("#") ])
   
#Remoce punctuation from hashtags
df['hashtags'].apply(lambda word : remove_punc(word))
df['hashtags'] = no_punc_lists

#Search words
search_hashtags = ['#coronavirus', '#covid19', '#covid-19', '#corona', \
                   '#coronavirusoutbreak', '#ncov19', '#covid', '#toiletpaper',\
                   '#toiletpaperapocalypse']

#Initialize graph
network = nx.DiGraph()

#Form edges between hashtags and search words
for hashtags in df.hashtags:
    hashtag_list_keys = []
    hashtag_list_vals = []
    for hashtag in hashtags:
        if hashtag.lower() in search_hashtags:
            hashtag_list_keys.append(hashtag)
        else:
            hashtag_list_vals.append(hashtag)
    for hashtag_ in hashtag_list_keys:
        from_ = hashtag_.lower()
        for item in hashtag_list_vals:
            to_ = item.lower()
            if not network.has_edge(from_,to_):
                network.add_edge(from_,to_,weight=0)
            network[from_][to_]['weight'] += 1

output = ""
nx.readwrite.gexf.write_gexf(network,  output, \
                             encoding='utf-8', version='1.2draft')
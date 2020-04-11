import pandas as pd

# Loading of the data from multiple files to dataframes
data_1 = pd.read_csv("twitter-2013dev-A.txt", sep='\t', \
                     names = ['id','sentiment','text'] )
data_2 = pd.read_csv("twitter-2013test-A.txt", sep='\t', \
                     names = ['id','sentiment','text'])
data_3 = pd.read_csv("twitter-2013train-A.txt", sep='\t', \
                     names = ['id','sentiment','text'])
data_4 = pd.read_csv("twitter-2014sarcasm-A.txt", sep='\t', \
                     names = ['id','sentiment','text'])
data_5 = pd.read_csv("twitter-2014test-A.txt", sep='\t', \
                     names = ['id','sentiment','text'])
data_6 = pd.read_csv("twitter-2015test-A.txt", sep='\t', \
                     names = ['id','sentiment','text'])
data_7 = pd.read_csv("twitter-2015train-A.txt", sep='\t', \
                     names = ['id','sentiment','text'])
data_8 = pd.read_csv("twitter-2016dev-A.txt", sep='\t', \
                     names = ['id','sentiment','text'])
data_9 = pd.read_csv("twitter-2016devtest-A.txt", sep='\t', \
                     names = ['id','sentiment','text'])
data_10 = pd.read_csv("twitter-2016test-A.txt", sep='\t', \
                      names = ['id','sentiment','text','random'])
data_11 = pd.read_csv("twitter-2016train-A.txt", sep='\t', \
                      names = ['id','sentiment','text'])

#Combining dataframes
data = pd.concat([data_1, data_2, data_3, data_4, data_5, data_6, data_7\
                        , data_8, data_9, data_10, data_11], ignore_index=True)

#One file increased the amount of columns -> removal of extra column
data = data.drop(['random'], axis = 1)

data['text'] = data['text'].str.replace(',','')

output = ""
data.to_csv(output, index=False)
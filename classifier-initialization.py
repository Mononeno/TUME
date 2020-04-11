import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing  import LabelEncoder
import pickle


filename =  ""
data = pd.read_csv(filename)

#Encode labels, select either sentiment or emotion
le = LabelEncoder()
le.fit(data['sentiment'])
classes = le.transform(data['sentiment'])
data['classes'] = classes

#Divide the dataset to training and testing, use stratify to balance class dist.
x_train, x_test, y_train, y_test = train_test_split(data['cleaned_tweet'], \
                                                    data['classes'], \
                                                    test_size = 0.33,\
                                                    stratify=data['classes'])

#Create a pipeline for data processing and modeling
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', LinearSVC())])

#Grid search parameters for finding the best parameters for algorithms
tuned_parameters = {
    'vect__ngram_range': [(1, 1), (1, 2), (2, 2)],
    'tfidf__use_idf': (True, False),
    'tfidf__norm': ('l1', 'l2'),
    "clf__penalty": ["l2"],
    "clf__dual":[False,True]
}

#Search best parameters for model and train the model
clf = GridSearchCV(text_clf, tuned_parameters)
clf.fit(x_train, y_train)

#Classify tweets and get a rough estimation of prediction accuracy
predictions = clf.predict(x_test)
np.mean(predictions == y_test)

#save the model to a file for later use
filename = ''
pickle.dump(clf, open(filename, 'wb'))

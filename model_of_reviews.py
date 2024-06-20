# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IhUf_lFRUtwzoTnyyznaVeWoHz7wfnlS

# import libraries
"""

import pandas as pd

import string

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer,PorterStemmer

from nltk import pos_tag

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,classification_report

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')

"""# import the data"""

data= pd.read_csv("Restaurant_Reviews.csv")
data.head(20)

data.shape

data.describe().transpose()

count= data.isnull().sum().sort_values(ascending=False)
percentage= ((data.isnull().sum()/len(data)*100)).sort_values(ascending=False)
missing_data=pd.concat([count,percentage],axis=1,keys=['count,percentage'])
missing_data

"""# Preprocessing"""

def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    # original of the words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # remove stop words
    tokens = [word for word in tokens if word.lower() not in stop_words]
    # Remove punctuation
    tokens = [word for word in tokens if word not in string.punctuation]

    return ' '.join(tokens)

data['Review'] = data['Review'].apply(preprocess_text)

"""# Feature Extraction (Bag of Words)"""

# convert the data to vectors of the word and the number of his appearence
vectorizer = CountVectorizer()

# feature column
x = vectorizer.fit_transform(data['Review'])

# target column
y = data['Liked']

"""# choose model and train it"""

# spilt the data to train and test
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

# train the data by using randomforestclassifier
classifier = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

# prediction
y_pred = classifier.predict(X_test)

"""# evaluate the model"""

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Yes')
recall = recall_score(y_test, y_pred, pos_label='Yes')
f1 = f1_score(y_test, y_pred, pos_label='Yes')
classification_rep = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy*100:.2f} %')
print(f'Precision: {precision*100:.2f} %')
print(f'Recall: {recall*100:.2f} %')
print(f'F1 Score: {f1*100:.2f} %')
print(f'Classification Report:\n{classification_rep}')
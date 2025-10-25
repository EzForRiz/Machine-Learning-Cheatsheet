#Feature hashing, also known as the hash trick, is a method for transforming categorical variables into numerical variables. The idea behind feature hashing is to map each categorical value to a unique integer using a hash function and then use these integers as input features for ML models.

from sklearn.feature_extraction import FeatureHasher
import pandas as pd

# Import data
data = pd.read_csv('data.csv')

# Create the FeatureHasher object
hasher = FeatureHasher(n_features=2, input_type='string')

# Transform the categorical variables into numerical features
features = hasher.fit_transform(data['profession'])

# Print the resulting features
print(features.toarray())



#The CountVectorizer class is a feature extraction method used to convert text data into numerical data. It works by tokenizing the text data and counting the frequency of occurrences of each word or n-gram (a contiguous sequence of n items from a given sample of text) in each document. The resulting matrix, known as the document-term matrix, features rows that represent documents and columns that represent words or n-grams.

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Import data
data = pd.read_csv('data.csv')

# Create the CountVectorizer object
vectorizer = CountVectorizer(
    ngram_range=(1,3),
    stop_words={'english'},
    lowercase=False
    )

# Transform the text data into numerical features
features = vectorizer.fit_transform(data['intro'])

# Print the resulting features
print(features.toarray())




#Before we discuss TfidfVectorizer, let’s first understand Term Frequency-Inverse Document Frequency (TF-IDF). It is a statistical method used to measure the importance of a word in a document or a set of documents. It is commonly used in information retrieval and text mining to rank the relevance of documents based on the presence of keywords.

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# load the data from csv file
data = pd.read_csv("data.csv")

# create the TfidfVectorizer object
tfidf_vectorizer = TfidfVectorizer()

# apply the TfidfVectorizer to the 'intro' column of the data
intro_tfidf = tfidf_vectorizer.fit_transform(data['intro'])

# get the feature names from the vectorizer
feature_names = tfidf_vectorizer.get_feature_names()

# convert the Tf-idf sparse matrix to a dense matrix
intro_tfidf = intro_tfidf.toarray()

# print the Tf-idf features and their corresponding weight
for i, intro in enumerate(data['intro']):
    print("Intro:", intro)
    print("TF-IDF features:")
    for j, feature in enumerate(feature_names):
        print(feature, intro_tfidf[i][j])
    print("\n")




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import json
import random

file_name = './Books_small_10000.json'

class Sentiment:
    
    NEGATIVE = 'Negative'
    NEUTRAL = 'Neutral'
    POSITIVE = 'Positive'

class Review:
    
    def __init__(self, text, score):
        self.text = text
        self.score = score
        self.sentiment = self.get_sentiment()
        
    def get_sentiment(self):
        if self.score <= 2:
            return Sentiment.NEGATIVE
        elif self.score == 3:
            return Sentiment.NEUTRAL
        else:
            return Sentiment.POSITIVE


class ReviewContainer:
    
    def __init__(self, reviews):
        self.reviews = reviews
    
    def get_text(self):
        return [x.text for x in self.reviews]
    
    def get_sentiment(self):
        return [x.sentiment for x in self.reviews]
    
    
    def evenly_distribution(self):
        negative = list(filter(lambda x: x.sentiment == Sentiment.NEGATIVE,
                          self.reviews))
        positive = list(filter(lambda x: x.sentiment == Sentiment.POSITIVE,
                          self.reviews))
        positive_shrunk = positive[:len(negative)]
        self.reviews = negative + positive_shrunk
        random.shuffle(self.reviews)
        
reviews = []
with open(file_name) as f:
    for line in f:
        review = json.loads(line)
        reviews.append(Review(review['reviewText'], review['overall']))
        
        
reviews[5].sentiment


from sklearn.model_selection import train_test_split

training, test = train_test_split(reviews, test_size=0.33, random_state=42)


training_container = ReviewContainer(training)
test_container = ReviewContainer(test)

training_container.evenly_distribution()

xtrain = training_container.get_text()
ytrain = training_container.get_sentiment()

xtest = test_container.get_text()
ytest = test_container.get_sentiment()



from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
xtrain_vectors = vectorizer.fit_transform(xtrain)
xtest_vectors = vectorizer.transform(xtest)


from sklearn.svm import SVC

cl_svm = SVC(kernel='linear')
cl_svm.fit(xtrain_vectors, ytrain)

cl_svm.predict(xtest_vectors[0])

cl_svm.score(xtest_vectors, ytest)

from sklearn.metrics import f1_score

f1_score(ytest, cl_svm.predict(xtest_vectors), average=None,
         labels=[Sentiment.POSITIVE, Sentiment.NEUTRAL, Sentiment.NEGATIVE])
"""
Functions for performing analysis on text.

-All functions should be "pure" i.e. no side effects
-The first argument should be a string containing the text body
-All hyperparameters should be given default parameters corresponding to the most common use case
-Any dependencies introduced for performing these analyses should be restricted to just this module,
 and not found anywhere else in the project
- This module should not depend on anything else in the project, and should work for any arbitrary text
- Make sure to annotate any 'helper' functions with an underscore. If there are too many helpers for one function,
  define a helper class and wrap the class with a function call
"""
from transformers import pipeline
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords

def sentiment(text):
    """
    Performs a sentiment analysis

    :param text: the text we performe sentiment analysis on
    :type text: str
    :return: sentiment_score, a number between -1 to 1, positive number for 
             positive senitment and vice versa. 
    :rtype: float
    """
    sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")
    result = sentiment_analysis('Trump is a racist!')[0]
    if result['label'] == 'NEGATIVE':
        return -result['score']
    else:
        return result['score']

def collocation(text):
    """
    Performs a collocation on text
    :param text: the text to perform collocation analysis on.
    :type text: str
    :return: top10 bigrams
    :rtype: list[tuple]
    """
    # TODO implement collocation
"""
Contains utility functions for preprocessing text
"""
import nltk
import re,string
from nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as nltk_sw
# nltk.download('stopwords')  # can just get this from online and put in a set
nltk.download('punkt')

STOPWORDS = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}


def strip_stopwords(text, stopwords=None,tokenized = True):
    """
    Strips the stopwords from a given text
    :param text: The text to be processed
    :type text: supports str, list of str, ...
    :param stopwords:
    :type stopwords: Optional, iterable: the list of stopwords to be removed.
        if not specified, goes with nltk's stopword
    :return: tokenized text with out stopwords
    :rtype: str, or list, ...
    """
    
    if stopwords is None:
        stopwords = STOPWORDS
      
      
    if isinstance(text,str):
        text_tokens = word_tokenize(text)
        remove_sw = [word for word in text_tokens if not word in stopwords]
        return remove_sw if tokenized else " ".join(remove_sw)

    if isinstance(text,list):
        res = []
        for sent in text:
            text_tokens = word_tokenize(sent)
            remove_sw = [word for word in text_tokens if not word in stopwords]
            if(not tokenized): remove_sw = " ".join(remove_sw)
            res.append(remove_sw)
        return res



def strip_punctuation(text, symbols=None, tokenized = True):
    """
    Strips punctuation from a given text
    :param text: The text to be processed
    :type text:
    :param stopwords:
    :type stopwords: Optional, iterable: the list of symbols to be removed.
        if not specified, goes with some default
    :return:
    :rtype:
    """
    # TODO implement strip_punctuation

    if(isinstance(text,str)):
        stripped = re.sub('[%s]' % string.punctuation,'',text)
        return word_tokenize(stripped) if tokenized else stripped
    if(isinstance(text,list)):
      res = []
      for sent in text:
          stripped = re.sub('[%s]' % string.punctuation,'',sent)
          if(tokenized): stripped = word_tokenize(stripped)
          res.append(stripped)
      return res
    

def preprocess(text,tokenized = True, lower = False):
    '''
    Combines lower, strip punctuation, and strip stop words in one function
    param: text
    type: str, list of str
    return preprocessed text
    '''

    if isinstance(text,str):
        if(lower):text = text.lower()
        stripped = strip_punctuation(text,tokenized=False)
        return strip_stopwords(stripped,tokenized = tokenized)

    if isinstance(text,list):  # maybe we shouldn't bother worrying about this?
      res = []
      for sent in text:
          if(lower): sent = sent.lower()
          stripped = strip_punctuation(sent,tokenized=False)
          stripped = strip_stopwords(stripped,tokenized=tokenized)
          res.append(stripped)
      return res


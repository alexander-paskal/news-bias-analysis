"""
Contains utility functions for preprocessing text
"""
import nltk
import re,string
from nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as nltk_sw
nltk.download('stopwords')
nltk.download('punkt')

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
    
    if(stopwords == None): 
      stopwords = nltk_sw.words('english')
      
      
    if(isinstance(text,str)):
      text_tokens = word_tokenize(text)
      remove_sw = [word for word in text_tokens if not word in stopwords]  
      return remove_sw if tokenized else " ".join(remove_sw)

    if(isinstance(text,list)):
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
    


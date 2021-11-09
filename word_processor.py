import re
import unicodedata
import math
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse.linalg import svds
from ast import literal_eval

from nltk import word_tokenize, sent_tokenize , PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords , wordnet as wn
import nltk



# fucntion =>  remove_non_ascii(words)
# param :
#   1) words : list of words
# return :
#   new_words : list of words ignoring no ascii characters
def remove_non_ascii(words):
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words




#function => to_lowercase(words)
#param :
#   1) 1) words : list of words
# return :
#   new_words : list of words converted to lowercase characters
def to_lowercase(words):
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words



#function => remove_punctuation(words)
#param :
#   1) 1) words : list of words
# return :
#   new_words : list of words with punctions removed
def remove_punctuation(words):
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words



#function => remove_stopwords(words)
#param :
#   1) 1) words : list of words
# return :
#   new_words : list of words with stopwords removed
def remove_stopwords(words):
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words




#function => stem(words)
#param :
#   1) 1) words : list of words
# return :
#   new_words : list of words converted to stem words
def stem(words):
    new_words = []
    ps = PorterStemmer()
    for word in words:
        new_words.append(ps.stem(word))
    return new_words




#function => lemmatize(words)
#param :
#   1) 1) words : list of words
# return :
#   new_words : list of lemmatize words
def lemmatize(words):
    new_words = []
    lemmatizer = WordNetLemmatizer()
    for word in words:
        syn = wn.synsets(word)
        if len(syn) != 0:
            new_words.append(lemmatizer.lemmatize(word, pos = syn[0].pos()))
        else :
            new_words.append(lemmatizer.lemmatize(word))
    return new_words





#function => pre_processing(words)
#param :
#   1) 1) words : list of words
# return :
#   new_words : list of words with all above operations applied
def pre_processing(words):
    words = nltk.word_tokenize(words)
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = remove_stopwords(words)
    words = stem(words)
    words = lemmatize(words)
    return words

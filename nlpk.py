from pythainlp.tokenize import word_tokenize
import requests
r_pos = requests.get('https://raw.githubusercontent.com/PyThaiNLP/lexicon-thai/master/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1/pos.txt')
r_neg = requests.get('https://raw.githubusercontent.com/PyThaiNLP/lexicon-thai/master/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1/neg.txt')
listpos=r_pos.text.split()
listneg=r_neg.text.split()
from nltk import NaiveBayesClassifier as nbc
import codecs
from itertools import chain
pos1=['pos']*len(listpos)
neg1=['neg']*len(listneg)
training_data = list(zip(listpos,pos1)) + list(zip(listneg,neg1))
from nltk import NaiveBayesClassifier as nbc
import codecs
from itertools import chain
pos1=['pos']*len(listpos)
neg1=['neg']*len(listneg)
training_data = list(zip(listpos,pos1)) + list(zip(listneg,neg1))
vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in training_data]))
feature_set = [({i:(i in word_tokenize(sentence.lower())) for i in vocabulary},tag) for sentence, tag in training_data]
classifier = nbc.train(feature_set)
test_sentence ="ดีจัง"
featurized_test_sentence = {i:(i in word_tokenize(test_sentence.lower())) for i in vocabulary}
print("test_sent:",test_sentence)
print("tag:",classifier.classify(featurized_test_sentence))
# -*- coding: utf-8 -*-
import re
import pickle
import numpy as np
import sklearn.metrics as metric
from nltk.stem import PorterStemmer
from matplotlib import pyplot as plt
from sklearn.datasets import load_files
from scipy.spatial.distance import cosine
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Base de dados IMDb
# Bd balanceada, tem tantos comentários positivos como negativos
trainDic = load_files('aclImdb/train/')
testDic = load_files('aclImdb/test/')
print trainDic.keys()
print testDic.keys()
# # Criar um ficheiro pickle com todos os textos de treino e de teste
# new_dict = dict(text_train = trainDic.data, target = trainDic.target)
# pickle.dump(new_dict, open('trainDic.p', 'wb'))
# new_dict = dict(text_test = testDic.data, target = testDic.target)
# pickle.dump(new_dict, open('testDic.p', 'wb'))

## Ficheiro com os textos de treino
## Dimensão do vocabulário todo: 74849
trainDic = pickle.load(open('trainDic.p', 'rb'))
print trainDic.keys()
text_train = trainDic["text_train"]
print text_train[0]
class_train = trainDic["target"]
print class_train

## Ficheiro com os textos de teste
testDic = pickle.load(open('testDic.p', 'rb'))
print testDic.keys()
text_test = testDic["text_test"]
print text_test[0]
class_test = testDic["target"]
print class_test




def plot_confusion(matrix, name, norm):
    plt.matshow(matrix)
    plt.title('Confusion matrix '+str(name))
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig('matriz-confusao'+str(name+"-"+str(norm))+'.png',bbox='tight',transparent=True)
    plt.show()


if __name__ == "__main__":
    print "cenas"

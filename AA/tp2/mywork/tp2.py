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

# # Criar um ficheiro pickle com todos os textos de treino e de teste
new_dict = dict(text_train = trainDic.data, target = trainDic.target)
pickle.dump(new_dict, open('trainDic.p', 'wb'))
new_dict = dict(text_test = testDic.data, target = testDic.target)
pickle.dump(new_dict, open('testDic.p', 'wb'))

## Ficheiro com os textos de treino
## Dimensão do vocabulário todo: 74849
trainDic = pickle.load(open('trainDic.p', 'rb'))
text_train = trainDic["text_train"]
class_train = trainDic["target"]

## Ficheiro com os textos de teste
testDic = pickle.load(open('testDic.p', 'rb'))
text_test = testDic["text_test"]
class_test = testDic["target"]

print 'Tipo de dados: %s' %type(text_train)
print 'Tamanho: %d' %len(text_train)
print 'Número de classes: %d' %len(np.unique(class_train))
print 'Número de +: %d' %np.sum(class_train==1)
print 'Número de -: %d' %np.sum(class_train==0)
print '2ª critíca negativa:%s' %text_train[3]

#limpeza de texto -------------- train ----------------------------------------------
# Retirar a mudança de linha HTML
# text_train = [doc.replace('<br />', ' ') for doc in text_train]

# # Usar uma expressão regular para guardar apenas os caracteres alfabéticos
# text_train = [re.sub(r'[^a-zA-Z]+', ' ', doc) for doc in text_train]

# # Serve para transformar uma palavra na sua raiz, permitindo assim mapear 
# # palavras semelhantes numa única palavra
# stemVocabTrain = text_train
# stemFunc = PorterStemmer()
# for i in range(len(text_train)):
#    vocab = [stemFunc.stem(w) for w in text_train[i].split()]
#    stemVocabTrain[i] =' '.join(vocab)

# #print ENGLISH_STOP_WORDS
# maxFeat = None
# tp = r'\b\w\w\w\w+\b'
# tfidf = TfidfVectorizer(min_df = 5, token_pattern = tp,
#                        stop_words = "english", max_features = maxFeat).fit(stemVocabTrain)
# vocabNew = tfidf.get_feature_names()
# # Sem limite máximo dá: 16989
# print 'Dimensão Vocabulário limpeza: %d' %len(np.unique(vocabNew))

# # Criar um novo pickle para cada dimensão do vocabulário
# new_dict = dict(stemVocab = stemVocabTrain, target = class_train, tfidf = tfidf)
# pickle.dump(new_dict, open('trainDic_' + str(len(vocabNew)) + '.p', 'wb'))

# lempexa textos de teste ----------------------teste ----------------------------
# # Retirar a mudança de linha HTML
# text_test = [doc.replace('<br />', ' ') for doc in text_test]
# # Usar uma expressão regular para guardar apenas os caracteres alfabéticos
# text_test = [re.sub(r'[^a-zA-Z]+', ' ', doc) for doc in text_test]

# # Serve para transformar uma palavra na sua raiz, permitindo assim mapear 
# # palavras semelhantes numa única palavra
# stemVocabTest = text_test
# stemFunc = PorterStemmer()
# for j in range(len(text_test)):
#    vocab = [stemFunc.stem(w) for w in text_test[j].split()]
#    stemVocabTest[j] = ' '.join(vocab)
# print 'Dimensão Vocabulário limpeza: %d' %len(np.unique(vocabNew))

# # Criar um novo pickle para cada dimensão do vocabulário
# new_dictTest = dict(stemVocab = stemVocabTest, target = class_test, tfidf = tfidf)
# pickle.dump(new_dictTest, open('testDic_' + str(len(vocabNew)) + '.p', 'wb'))



def plot_confusion(matrix, name):
    plt.matshow(matrix)
    plt.title('Confusion matrix '+str(name))
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig('matriz-confusao'+str(name)+'.png',bbox='tight',transparent=True)
    plt.show()


if __name__ == "__main__":
    print "cenas"

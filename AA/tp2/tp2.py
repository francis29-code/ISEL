# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:25:12 2016

@author: Pedro Morais
"""
import re
import pickle
import numpy as np
import sklearn.metrics as metric
import plot_confusion_matrix as cnf
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

## Base de dados IMDb
## Bd balanceada, tem tantos comentários positivos como negativos
#trainDic = load_files('aclImdb/train/')
#testDic = load_files('aclImdb/test/')

## Criar um ficheiro pickle com todos os textos de treino e de teste
#new_dict = dict(text_train = trainDic.data, target = trainDic.target)
#pickle.dump(new_dict, open('trainDic.p', 'wb'))
#new_dict = dict(text_test = testDic.data, target = testDic.target)
#pickle.dump(new_dict, open('testDic.p', 'wb'))

## Ficheiro com os textos de treino
## Dimensão do vocabulário todo: 74849
trainDic = pickle.load(open('trainDic.p', 'rb'))
text_train = trainDic["text_train"]
class_train = trainDic["target"]

## Ficheiro com os textos de teste
testDic = pickle.load(open('testDic.p', 'rb'))
text_test = testDic["text_test"]
class_test = testDic["target"]

#print 'Tipo de dados: %s' %type(text_train)
#print 'Tamanho: %d' %len(text_train)
#print 'Número de classes: %d' %len(np.unique(class_train))
#print 'Número de +: %d' %np.sum(class_train==1)
#print 'Número de -: %d' %np.sum(class_train==0)
#print '2ª critíca negativa:%s' %text_train[3]

"""Limpeza do texto"""
"""Limpeza nos textos de treino"""
## Retirar a mudança de linha HTML
#text_train = [doc.replace('<br />', ' ') for doc in text_train]

## Usar uma expressão regular para guardar apenas os caracteres alfabéticos
#text_train = [re.sub(r'[^a-zA-Z]+', ' ', doc) for doc in text_train]

## Serve para transformar uma palavra na sua raiz, permitindo assim mapear 
## palavras semelhantes numa única palavra
#stemVocabTrain = text_train
#stemFunc = PorterStemmer()
#for i in range(len(text_train)):
#    vocab = [stemFunc.stem(w) for w in text_train[i].split()]
#    stemVocabTrain[i] =' '.join(vocab)

##print ENGLISH_STOP_WORDS
#maxFeat = None
#tp = r'\b\w\w\w\w+\b'
#tfidf = TfidfVectorizer(min_df = 5, token_pattern = tp,
#                        stop_words = "english", max_features = maxFeat).fit(stemVocabTrain)
#vocabNew = tfidf.get_feature_names()
## Sem limite máximo dá: 16989
#print 'Dimensão Vocabulário limpeza: %d' %len(np.unique(vocabNew))

## Criar um novo pickle para cada dimensão do vocabulário
#new_dict = dict(stemVocab = stemVocabTrain, target = class_train, tfidf = tfidf)
#pickle.dump(new_dict, open('trainDic_' + str(len(vocabNew)) + '.p', 'wb'))

"""Limpeza nos textos de teste"""
## Retirar a mudança de linha HTML
#text_test = [doc.replace('<br />', ' ') for doc in text_test]
## Usar uma expressão regular para guardar apenas os caracteres alfabéticos
#text_test = [re.sub(r'[^a-zA-Z]+', ' ', doc) for doc in text_test]

## Serve para transformar uma palavra na sua raiz, permitindo assim mapear 
## palavras semelhantes numa única palavra
#stemVocabTest = text_test
#stemFunc = PorterStemmer()
#for j in range(len(text_test)):
#    vocab = [stemFunc.stem(w) for w in text_test[j].split()]
#    stemVocabTest[j] = ' '.join(vocab)
#print 'Dimensão Vocabulário limpeza: %d' %len(np.unique(vocabNew))

## Criar um novo pickle para cada dimensão do vocabulário
#new_dictTest = dict(stemVocab = stemVocabTest, target = class_test, tfidf = tfidf)
#pickle.dump(new_dictTest, open('testDic_' + str(len(vocabNew)) + '.p', 'wb'))

"""Classificação"""
tamanho = 16989
trainDicTrimmed = pickle.load(open('trainDic_' + str(tamanho) + '.p', 'rb'))
testDicTrimmed = pickle.load(open('testDic_' + str(tamanho) + '.p', 'rb'))

stemVocabTrain = trainDicTrimmed['stemVocab']
targetTrain = trainDicTrimmed['target']
stemVocabTest = testDicTrimmed['stemVocab']
targetTest = testDicTrimmed['target']

tfidf = trainDicTrimmed['tfidf']

## Aplicar o tfidf ao texto e transformá-lo em vectores
stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
stemVocabTestTransform = tfidf.transform(stemVocabTest)

"""Discriminante Logístico"""
logreg = LogisticRegression().fit(stemVocabTrainTransform, class_train)
results = logreg.score(stemVocabTestTransform, class_test)
print 'Prob Acertos: %.2f' %(results*100.)

## Matriz de confusão
prediction = logreg.predict(stemVocabTestTransform)
cnf_matrix = confusion_matrix(class_test, prediction)
print "Matriz de confusão: \n", cnf_matrix
## Plot da matriz de confusão
#plt.figure()
#cnf.plot_confusion_matrix(cnf_matrix)
##plt.savefig('img/confusionMatrix' + str(tamanho) + '.png', bbox_inches='tight', transparent=True)

## Recall e Precision neste exemplo são menos importantes porque o nº de exemplos
## de cada tipo tem o mesmo número. Neste caso é mais proveitoso calcular a accuracy

## % dos positivos bem classificados (recall)
tp_rate = metric.recall_score(class_test, prediction)
print 'Recall: %.2f' %(tp_rate*100.)
## % dos negativos mal classificados (false alarm)
fp_rate = cnf_matrix[1][0]*1. / (cnf_matrix[1][0] + cnf_matrix[1][1])
print 'False Alarm: %.2f' %(fp_rate*100.)

## Habilidade do classificador não classificar como positivo uma amostra negativa
precision = metric.precision_score(class_test, prediction)
print 'Precision: %.2f' %(precision*100.)
 
accuracy = metric.accuracy_score(class_test, prediction)
print 'Accuracy: %.2f' %(accuracy*100.)
## The F1 score can be interpreted as a weighted average of the precision and 
## recall, where an F1 score reaches its best value at 1 and worst score at 0.
f_score = metric.f1_score(class_test, prediction)
print 'F-Score: %.2f' %(f_score*100.)

target_names = ['Negativo', 'Positivo']
print(metric.classification_report(class_test, prediction, target_names=target_names))

false_positive_rate, true_positive_rate, thresholds = roc_curve(targetTest, prediction)
roc_auc = auc(false_positive_rate, true_positive_rate)

## Curva ROC
plt.figure()
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'g', label='AUC = %0.2f'% roc_auc)
plt.plot(0.5, .3)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'b--')
plt.xlim([0,1])
plt.ylim([0,1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')

## Grafico para verificar qual o desempenho dos classificadores com diferentes
## dimensões de vocabulário
#size = [1, 1000, 1500, 2000, 3000, 4000, 5000, 10000, 15000, 16989]
#score = [55.25, 85.39, 85.94, 86.41, 86.62, 86.78, 86.85, 86.88, 86.88, 86.92]
#plt.figure()
#plt.plot(size, score)
#plt.grid()
#plt.xlim([1, 16989])
#plt.ylim([55., 88])
#plt.xlabel('Dimensao do vocabulario')
#plt.ylabel('Probabilidade de acertos (%)')
#plt.title('Dimensao do vocabulario vs probabilidade de acertos')
##plt.savefig('img/valorDimensaoVocab.png', bbox_inches='tight', transparent=True)

"""Classificador k-NN"""
## Dá MemoryError - 10.000, 5.000, 2.000, 1.000
## Deixa de dar MemoryError com um tamanho de vocabulário de 650

#vocabSize = 650
#stemVocabTrainTrimmed = stemVocabTrain[:vocabSize]
#targetTrimmed = targetTrain[:vocabSize]
#auxNeg = 0
#auxPos = 0
#aux = 0
#
### Fazer o trimmed dos 25k documentos de modo a não dar MemoryError no kNN
#for i in range(len(stemVocabTrain)):
#    if targetTrain[i] == 0:
#        if auxNeg < (vocabSize / 2.):
#            stemVocabTrainTrimmed[aux] = stemVocabTrain[i]
#            targetTrimmed[aux] = 0
#            auxNeg += 1
#            aux += 1
#        else:
#            pass
#    else:
#        if auxPos < (vocabSize / 2.):
#            stemVocabTrainTrimmed[aux] = stemVocabTrain[i]
#            targetTrimmed[aux] = 1
#            auxPos += 1
#            aux += 1
#        else:
#            pass
#
### Verificar se a divisão ficou bem balanceada
##nC = np.zeros(2)
##for i in range(2):
##    nI = np.sum(targetTrimmed == i)
##    nC[i] = nI
##print nC
#
#stemVocabTrainTrimmedTransform = tfidf.transform(stemVocabTrainTrimmed)
##
#n_neighbor = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 190, 195, 200, 205,
#              210, 215, 220, 230, 240, 250, 300, 400, 500, 600, 650]
#score = []
#for i in range(len(n_neighbor)):
#    kNN = KNeighborsClassifier(n_neighbors = n_neighbor[i], weights ='uniform', metric='euclidean')
#    kNN.fit(stemVocabTrainTrimmedTransform, targetTrimmed)
#
#    results = kNN.score(stemVocabTestTransform, class_test)
#    score.append(results*100.)
##print 'Prob Acertos: %.2f' %(results*100.)
#print np.round(score, 2)

## Não dá para fazer com média nula porque com 25k dá memoryError, mas para a distancia 
## Com média nula
#Xn = (stemVocabTrainTrimmedTransform.T - np.mean(stemVocabTrainTrimmedTransform.toarray(), 1)).T

#n_neighbor = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 210, 220, 
#              230, 240, 250, 300, 400, 500, 600, 650]
#score = []
#for i in range(len(n_neighbor)):
#    kNN = KNeighborsClassifier(n_neighbors = n_neighbor[i], weights ='uniform', metric='euclidean')
#    kNN.fit(Xn, targetTrimmed)
#
#    results = kNN.score(stemVocabTestTransform, class_test)
#    score.append(results*100.)
##print 'Prob Acertos: %.2f' %(results*100.)
#print np.round(score, 2)


## Matriz de confusão
#results = kNN.predict((stemVocabTestTransform))
#cnf_matrix = confusion_matrix(targetTest, results)
#print "Matriz de confusão: \n", cnf_matrix


"""Distância de cosseno"""
#vectorA = [1, 2, 3]
#vectorB = [3, 5, 7]
#distCosseno = cosine(vectorA, vectorB)
#print distCosseno
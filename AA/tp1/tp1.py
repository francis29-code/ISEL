# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 12:13:01 2016

@author: ASUS
"""

import pickle
import sklearn
import numpy as np
import plot_confusion_matrix as cnf
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.datasets import fetch_lfw_people
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

"""Scikit Version"""
#print('The scikit-learn version is {}.'.format(sklearn.__version__))

"""Import database labeled faces in the wild"""
#carasBD = fetch_lfw_people(min_faces_per_person=30, resize=0.75)
## Criar um pickle com todas as imagens
#pickle.dump(carasBD, open('full_lib.p', 'wb'))

"""Criar um ficheiro pickle para guardar pelo menos 50 imagens de cada exemplo"""
#full_lib = pickle.load(open('full_lib.p', 'rb'))
#
#images = full_lib['data']
#tNames = full_lib['target_names']
#target = full_lib['target']

## Contar quantas imagens existem em cada classe
#nC = np.zeros(34)
#for i in range(34):
#    nI = np.sum(target == i)
#    nC[i] = nI

## Criar um array com pelo menos 50 imagens em cada classe
## No total iremos ter 1410 imagens
#arrayImages = images[target == 0]
#for i in range(1, 34):
#    if(len(images[target == i]) < 50):
#        arrayImages = np.vstack((arrayImages,images[target == i]))
#    else:
#        arrayImages = np.vstack((arrayImages, images[target == i][0:50]))

## Cria um array agora com o número final de imagens em cada classe
#nTrimmed = np.zeros(34)
#for i in range(len(nC)):
#    if (nC[i] > 50):
#        nTrimmed[i] = 50
#    else:
#        nTrimmed[i] = nC[i]

## Organizar os targets para corresponderem à imagem da mesma classe
#xArray = np.array([0]*39)
#for i in range(len(nTrimmed)):
#    if i == 0:
#        pass
#    else:
#        xArray = np.hstack((xArray, np.array([i] * nTrimmed[i])))

#plt.figure()
#plt.imshow(np.reshape(arrayImages[0], (93, 70)), cmap="gray", interpolation="none")

## Criação do ficheiro pickle que irá ser utilizado
#new_dict = dict(data=arrayImages, target=xArray, target_names=tNames)
#pickle.dump(new_dict, open('trimmed_lib.p', 'wb'))

""" """
trimmed_lib = pickle.load(open('trimmed_lib.p', 'rb'))

data   = trimmed_lib['data']
target = trimmed_lib['target']
tNames = trimmed_lib['target_names']

## Modificar os valores da escala de cinzento para que estes fiquem compreendidos
## entre [0, 1]
data = data*(255**-1)

"""Projectar e avaliar o desempenho do classificador dos k vizinhos mais próximos (kNN)"""
## Dividir os dados em K folds
## O gerador de números aleatórios é utilizado para se obter sempre a mesma divisão
## Shuffle para baralhar os dados antes de os dividir
kfold = StratifiedKFold(n_splits = 5, shuffle = True, random_state=0)

## Escolha do melhor vizinho
#n_neighbor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 50]
#score = []
#for i in range(len(n_neighbor)):
#    kNN = KNeighborsClassifier(n_neighbors = n_neighbor[i], weights ='uniform')
#
#    ## Estimar qual o desempenho do classificador
#    scoreskNN = cross_val_score(kNN, data, target, cv = kfold)
#    #print "Probabilidade de acertos em cada fold: \n", scoreskNN
#
#    ## Média dos resultados das 5 folds
#    mean_scores = np.sum(scoreskNN)/5.0
#
#    score.append(mean_scores)
## Arredondar a média dos folds a 3 casas décimais
#score = np.round(score, 3)

# Plot dos valor óptimo do número de vizinhos
#plt.figure()
#plt.plot(n_neighbor, score)
#plt.grid()
#plt.xlim([0, 50])
#plt.ylim([0.26, 0.32])
#plt.xlabel('n_neighbors')
#plt.ylabel('scores')
#plt.title('Valor optimo do numero de vizinhos')
#plt.savefig('valorNumerodeVizinhos.png', bbox_inches='tight', transparent=True)

## O número óptimo de vizinhos estimado foi: 1
kNN = KNeighborsClassifier(n_neighbors = 1, weights ='uniform')
# scoreskNN = cross_val_score(kNN, data, target, cv = kfold)
# print "Probabilidade de acertos em cada fold: \n", scoreskNN
#
# mean_scoreskNN = np.sum(scoreskNN) / 5.
# mean_scoreskNN = np.round(mean_scoreskNN, 3)
# print "Média da probabilidade de acertos:", mean_scoreskNN
#
# # Matriz de confusão
# results = cross_val_predict(kNN, data, target, cv = kfold)
# cnf_matrix = confusion_matrix(target, results)
# print "Matriz de confusão: \n", cnf_matrix

## Plot da matriz de confusão
#plt.figure()
#cnf.plot_confusion_matrix(cnf_matrix)

"""Repetir a avaliação do desempenho usando faces processadas com PCA"""
Xn = (data.T - np.mean(data, 1)).T #tirar média

## Escolha do melhor número de componentes
#n_component = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500,
#               600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1409]
#scorePCA = []
#for i in range(len(n_component)):
#    pca = PCA(n_components = n_component[i])
#    ## Estimação do modelo para os dados (1410x6510)
#    pca.fit(Xn)             #Xn matriz de dados
#    ## Projecta dados nas componentes principais
#    Y = pca.transform(Xn)
#
#    ## Estimar qual o desempenho do classificador
#    scoresPCA = cross_val_score(kNN, Y, target, cv = kfold)
#    print "Probabilidade de acertos em cada fold com PCA: \n", scoresPCA
#
#    ## Média dos resultados das 5 folds
#    mean_scoresPCA = np.sum(scoresPCA) / 5.
#    scorePCA.append(mean_scoresPCA)

## Arredondar a média dos folds a 3 casas décimais
#scorePCA = np.round(scorePCA, 3)

## Plot dos valor óptimo do número de componentes
#plt.figure()
#plt.plot(n_component, scorePCA)
#plt.grid()
#plt.xlim([5, 1410])
#plt.ylim([0, 0.4])
#plt.xlabel('n_neighbors')
#plt.ylabel('scores')
#plt.title('Valor optimo do numero de componentes')
#plt.savefig('valorNumeroDeComponentes.png', bbox_inches='tight', transparent=True)

## O número óptimo de componentes principais estimado foi 200
#pca = PCA(n_components = 200) #guardar n_components
#pca.fit(Xn)
#Y = pca.transform(Xn)

#scoresPCA = cross_val_score(kNN, Y, target, cv = kfold)
#print "Probabilidade de acertos em cada fold com PCA: \n", scoresPCA

#mean_scoresPCA = np.sum(scoresPCA) / 5.
#mean_scoresPCA = np.round(mean_scoresPCA, 3)
#print "Média da probabilidade de acertos:", mean_scoresPCA

## Matriz de confusão
#results = cross_val_predict(kNN, Y, target, cv = kfold)
#cnf_matrix = confusion_matrix(target, results)
#print "Matriz de confusão: \n", cnf_matrix

## Plot da matriz de confusão
#plt.figure()
#cnf.plot_confusion_matrix(cnf_matrix)

"""Verificar se normalizar a variância dos dados transformados é benéfico. """
#pca = PCA(n_components = 200, whiten = True)
#pca.fit(Xn)
#Yw = pca.transform(Xn)

## Estimar qual o desempenho do classificador
#scoresPCAWhiten = cross_val_score(kNN, Yw, target, cv = kfold)
#print "Probabilidade de acertos em cada fold com PCA e variância normalizada: \n", scoresPCAWhiten

#mean_scoresPCAWhiten = np.sum(scoresPCAWhiten) / 5.
#mean_scoresPCAWhiten = np.round(mean_scoresPCAWhiten, 3)
#print "Média da probabilidade de acertos:", mean_scoresPCAWhiten

## Matriz de confusão
#results = cross_val_predict(kNN, Yw, target, cv = kfold)
#cnf_matrix = confusion_matrix(target, results)
#print "Matriz de confusão: \n", cnf_matrix

## Plot da matriz de confusão
#plt.figure()
#cnf.plot_confusion_matrix(cnf_matrix)

"""Testar e avaliar outro classificador"""
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(random_state = 0)

pca = PCA(n_components = 200)
pca.fit(Xn)
Ytree = pca.transform(Xn)

## Estimar qual o desempenho do classificador
scoresTreeClass = cross_val_score(clf, Ytree, target, cv = kfold)
#print "Probabilidade de acertos em cada fold com DecisionTreeClassifier: \n", scoresTreeClass

#mean_scoresTreeClass = np.sum(scoresTreeClass) / 5.
#mean_scoresTreeClass = np.round(mean_scoresTreeClass, 3)
#print "Média da probabilidade de acertos:", mean_scoresTreeClass
#
## Matriz de confusão
#results = cross_val_predict(kNN, Ytree, target, cv = kfold)
#cnf_matrix = confusion_matrix(target, results)
#print "Matriz de confusão: \n", cnf_matrix
#
## Plot da matriz de confusão
#plt.figure()
#cnf.plot_confusion_matrix(cnf_matrix)

pca = PCA(n_components = 200, whiten = True)
pca.fit(Xn)
Ywtree = pca.transform(Xn)

## Estimar qual o desempenho do classificador
scoresTreeClassWhiten = cross_val_score(clf, Ywtree, target, cv = kfold)
#print "Probabilidade de acertos em cada fold com DecisionTreeClassifier, variância normalizada: \n", scoresTreeClassWhiten

#mean_scoresTreeClassWhiten = np.sum(scoresTreeClassWhiten) / 5.
#mean_scoresTreeClassWhiten = np.round(mean_scoresTreeClassWhiten, 3)
#print "Média da probabilidade de acertos:", mean_scoresTreeClassWhiten

# Matriz de confusão
#results = cross_val_predict(kNN, Ywtree, target, cv = kfold)
#cnf_matrix = confusion_matrix(target, results)
#print "Matriz de confusão: \n", cnf_matrix

## Plot da matriz de confusão
#plt.figure()
#cnf.plot_confusion_matrix(cnf_matrix)

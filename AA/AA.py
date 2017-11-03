# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:00:26 2017

@author: Vanessa Nunes
"""

import pickle
import numpy as np
import scipy.spatial.distance as spd
import scipy.linalg as la
from sklearn.metrics import confusion_matrix
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sklearn as sk


fD = pickle.load(open("mnist_small.p"))

train9=fD['train7']
train9 = train9[:,:363].astype('float')


def pergA():
    nn = LA.norm(np.mean(train9, axis = 1))
    #DESVIO PADRÃO NÃO FIZEMOS
    #Cx=np.cov(train9)
    #dv = np.sqrt(Cx)
    #dd = np.sqrt(np.mean(abs(train9[:,206] - np.mean(train9[:,206]) )**2))
    return nn

a = pergA()
print 'pergunta a) correta = iii) true', a

def pergB():
    original=np.reshape(train9[:,213],(28,28)) #i) falso
    plt.imshow(255-original, interpolation='none',cmap='gray')

    Cx=np.cov(train9)

    (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios

    v = v.real
    idx=np.argsort(-v)
    v=v[idx]

    W=W[:,idx]
    W=W[:,v>=1e-10]
    W=W.real


    W=W[:,0:1]

    Y=np.dot(W.T,train9)

    Xr=np.dot(W,Y)

    ii=np.reshape(Xr[:,213],(28,28))
    #descomentar a cena de baixo para ver a ii)
    #plt.imshow(255-ii , interpolation='none',cmap='gray')

#pergB()
print 'pergunta b) correta = iv) '

def pergC():
    #SEM CERTEZA
    x1= train9[24]
    x2= train9[62]
    x3= train9[347]
    x4= train9[354]


    x1x2 = np.dot(x1,x2)
    x3x4 = np.dot(x3,x4)

    return x1x2, x3x4


c12, c34 = pergC()
print 'pergunta c) correta = iv) ', 'x1 e x2=', c12,',x3 e x4 =' , c34


def pergD():
    #SEM CERTEZA
    train9=fD['train9'].astype('float')
    x= train9[719]
    y= train9[629]
    cc = np.corrcoef(y,x)
    return cc


cc = pergD()
print 'pergunta d) correta = iv) ', cc


def pergE():
    Cx=np.cov(train9)
    (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios

    v = v.real
    idx=np.argsort(-v)
    v=v[idx]
    x = 0
    for i in range (len(v)):
        if(v[i] == 0.0):
            x+=1

    return x

e = pergE()
print 'pergunta e) correta = i) ', e

def pergF():
    Cx=np.cov(train9)
    (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios

    v = v.real
    idx=np.argsort(-v)
    v=v[idx]
    v=v/np.sum(v)
    L=np.cumsum(v)
    gg = np.sum(L<=0.90)
    return gg

f = pergF()
print 'pergunta f) correta = iv) ', f

def pergG():
    Cx=np.cov(train9)
    (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios
    v = v.real
    idx=np.argsort(-v)
    v=v[idx]
    W=W[:,idx]
    W=W[:,v>=1e-10]
    W=W.real
    return W.shape

g = pergG()
print 'pergunta g) correta = ii) ', g


def pergH():
    Cx=np.cov(train9)
    det = np.linalg.det(Cx)

    return Cx.shape, det

h = pergH()
print 'pergunta h) correta = iii) ', h

def pergI():

    original=np.reshape(train9[:,312],(28,28)) #b) falso
    #plt.imshow(255-original, interpolation='none',cmap='gray')

    Cx=np.cov(train9)

    (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios

    v = v.real
    idx=np.argsort(-v)
    v=v[idx]

    W=W[:,idx]
    W=W[:,v>=1e-10]
    W=W.real


    W=W[:,0:14]

    Y=np.dot(W.T,train9)

    Xr=np.dot(W,Y)

    ii=np.reshape(Xr[:,312],(28,28))
    #plt.imshow(255-ii , interpolation='none',cmap='gray')

    ee = sk.metrics.mean_squared_error(original,ii)
    return ee

i = pergI()
print 'pergunta i) correta = ii) ', i


def pergJ():

    original=np.reshape(train9[:,362],(28,28)) #b) falso
    #plt.imshow(255-original, interpolation='none',cmap='gray')

    Cx=np.cov(train9)

    (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios

    v = v.real
    idx=np.argsort(-v)
    v=v[idx]

    W=W[:,idx]
    W=W[:,v>=1e-10]
    W=W.real


    W=W[:,0:13]

    Y=np.dot(W.T,train9)

    Xr=np.dot(W,Y)


    ii=np.reshape(Xr[:,362],(28,28))
    #plt.imshow(255-ii , interpolation='none',cmap='gray')

    ee = sk.metrics.mean_absolute_error(original, ii)
    return ee

j = pergJ()
print 'pergunta j) correta = iv) ', j

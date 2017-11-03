import pickle
import numpy as np
import scipy.spatial.distance as spd
import scipy.linalg as la
from sklearn.metrics import confusion_matrix
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sklearn as sk

fd = pickle.load(open("mnist_small.p"))

train7 = fd['train7']
train7 = train7[:,:393].astype('float')

def pergA():
    x1=train7[3]
    x2=train7[81]
    x3=train7[212]
    x4=train7[378]

    x1x2 = np.dot(x1,x2)
    x3x4 = np.dot(x3,x4)

    return x1x2,x3x4


a1,a2 = pergA()
print "primeiro: ",a1," segundo: ",a2

#reposta iv) verdade

def pergB():
    original = np.reshape(train7[:,152],(28,28))
    Cx=np.cov(train7)
    (v,W)=np.linalg.eig(Cx)
    v = v.real
    idx=np.argsort(-v)
    v=v[idx]
    W=W[:,0:41]
    Y=np.dot(W.T,train7)
    Xr=np.dot(W,Y)
    ii=np.reshape(Xr[:,152],(28,28))
    ee = sk.metrics.mean_squared_error(original,ii)

    return ee

b = pergB()
print "pergunta b) correta iv)",b

def pergC():
    Cx=np.cov(train7)
    (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios

    v = v.real
    idx=np.argsort(-v)
    v=v[idx]

    return len(v) - np.count_nonzero(v)

c = pergC()
print 'pergunta c) correta = i) ', c

def pergD():
    Cx=np.cov(train7)
    det = np.linalg.det(Cx)

    return Cx.shape, det

D = pergD()
print 'pergunta d) correta = i) ', D

def pergE():
    original=np.reshape(train7[:,207],(28,28)) #i) falso
    # plt.imshow(255-original, interpolation='none',cmap='gray')
    Cx=np.cov(train7)
    (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios
    v = v.real
    idx=np.argsort(-v)
    v=v[idx]
    W=W[:,idx]
    W=W[:,v>=1e-10]
    W=W.real
    W=W[:,0:1]
    Y=np.dot(W.T,train7)
    Xr=np.dot(W,Y)
    ii=np.reshape(Xr[:,207],(28,28))
    # plt.imshow(255-ii, interpolation='none',cmap='gray')

    plt.show()

pergE()
print 'pergunta e) correta = iv) '

def pergF():
        original=np.reshape(train7[:,184],(28,28)) #b) falso
        #plt.imshow(255-original, interpolation='none',cmap='gray')

        Cx=np.cov(train7)

        (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios

        v = v.real
        idx=np.argsort(-v)
        v=v[idx]

        W=W[:,idx]
        W=W[:,v>=1e-10]
        W=W.real


        W=W[:,0:13]

        Y=np.dot(W.T,train7)

        Xr=np.dot(W,Y)


        ii=np.reshape(Xr[:,184],(28,28))
        #plt.imshow(255-ii , interpolation='none',cmap='gray')

        ee = sk.metrics.mean_absolute_error(original, ii)

        return ee

f = pergF()
print 'pergunta f) correta = iii) ', f

def pergG():
    nn = LA.norm(np.mean(train7, axis = 1))
    return nn

g = pergG()
print 'pergunta g) correta = iv) ', g

def pergH():
        Cx=np.cov(train7)
        (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios
        v = v.real
        idx=np.argsort(-v)
        v=v[idx]
        W=W[:,idx]
        W=W[:,v>=1e-10]
        W=W.real
        return W.shape

h = pergH()
print 'pergunta h) correta ii)= ',h

def pergI():
        train9=fd['train7'].astype('float')
        x= train9[719]
        y= train9[629]
        cc = np.corrcoef(y,x)
        return cc

i = pergI()
print 'pergunta I) correta iv)',i


def pergJ():
        Cx=np.cov(train7)
        (v,W)=np.linalg.eig(Cx) #v valores prorpios, w vectores proprios

        v = v.real
        idx=np.argsort(-v)
        v=v[idx]
        v=v/np.sum(v)
        L=np.cumsum(v)
        gg = np.sum(L<=0.95)
        return gg

j = pergJ()
print 'pergunta j) correta = iii) ', j


ficheiro = pickle.load(open('A39286_Ficha3_Respostas.p','rb'))
#a
ficheiro['Q001'][0][0] = 0
ficheiro['Q001'][0][1] = 0
ficheiro['Q001'][0][2] = 0
ficheiro['Q001'][0][3] = 1
#b
ficheiro['Q001'][1][0] = 0
ficheiro['Q001'][1][1] = 0
ficheiro['Q001'][1][2] = 0
ficheiro['Q001'][1][3] = 1
#c
ficheiro['Q001'][2][0] = 1
ficheiro['Q001'][2][1] = 0
ficheiro['Q001'][2][2] = 0
ficheiro['Q001'][2][3] = 0
#d
ficheiro['Q001'][3][0] = 1
ficheiro['Q001'][3][1] = 0
ficheiro['Q001'][3][2] = 0
ficheiro['Q001'][3][3] = 0
#e
ficheiro['Q001'][4][0] = 0
ficheiro['Q001'][4][1] = 0
ficheiro['Q001'][4][2] = 0
ficheiro['Q001'][4][3] = 1
#f
ficheiro['Q001'][5][0] = 0
ficheiro['Q001'][5][1] = 0
ficheiro['Q001'][5][2] = 1
ficheiro['Q001'][5][3] = 0
#g
ficheiro['Q001'][6][0] = 0
ficheiro['Q001'][6][1] = 0
ficheiro['Q001'][6][2] = 0
ficheiro['Q001'][6][3] = 1
#h
ficheiro['Q001'][7][0] = 0
ficheiro['Q001'][7][1] = 1
ficheiro['Q001'][7][2] = 0
ficheiro['Q001'][7][3] = 0
#i
ficheiro['Q001'][8][0] = 0
ficheiro['Q001'][8][1] = 0
ficheiro['Q001'][8][2] = 0
ficheiro['Q001'][8][3] = 1
#j
ficheiro['Q001'][9][0] = 0
ficheiro['Q001'][9][1] = 0
ficheiro['Q001'][9][2] = 1
ficheiro['Q001'][9][3] = 0


pickle.dump(ficheiro,open('A39286_Ficha3_Respostas.p','wb'))

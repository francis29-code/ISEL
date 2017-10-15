import pickle
import numpy as np
import scipy.spatial.distance as scp
import matplotlib.pyplot as plt
import scipy.linalg as la

ficheiro = pickle.load(open('A39286_Ficha1_Respostas.p','rb'))
ficheiro['Q001'][0]=1
ficheiro['Q001'][1]=0
ficheiro['Q001'][2]=0
ficheiro['Q001'][3]=0
ficheiro['Q001'][4]=0
ficheiro['Q001'][5]=0

ficheiro['Q002'][0]=1
ficheiro['Q002'][1]=0
ficheiro['Q002'][2]=1
ficheiro['Q002'][3]=0
ficheiro['Q002'][4]=1
ficheiro['Q002'][5]=0

ficheiro['Q003'][0]=0
ficheiro['Q003'][1]=0
ficheiro['Q003'][2]=0
ficheiro['Q003'][3]=0

ficheiro['Q004'][0]=0
ficheiro['Q004'][1]=0
ficheiro['Q004'][2]=0
ficheiro['Q004'][3]=0

pickle.dump(ficheiro,open('A39286_Ficha1_Respostas.p','wb'))

#ficheiro = pickle.load(open("A39286_Q001_data.p",'rb'))
#myDict = pickle.load(ficheiro)
#ficheiro.close()
#dados = myDict.get('dados')
#trueClass = myDict.get('trueClass')
#
#classe1X = []
#classe1Y = []
#
#classe2X = []
#classe2Y = []
#
#classe3X = []
#classe3Y = []
#
##criacao dos arrays das diferentes classes
#
#for i in range(len(trueClass)):
#    if(trueClass[i] == 0.):
#        classe1X.append(dados[0][i])
#        classe1Y.append(dados[1][i])
#    if(trueClass[i] == 1.):
#        classe2X.append(dados[0][i])
#        classe2Y.append(dados[1][i])
#    if(trueClass[i] == 2.):
#        classe3X.append(dados[0][i])
#        classe3Y.append(dados[1][i])
#
#classe0 = np.array([np.asarray(classe1X),np.asarray(classe1Y)])
#classe1 = np.array([np.asarray(classe2X),np.asarray(classe2Y)])
#classe2 = np.array([np.asarray(classe3X),np.asarray(classe3Y)])
#
##1 - a) matriz de media dos dados
#dados1 = np.mean(dados[0])
#dados2 = np.mean(dados[1])
#
#media = np.mean(ficheiro['dados'],axis=1)
#print media
#
#matrizMedia = np.array([dados1,dados2])
##print matrizMedia
## Resposta: Verdadeiro
#
## b)
##print (1300./3200)*100
## Resposta: Falso
#
#
##c)
##print np.cov(dados)
## resposta: Falso
#
#
##d)
#classe0mediaX = np.mean(classe0[0])
#classe0mediaY = np.mean(classe0[1])
#media0 = np.array([classe0mediaX,classe0mediaY])
#
#classe1mediaX = np.mean(classe1[0])
#classe1mediaY = np.mean(classe1[1])
#media1 = np.array([classe1mediaX,classe1mediaY])
#
#eucl = scp.euclidean(media1,media0)
##print eucl
## Resposta : Falso
#
##e) covariancia da classe 2
##print np.cov(classe2)
## Resposta : Falso
#
##f)
##print media0
## Resposta : Falso
#
#
##2--------------------
##a)
#
#Cx = np.cov(dados,ddof=1)
##print Cx
#
##Resposta : Verdadeiro
#
##b)
#
#mx = np.mean(dados,axis=1)
#xn = (dados.T-mx).T
#Ctmp = xn*xn
#Cx = Ctmp/(dados.shape[1]-1)
#
##print Cx
#
##Resposta : Falso
#
##c)
#Cx = np.cov(dados.T,rowvar=False,ddof=0)
##print Cx
##Resposta : Verdadeiro
#
##d)
#mx = np.mean(dados,axis=0)
#xn = dados - mx
#Ctmp = np.dot(xn,xn.T)
#Cx = Ctmp/(dados.shape[1]-1)
##print Cx
## Resposta : Falso
#
##e)
#mx = np.mean(dados,axis=1)
#xn = dados-mx[:,np.newaxis]
#Ctmp = np.dot(xn,xn.T)
#Cx = Ctmp/(dados.shape[1]-1)
##print Cx
##Resposta : Verdadeiro
#
##f)
#mx = np.mean(dados,axis=0)
#mx = mx
#Ctmp = np.dot(dados,dados.T)/(dados.shape[1]-1)
#Cx = Ctmp-np.dot(mx,mx.T)
##print Cx
## Resposta : Falso

# np.random.seed(0)
# pontos = np.random.rand(2,1e3)
# matrizTranslacao = np.array([[-2.,2.]])
# matrizEscalamento = np.array([[2.,0.],[0.,3.]])
# matrizRotacao = np.array([[np.sqrt(3.)/2.,-0.50],[0.50,np.sqrt(3)/2.]])
#
# pontosy_aux = np.dot(matrizRotacao,matrizEscalamento)
# pontosY = (np.dot(pontosy_aux,pontos).T+matrizTranslacao).T
# print pontosY.shape
# plt.figure(figsize=(7,5))
# plt.plot(pontos[0,:],pontos[1,:],'.g',markersize=4)
# plt.plot(pontosY[0,:],pontosY[1,:],'.b',markersize=4)
# plt.axis('equal')
# plt.axis([-6.,10.,-10.,10.])
# plt.grid
# plt.show()

#tudo Falso


#4 c e d - Falso
# media1 = np.array([[-2.,1.]])
# media2 = np.array([[2.,-1]])
# cov1 = np.array([[2.25,-0.00],[-0.00,2.25]])
# cov2 = np.array([[0.25,0.0],[0.0,0.25]])
#
# A1 = la.sqrtm(cov1)
# A2 = la.sqrtm(cov2)
# X1 = np.dot(A1,np.random.rand(2,1000))+media1.T
# X2 = np.dot(A2,np.random.rand(2,1000))+media2.T
# X = np.hstack((X1,X2))
# plt.plot(X)
# plt.show()

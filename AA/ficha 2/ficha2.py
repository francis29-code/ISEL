import pickle
import numpy as np
import numpy.linalg as la
# from sklearn.neighbors import KNeighborsClassifier as KNC
# from sklearn.neighbors.nearest_centroid import NearestCentroid as NC
#
# ficheiro = pickle.load(open('A39286_Q001_data.p','rb'))
# estClass = ficheiro['estClass']
# trueClass = ficheiro['trueClass']
#
# lengthestclass = len(estClass)
# lengthtrueclass = len(trueClass)
#
# countEst = np.count_nonzero(estClass)
# countTrue = np.count_nonzero(trueClass)
#
# percentagem = ((countEst*1.)/(lengthestclass*1.))*100
# percentagem1 = ((countTrue*1.)/(lengthtrueclass*1.))*100


# print percentagem
# print percentagem1
# print percentagem1 + percentagem
# falso

#### PERGUNTA 3
# filezor = pickle.load(open('A39286_Q003_data.p'))
# dados = filezor['dados']
# tClass = filezor['trueClass']
# print tClass
# m0 = np.mean(tClass)
# print m0
# print estClass
# print trueClass

#respostas
ficheiro = pickle.load(open('A39286_Ficha2_Respostas.p','rb'))

ficheiro['Q001'][0]=1
ficheiro['Q001'][1]=1
ficheiro['Q001'][2]=0
ficheiro['Q001'][3]=1
ficheiro['Q001'][4]=0
ficheiro['Q001'][5]=1

ficheiro['Q002'][0]=0
ficheiro['Q002'][1]=0
ficheiro['Q002'][2]=0
ficheiro['Q002'][3]=1

ficheiro['Q003_A'][0]=1
ficheiro['Q003_A'][1]=1
ficheiro['Q003_A'][2]=0
ficheiro['Q003_A'][3]=1

ficheiro['Q003_B'][0]=0
ficheiro['Q003_B'][1]=0
ficheiro['Q003_B'][2]=1
ficheiro['Q003_B'][3]=0

ficheiro['Q004'][0]=1
ficheiro['Q004'][1]=1
ficheiro['Q004'][2]=0
ficheiro['Q004'][3]=0


pickle.dump(ficheiro,open('A39286_Ficha2_Respostas.p','wb'))

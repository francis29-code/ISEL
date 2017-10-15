import pickle
import numpy as np
import numpy.linalg as la
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.neighbors.nearest_centroid import NearestCentroid as NC

ficheiro = pickle.load(open('A39286_Q001_data.p','rb'))
estClass = ficheiro['estClass']
trueClass = ficheiro['trueClass']

lengthestclass = len(estClass)
lengthtrueclass = len(trueClass)

countEst = np.count_nonzero(estClass)
countTrue = np.count_nonzero(trueClass)

percentagem = ((countEst*1.)/(lengthestclass*1.))*100
percentagem1 = ((countTrue*1.)/(lengthtrueclass*1.))*100


print percentagem
print percentagem1
print percentagem1 + percentagem
# falso

# print estClass
# print trueClass

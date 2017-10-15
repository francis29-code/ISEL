# -*- coding: latin-1 -*-
import numpy as np
from matplotlib import pyplot as plt
import numpy.linalg as la
from mpl_toolkits.mplot3d import Axes3D
from mkgrid2d import *
plt.close('all')
#matriz de transformação
cnts=1./np.sqrt(2.);A=np.array([[cnts/3,cnts],[-cnts/3,cnts]])
#cov + média
S=np.dot(A,A.T);SI=la.inv(S);m=np.array([3,2])
#criar grelha
G=mkgrid2d(np.arange(0.5,5.5,.1),np.arange(-0.5,4.5,.1))
#tirar média
Gn=(G.T-m).T
px=1./(2*np.pi*np.sqrt(la.det(S)))*np.exp(-1./2*np.sum(Gn*np.dot(SI,Gn),0))
#criar  pontos
N=500;np.random.seed(0)
X=np.random.randn(2,N)
Y=(np.dot(A,X).T+m).T
f1=plt.figure(figsize=(7,5)) #criar figura
ax=f1.add_subplot(111,projection='3d')
ax.plot(G[0,:],G[1,:],px,'b',linewidth=.5,alpha=.3)
ax.axis('scaled');ax.axis('tight');plt.grid()
plt.plot(Y[0,:],Y[1,:],'.k')

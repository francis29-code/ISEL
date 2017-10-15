# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:30:01 2017

@author: Hugo Safara
"""

import numpy as np
from matplotlib import pyplot as plt


N=1e3;
np.random.seed(0);
X=np.random.rand(2,N)

matriz_rotacao= np.array([[np.sqrt(3.)/2.,-0.5],[0.5,np.sqrt(3.)/2.]])
matriz_escalamento = np.array([[3.,0.],[0.,5.]])
matriz_translacao = np.array([[-1.,-2.]])


y= np.dot(matriz_rotacao,matriz_escalamento)


y_final = (np.dot(y,X).T+matriz_translacao).T

plt.figure(figsize=(7,5)) #criar figura
plt.plot(X[0,:],X[1,:],'.g',markersize=4)
plt.plot(y_final[0,:],y_final[1,:],'.b',markersize=4)
plt.axis('equal')
plt.axis([-6.,10.,-10.,10.])
plt.grid()
plt.show()

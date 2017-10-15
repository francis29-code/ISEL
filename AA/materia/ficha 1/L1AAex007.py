# -*- coding: latin-1 -*-
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle
plt.close('all')

#importar pontos
Parm=pickle.load(open('L1AAestrela.p','rb'))
pts1=Parm[0]
pts2=Parm[1]
pts3=Parm[2]
pts3=Parm[3]
pts3=Parm[4]
allPts3=Parm[5]
#matriz de transformação y=Ax+b
#S=np.array([[1,0],[0,np.sqrt(2.0)]])
#a=np.pi/4
#T=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
#A=np.dot(T,S)
#S=np.dot(A,A.T);SI=np.linalg.inv(S);b=np.array([3,2])#cov + média

A=np.array([[1,-0.5],[1,0.5]])
x=np.array([[-1,1,1,-1,-1],[-1,-1,1,1,-1]])
#b=np.array([[np.sqrt(2)],[0]])
b=np.array([[3.5],[0.5]])
y=np.dot(A,x)
z=y+b
plt.figure(figsize=(6,3.75)) #criar figura
plt.plot(x[0,:],x[1,:],'k',linewidth=1)
plt.fill(x[0,:],x[1,:],color=[.6,.6,.6])
#plt.plot(y[0,:],y[1,:],'k',linewidth=1)
#plt.fill(y[0,:],y[1,:],color=[.8,.6,.6])
plt.plot(z[0,:],z[1,:],'k',linewidth=1)
plt.fill(z[0,:],z[1,:],color=[.6,.6,.8])
plt.axis('scaled')
plt.grid('on')
plt.axis([-2,6.,-1.,2.5])
plt.xlabel('$x_1$',fontsize=16)
plt.xticks(np.arange(-2,6.1))
plt.ylabel('$x_2$',fontsize=16)
plt.yticks(np.arange(-2,2.1))
#ax.set_zlabel('$\mathcal{N}(\mu,\Sigma)$',fontsize=16)
#plt.savefig('../figs/L1AAex005.png',\
#bbox_inches='tight',transparent=True) #guardar em ficheiro ".png"

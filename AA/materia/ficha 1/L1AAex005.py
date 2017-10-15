# -*- coding: latin-1 -*-
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#matriz de transformação y=Ax+b
cnts=1./np.sqrt(2.);A=np.array([[cnts/3,cnts],[-cnts/3,cnts]])
S=np.dot(A,A.T);SI=np.linalg.inv(S);b=np.array([3,2])#cov + média
#criar grelha com função meshgrid (matrizes NxM)
Xg,Yg=np.meshgrid(np.arange(0.5,5.5,.1),np.arange(-0.5,4.5,.1))
#coverter matrizes NxM numa só matriz D de 2x(NxM) e tirar media
xg=Xg.flatten();yg=Yg.flatten();D=np.vstack((xg,yg))
D=(D.T-b.T).T #tirar média
zg=1./(2*np.pi*np.sqrt(np.linalg.det(S)))\
*np.exp(-1./2*np.sum(D*np.dot(SI,D),0))#Calcular densidade
Zg=np.reshape(zg,(Xg.shape[0],Xg.shape[1]))
x=(np.dot(A,np.random.randn(2,1000)).T+b).T#criar pontos
f1=plt.figure(figsize=(7,5)) #criar figura
ax=f1.add_subplot(111,projection='3d') #3D
ax.plot_wireframe(Xg,Yg,Zg,alpha=.3)
ax.contour(Xg,Yg,Zg,10,offset=Zg.min()) 
plt.plot(x[0,:],x[1,:],'.k',markersize=3)
plt.axis([.5,5.5,-0.5,4.5]);ax.elev=30;ax.azim=-110
ax.set_xlabel('$x_1$',fontsize=16);ax.set_ylabel('$x_2$',fontsize=16)
ax.set_zlabel('$\mathcal{N}(\mu,\Sigma)$',fontsize=16)
plt.savefig('../figs/L1AAex005.png',\
bbox_inches='tight',transparent=True) #guardar em ficheiro ".png"

# -*- coding: latin-1 -*-
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
#visualizar fun��o f(x,y)=sin(x+x*y)*sin(y+x*y)/(x+x*y)/x
#criar grelha com fun��o meshgrid
X,Y=np.meshgrid(np.linspace(-5,5.,50),np.linspace(-3,3.,50))
#X e Y arrays bi-dimensionais de 50x50
Z=np.sin(X+X*Y)*np.sin(Y+X*Y)/(Y+X*Y)/X
f1=plt.figure() #criar figura
ax=f1.add_subplot(111,projection='3d') #3D
ax.plot_wireframe(X,Y,Z,alpha=.3)
ax.contour(X,Y,Z,25,offset=Z.min()) #25=n� contornos
ax.elev=20   #posi��o da c�mera:eleva��o
ax.azim=-150 #posi��o da c�mera:azimute (em graus)
ax.set_xlabel('$x$',fontsize=16)
ax.set_ylabel('$y$',fontsize=16)
ax.set_zlabel('$f(x,y)$',fontsize=16)
plt.savefig('../figs/T1AAex004a.png') #guardar em ficheiro ".png"

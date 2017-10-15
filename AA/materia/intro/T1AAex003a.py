# -*- coding: latin-1 -*-
import numpy as np
from matplotlib import pyplot as plt
#desenhar a fun��o sinc(x)
x=np.linspace(-5,5,1000) #1000pts equi-espa�ados entre [-5,5]
fx=np.sin(np.pi*x)/(np.pi*x) #fx � a fun��o "sinc(x)"
plt.plot(x,fx,lw=1)
plt.axis([-5,5,-0.25,1.1])   #eixos 
plt.grid()                   #grelha
plt.xticks(np.arange(-5,6))  #intervalos no x = 1
plt.yticks(np.arange(-.25,1.25,.25))  #intervalos no y = 1/4
plt.text(.5,.75,r'$f(x)=\frac{\sin(\pi x)}{\pi x}$',fontsize=16)
plt.savefig('../figs/T1AAex003a.png') #guardar  em ficheiro ".png"
                                  #(na directoria "../figs/")
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
#myu = 1
u =1
#lambda = 3
lamb = 3

x = rd.wald(u,lamb,100000) # myu = 1 - lambda = 3
hx, b = np.histogram(x,np.linspace(0,5,201),density=True)

b = (b[:-1]+b[1:])/2.0
t = np.linspace(0+1e-6,5,1000)
fx = np.sqrt(lamb/ (2*np.pi*t**3))*np.exp(-lamb*(t-u)**2/(2*(u**2)*t)) #myu ignoravel visto ser 1
plt.figure(figsize=(8,4))
plt.bar(b,hx,width=0.025,color=[.2,.3,.5])
plt.plot(t,fx,'r',linewidth=2)
plt.axis([0,5,0,1.1])
plt.show()

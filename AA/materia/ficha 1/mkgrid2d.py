# -*- coding: latin-1 -*-
#função para fazer grelha a duas dimensões
# G=mkgrid2d(xgrid,ygrid)
# Entradas: xgrid e ygrid 
# arrays com os espaçamentos desejados no x e y
# Saídas: G -> array de 2xN
# N é nº total de pontos na grelha 
# Exemplo:
# g1=np.arange(-1.,1.25,.25)
# g2=np.arange(-2.,2.5,.5)
# G=mkgrid2d(g1,g2)
import numpy as np
def mkgrid2d(xGrid,yGrid):
    X,Y=np.meshgrid(xGrid,yGrid)
    c=len(xGrid)
    r=len(yGrid)
    Xt=X.copy()
    for i in np.arange(0,r,2):
        Xt[i,:]=Xt[i,np.arange(c-1,-1,-1)]  
    
    
    x1=Xt.flatten()
    x2=X.T.flatten()
    x=np.hstack((x2,x1))

    Yt=Y.copy()
    for i in np.arange(1,c,2):
        Y[:,i]=Y[np.arange(r-1,-1,-1),i]
    
    y1=Y.T.flatten()
    y2=Yt.flatten()
    y=np.hstack((y1,y2))

    G=np.vstack((x,y))
    #print G.shape
    return G


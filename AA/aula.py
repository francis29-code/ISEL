import pickle
import numpy as np
import matplotlib.pyplot as plt

ficheiro = pickle.load(open('C:\Users\Denga\Desktop\ISEL\AA\ficha 2\estudo'))

train3 = ficheiro['train3']
I3_8 = np.reshape(train3[:,7],(28,28))
plt.imshow(255-I3_8, interpolation='none',cmap='gray')

I3_m = np.mean(train3,l)

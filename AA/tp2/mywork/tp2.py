
import re
import pickle
import numpy as np
import sklearn.metrics as metric
from nltk.stem import PorterStemmer
from matplotlib import pyplot as plt
from sklearn.datasets import load_files
from scipy.spatial.distance import cosine
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS



def plot_confusion(matrix, name, norm):
    plt.matshow(matrix)
    plt.title('Confusion matrix '+str(name))
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig('matriz-confusao'+str(name+"-"+str(norm))+'.png',bbox='tight',transparent=True)
    plt.show()

import pickle
import sklearn
import numpy as np
import itertools
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.datasets import fetch_lfw_people
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# np.set_printoptions(threshold=np.nan)

def readPickle(file):
    return pickle.load(open(file, 'rb'))

def normalizeImages():
    #somente para a normalizacao das imagens
    full_lib = readPickle('faces_lib.p')
    images = full_lib['data']
    names = full_lib['target_names']
    classes = full_lib['target']

    newClasses = np.asarray([np.sum(classes==i) for i in range(len(classes))])
    newClasses = np.asarray(filter(lambda x: x!=0, newClasses))

    arrayImages = images[classes==0]
    for i in range(1,len(newClasses)):
        if(len(images[classes ==i]) < 50):
            arrayImages = np.vstack((arrayImages,images[classes==i]))
        else:
            arrayImages = np.vstack((arrayImages, images[classes==i][0:50]))

    for i in range(len(newClasses)):
        if(newClasses[i]>50):
            newClasses[i]=50

    #de forma a ser possivel o vstack
    #indicamos que a primera class tem 39 imagens, valores obtidos na analise
    #logo vao existir 39 indices com zeros
    #de forma a corresponderem com as imagens
    array = np.array([0]*newClasses[0])
    for i in range(len(newClasses)):
        if i != 0:
            array = np.hstack((array,np.array([i]*newClasses[i])))

    final_lib = dict(images = arrayImages, classes = array, target_names = names)

    pickle.dump(final_lib, open('final_images_lib.p','wb'))

def neighbors_experiment(full_lib):
    images = full_lib['images']
    classes = full_lib['classes']
    names = full_lib['target_names']

    kfold = StratifiedKFold(n_splits=3,shuffle=True,random_state=0)

    n_tests_neighbors = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,70,90,100]
    final_scores = []
    for i in range(len(n_tests_neighbors)):
        kNN = KNeighborsClassifier(n_neighbors=n_tests_neighbors[i], weights='uniform')
        kNN_values = cross_val_score(kNN,images,classes,cv = kfold)
        final_scores.append(np.sum(kNN_values)/3.0)

    minimum_value = min(final_scores)-0.10
    maximum_value = max(final_scores)+0.10
    plt.figure()
    plt.plot(n_tests_neighbors,final_scores)
    plt.grid()
    plt.ylim([minimum_value,maximum_value])
    plt.xlim([0,max(n_tests_neighbors)])
    plt.xlabel('Numero Vizinhos')
    plt.ylabel('Valores da media')
    plt.title('Valores do numeros de vizinhos')
    plt.savefig('valoresdosvizinhos.png',bboxes='tight',transparent=True)
    plt.show()

def confusion_of_neighbor(full_lib,neighbor):
    images = full_lib['images']
    classes = full_lib['classes']
    names = full_lib['target_names']
    #7 vizinhos melhor valor
    kfold = StratifiedKFold(n_splits=3,shuffle=True,random_state=0)
    kNN = KNeighborsClassifier(n_neighbors=neighbor, weights='uniform')
    kNN_score = cross_val_score(kNN,images,classes,cv = kfold)
    print "media: " +str(np.sum(kNN_score)/3.0)
    kNN_predict = cross_val_predict(kNN,images,classes,cv = kfold)
    matrix = confusion_matrix(kNN_predict,classes)
    plot_confusion(matrix,'kNN')

def pca_experiment(full_lib):
    images = full_lib['images']
    classes = full_lib['classes']
    names = full_lib['target_names']

    kfold = StratifiedKFold(n_splits=3,shuffle=True,random_state=0)
    kNN = KNeighborsClassifier(n_neighbors=1, weights='uniform')

    n_components = [10,20,30,40,50,60,70,80,90,100,200,300,400,500]
    final_score = []
    mean_images = (images.T - np.mean(images,1)).T
    for i in range(len(n_components)):
        pca = PCA(n_components = n_components[i])
        #modelo de dados
        pca.fit(mean_images)
        result = pca.transform(mean_images)
        pca_score = cross_val_score(kNN,result,classes,cv = kfold)
        print "Probabilidade Acertar: " + str(np.sum(pca_score)/3.0)
        final_score.append(np.sum(pca_score)/3.0)

    plt.figure()
    plt.plot(n_components,final_score)
    plt.grid()
    plt.xlim([5,510])
    plt.ylim([0,0.4])
    plt.xlabel('Numero Componentes')
    plt.ylabel('Valores Media')
    plt.title('Valores dos Componentes')
    plt.savefig('valoresdoscomponentes.png',bbox='tight',transparent=True)
    plt.show()

def confusion_pca(full_lib,components,w=False):
    images = full_lib['images']
    classes = full_lib['classes']
    names = full_lib['target_names']

    kfold = StratifiedKFold(n_splits=3,shuffle=True,random_state=0)
    kNN = KNeighborsClassifier(n_neighbors=1, weights='uniform')

    mean_images = (images.T - np.mean(images,1)).T
    pca = PCA(n_components=components,whiten=w)
    pca.fit(mean_images)
    result = pca.transform(mean_images)
    pca_scores = cross_val_score(kNN,result,classes,cv=kfold)
    print "media com pca: " + str(np.sum(pca_scores)/3.0)
    predict = cross_val_predict(kNN,result,classes,cv=kfold)
    matrix = confusion_matrix(classes,predict)
    plot_confusion(matrix,'PCA',w)


def other_classifier(full_lib,components,w=False):
    images = full_lib['images']
    classes = full_lib['classes']
    names = full_lib['target_names']

    mean_images = (images.T - np.mean(images,1)).T
    kfold = StratifiedKFold(n_splits=3,shuffle=True,random_state=0)
    kNN = KNeighborsClassifier(n_neighbors=1, weights='uniform')

    qc = QuadraticDiscriminantAnalysis(priors=None, reg_param=0.0,
                              store_covariance=False,
                              store_covariances=None, tol=0.0001)
    pca = PCA(n_components=components,whiten=w)
    pca.fit(mean_images)
    result=pca.transform(mean_images)
    scores=cross_val_score(qc,result,classes,cv=kfold)
    print "media: " + str(np.sum(scores)/3.0)
    results = cross_val_predict(qc,result,classes,cv=kfold)
    matrix = confusion_matrix(classes,results)
    plot_confusion(matrix,'QUAD',w)

def faces_classifier_test(full_lib):
    images = full_lib['images']
    classes = full_lib['classes']
    names = full_lib['target_names']
    n_samples = images.shape[0]
    # for machine learning we use the 2 data directly (as relative pixel
    # positions info is ignored by this model)
    n_classes = names.shape[0]
    x_train, x_test,y_train,y_test = train_test_split(images,classes,test_size=0.25,random_state=0)
    pca = PCA(n_components = 200,whiten=True).fit(x_train)
    x_train_pca = pca.transform(x_train)
    x_test_pca = pca.transform(x_test)
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
    clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
    clf = clf.fit(x_train_pca, y_train)
    y_pred = clf.predict(x_test_pca)
    #precision - classificacoes positivas corretas
    #recall - positivos classificados corretamente
    #f-score - media harmonica entre precisoon e recall
    #support - numero de ocorrencias no y_test
    print(classification_report(y_test, y_pred, target_names=names))
    print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))

def plot_confusion(matrix, name, norm):
    plt.matshow(matrix)
    plt.title('Confusion matrix '+str(name))
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig('matriz-confusao'+str(name+"-"+str(norm))+'.png',bbox='tight',transparent=True)
    plt.show()

def classifier_performance():
    full_lib = readPickle('final_images_lib.p')
    # neighbors_experiment(full_lib)
    # confusion_of_neighbor(full_lib,1)
    # pca_experiment(full_lib)
    # confusion_pca(full_lib,200)
    # confusion_pca(full_lib,200,True)
    # other_classifier(full_lib,200)
    # other_classifier(full_lib,200,True)
    faces_classifier_test(full_lib)



def main():
    # normalizeImages()
    classifier_performance()



if __name__ == "__main__":

    main()

# -*- coding: utf-8 -*-
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
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model
from sklearn.model_selection import cross_val_predict


def plot_confusion(matrix, name,condition):
    plt.matshow(matrix)
    plt.title(name)
    plt.colorbar()
    if(condition):
        plt.xticks(range(8),['1','2','3','4','7','8','9','10'], rotation='horizontal')
        plt.yticks(range(8),['1','2','3','4','7','8','9','10'], rotation='horizontal')
    plt.ylabel('Predicted')
    plt.xlabel('True class')
    plt.savefig(str(name)+'.png', bbox='tight', transparent=True)
    plt.show()

def data_to_pickle():
    # Base de dados IMDb
    # Bd balanceada, tem tantos comentários positivos como negativos
    trainDic = load_files('aclImdb/train/')
    testDic = load_files('aclImdb/test/')

    # # Criar um ficheiro pickle com todos os textos de treino e de teste
    new_dict = dict(text_train = trainDic.data, target = trainDic.target)
    pickle.dump(new_dict, open('trainDic.p', 'wb'))
    new_dict = dict(text_test = testDic.data, target = testDic.target)
    pickle.dump(new_dict, open('testDic.p', 'wb'))

def limpeza_dos_pickles():
    ## Ficheiro com os textos de treino
    trainDic = pickle.load(open('trainDic.p', 'rb'))
    text_train = trainDic["text_train"]
    class_train = trainDic["target"]

    ## Ficheiro com os textos de teste
    testDic = pickle.load(open('testDic.p', 'rb'))
    text_test = testDic["text_test"]
    class_test = testDic["target"]

    #-------------- train ----------------------------------------------
    # Retirar a mudança de linha HTML
    text_train = [doc.replace('<br />', ' ') for doc in text_train]

    # # Usar uma expressão regular para guardar apenas os caracteres alfabéticos
    text_train = [re.sub(r'[^a-zA-Z]+', ' ', doc) for doc in text_train]

    # # Serve para transformar uma palavra na sua raiz, permitindo assim mapear 
    # # palavras semelhantes numa única palavra
    stemVocabTrain = text_train
    stemFunc = PorterStemmer()
    for i in range(len(text_train)):
       vocab = [stemFunc.stem(w) for w in text_train[i].split()]
       stemVocabTrain[i] =' '.join(vocab)

    # #print ENGLISH_STOP_WORDS
    maxFeat = None
    tp = r'\b\w\w\w\w+\b'
    tfidf = TfidfVectorizer(min_df = 5, token_pattern = tp,
                           stop_words = "english", max_features = maxFeat).fit(stemVocabTrain)
    vocabNew = tfidf.get_feature_names()
    # # Sem limite máximo dá: 16989
    print 'Dimensão Vocabulário limpeza: %d' %len(np.unique(vocabNew))

    # # Criar um novo pickle para cada dimensão do vocabulário
    new_dict = dict(stemVocab = stemVocabTrain, target = class_train, tfidf = tfidf)
    pickle.dump(new_dict, open('trainDic_' + str(len(vocabNew)) + '.p', 'wb'))

    #-------------------------------- teste ---------------------------------
    # Retirar a mudança de linha HTML
    text_test = [doc.replace('<br />', ' ') for doc in text_test]
    # Usar uma expressão regular para guardar apenas os caracteres alfabéticos
    text_test = [re.sub(r'[^a-zA-Z]+', ' ', doc) for doc in text_test]

    # Serve para transformar uma palavra na sua raiz, permitindo assim mapear 
    # palavras semelhantes numa única palavra
    stemVocabTest = text_test
    stemFunc = PorterStemmer()
    for j in range(len(text_test)):
       vocab = [stemFunc.stem(w) for w in text_test[j].split()]
       stemVocabTest[j] = ' '.join(vocab)
    print 'Dimensão Vocabulário limpeza: %d' %len(np.unique(vocabNew))

    # Criar um novo pickle para cada dimensão do vocabulário
    new_dictTest = dict(stemVocab = stemVocabTest, target = class_test, tfidf = tfidf)
    pickle.dump(new_dictTest, open('testDic_' + str(len(vocabNew)) + '.p', 'wb'))


def limpeza_dos_pickles_sem_stem():
    ## Ficheiro com os textos de treino
    trainDic = pickle.load(open('trainDic.p', 'rb'))
    text_train = trainDic["text_train"]
    class_train = trainDic["target"]

    ## Ficheiro com os textos de teste
    testDic = pickle.load(open('testDic.p', 'rb'))
    text_test = testDic["text_test"]
    class_test = testDic["target"]

    #-------------- train ----------------------------------------------
    # Retirar a mudança de linha HTML
    text_train = [doc.replace('<br />', ' ') for doc in text_train]

    # # Usar uma expressão regular para guardar apenas os caracteres alfabéticos
    text_train = [re.sub(r'[^a-zA-Z]+', ' ', doc) for doc in text_train]

    # # Serve para transformar uma palavra na sua raiz, permitindo assim mapear 
    # # palavras semelhantes numa única palavra
    stemVocabTrain = text_train
    # stemFunc = PorterStemmer()
    # for i in range(len(text_train)):
    #    vocab = [stemFunc.stem(w) for w in text_train[i].split()]
    #    stemVocabTrain[i] =' '.join(vocab)

    # #print ENGLISH_STOP_WORDS
    maxFeat = None
    tp = r'\b\w\w\w\w+\b'
    tfidf = TfidfVectorizer(min_df = 5, token_pattern = tp,
                           stop_words = "english", max_features = maxFeat).fit(stemVocabTrain)
    vocabNew = tfidf.get_feature_names()
    # # Sem limite máximo dá: 16989
    print 'Dimensão Vocabulário limpeza: %d' %len(np.unique(vocabNew))

    # # Criar um novo pickle para cada dimensão do vocabulário
    new_dict = dict(stemVocab = stemVocabTrain, target = class_train, tfidf = tfidf)
    pickle.dump(new_dict, open('trainDic_sem_stem' + str(len(vocabNew)) + '.p', 'wb'))

    #-------------------------------- teste ---------------------------------
    # Retirar a mudança de linha HTML
    text_test = [doc.replace('<br />', ' ') for doc in text_test]
    # Usar uma expressão regular para guardar apenas os caracteres alfabéticos
    text_test = [re.sub(r'[^a-zA-Z]+', ' ', doc) for doc in text_test]

    # Serve para transformar uma palavra na sua raiz, permitindo assim mapear 
    # palavras semelhantes numa única palavra
    stemVocabTest = text_test
    # stemFunc = PorterStemmer()
    # for j in range(len(text_test)):
    #    vocab = [stemFunc.stem(w) for w in text_test[j].split()]
    #    stemVocabTest[j] = ' '.join(vocab)
    print 'Dimensão Vocabulário limpeza: %d' %len(np.unique(vocabNew))

    # Criar um novo pickle para cada dimensão do vocabulário
    new_dictTest = dict(stemVocab = stemVocabTest, target = class_test, tfidf = tfidf)
    pickle.dump(new_dictTest, open('testDic_sem_stem' + str(len(vocabNew)) + '.p', 'wb'))

def classificar_binario():
    #----------------- classificação -----------------------------
     ## Ficheiro com os textos de treino
    trainDic = pickle.load(open('trainDic.p', 'rb'))
    text_train = trainDic["text_train"]
    class_train = trainDic["target"]

    ## Ficheiro com os textos de teste
    testDic = pickle.load(open('testDic.p', 'rb'))
    text_test = testDic["text_test"]
    class_test = testDic["target"]

    tamanho = 16988
    trainDicTrimmed = pickle.load(open('trainDic_' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    """Discriminante Logístico"""
    logreg = LogisticRegression().fit(stemVocabTrainTransform, class_train)
    results = logreg.score(stemVocabTestTransform, class_test)
    print 'Prob Acertos: %.2f' %(results*100.)

    ## Matriz de confusão
    prediction = logreg.predict(stemVocabTestTransform)
    cnf_matrix = confusion_matrix(class_test, prediction)
    print "Matriz de confusão: \n", cnf_matrix
    plot_confusion(cnf_matrix, "Confusion Binary LogisticRegression",False)

def classificar_binario_sem_stem():
    #----------------- classificação -----------------------------
     ## Ficheiro com os textos de treino
    trainDic = pickle.load(open('trainDic.p', 'rb'))
    text_train = trainDic["text_train"]
    class_train = trainDic["target"]

    ## Ficheiro com os textos de teste
    testDic = pickle.load(open('testDic.p', 'rb'))
    text_test = testDic["text_test"]
    class_test = testDic["target"]

    tamanho = 25626
    trainDicTrimmed = pickle.load(open('trainDic_sem_stem' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_sem_stem' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    """Discriminante Logístico"""
    logreg = LogisticRegression().fit(stemVocabTrainTransform, class_train)
    results = logreg.score(stemVocabTestTransform, class_test)
    print 'Prob Acertos: %.2f' %(results*100.)

    ## Matriz de confusão
    prediction = logreg.predict(stemVocabTestTransform)
    cnf_matrix = confusion_matrix(class_test, prediction)
    print "Matriz de confusão: \n", cnf_matrix
    plot_confusion(cnf_matrix, "Confusion Binary LogisticRegression sem stem",False)

def multi_class_to_pickle():
    trainDic = load_files('aclImdb/train/')
    testDic = load_files('aclImdb/test/')

    print "size train files: {0}".format(len(trainDic.filenames))
    print "size test files: {0}".format(len(testDic.filenames))
    train_multi_class = [int(rate.split('_')[1].split('.')[0]) for rate in trainDic.filenames]
    test_multi_class = [int(rate.split('_')[1].split('.')[0]) for rate in testDic.filenames]
    new_dict_multi_class = dict(train = train_multi_class, test = test_multi_class)
    pickle.dump(new_dict_multi_class, open('multiclass.p', 'wb'))

def classificar_multi_classe():
    multi_class = pickle.load(open('multiclass.p','rb'))
    test = multi_class['test']
    train = multi_class['train']

    tamanho = 16988
    trainDicTrimmed = pickle.load(open('trainDic_' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    """Discriminante Logístico"""
    logreg = LogisticRegression().fit(stemVocabTrainTransform, train)
    results = logreg.score(stemVocabTestTransform, test)
    print 'Prob Acertos: %.2f' %(results*100.)

    ## Matriz de confusão
    prediction = logreg.predict(stemVocabTestTransform)
    cnf_matrix = confusion_matrix(test, prediction)
    print "Matriz de confusão: \n", cnf_matrix
    plot_confusion(cnf_matrix, "Confusion Multi Class LogisticRegression",True)

def classificar_multi_classe_sem_stem():
    multi_class = pickle.load(open('multiclass.p','rb'))
    test = multi_class['test']
    train = multi_class['train']

    tamanho = 25626
    trainDicTrimmed = pickle.load(open('trainDic_sem_stem' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_sem_stem' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    """Discriminante Logístico"""
    logreg = LogisticRegression().fit(stemVocabTrainTransform, train)
    results = logreg.score(stemVocabTestTransform, test)
    print 'Prob Acertos: %.2f' %(results*100.)

    ## Matriz de confusão
    prediction = logreg.predict(stemVocabTestTransform)
    cnf_matrix = confusion_matrix(test, prediction)
    print "Matriz de confusão: \n", cnf_matrix
    plot_confusion(cnf_matrix, "Confusion Multi Class LogisticRegression sem stem",True)

def dtc_classificador_binario():
     ## Ficheiro com os textos de treino
    trainDic = pickle.load(open('trainDic.p', 'rb'))
    text_train = trainDic["text_train"]
    class_train = trainDic["target"]

    ## Ficheiro com os textos de teste
    testDic = pickle.load(open('testDic.p', 'rb'))
    text_test = testDic["text_test"]
    class_test = testDic["target"]

    tamanho = 16988
    trainDicTrimmed = pickle.load(open('trainDic_' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)
    """Discriminante Logístico"""
    dt_classifier = DecisionTreeClassifier(random_state=0).fit(stemVocabTrainTransform, class_train)
    results = dt_classifier.score(stemVocabTestTransform, class_test)
    print 'Prob Acertos: %.2f' %(results*100.)

    ## Matriz de confusão
    prediction = dt_classifier.predict(stemVocabTestTransform)
    cnf_matrix = confusion_matrix(class_test, prediction)
    print "Matriz de confusão: \n", cnf_matrix
    plot_confusion(cnf_matrix, "Confusion Binary DecisionTree",False)

def dtc_classificador_binario_sem_stem():
     ## Ficheiro com os textos de treino
    trainDic = pickle.load(open('trainDic.p', 'rb'))
    text_train = trainDic["text_train"]
    class_train = trainDic["target"]

    ## Ficheiro com os textos de teste
    testDic = pickle.load(open('testDic.p', 'rb'))
    text_test = testDic["text_test"]
    class_test = testDic["target"]

    tamanho = 25626
    trainDicTrimmed = pickle.load(open('trainDic_sem_stem' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_sem_stem' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)
    """Discriminante Logístico"""
    dt_classifier = DecisionTreeClassifier(random_state=0).fit(stemVocabTrainTransform, class_train)
    results = dt_classifier.score(stemVocabTestTransform, class_test)
    print 'Prob Acertos: %.2f' %(results*100.)

    ## Matriz de confusão
    prediction = dt_classifier.predict(stemVocabTestTransform)
    cnf_matrix = confusion_matrix(class_test, prediction)
    print "Matriz de confusão: \n", cnf_matrix
    plot_confusion(cnf_matrix, "Confusion Binary DecisionTree sem stem",False)

def dtc_classificador_multi_classe():
    multi_class = pickle.load(open('multiclass.p','rb'))
    test = multi_class['test']
    train = multi_class['train']

    tamanho = 16988
    trainDicTrimmed = pickle.load(open('trainDic_' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    """Discriminante Logístico"""
    dt_classifier = DecisionTreeClassifier(random_state=0).fit(stemVocabTrainTransform, train)
    results = dt_classifier.score(stemVocabTestTransform, test)
    print 'Prob Acertos: %.2f' %(results*100.)

    ## Matriz de confusão
    prediction = dt_classifier.predict(stemVocabTestTransform)
    cnf_matrix = confusion_matrix(test, prediction)
    print "Matriz de confusão: \n", cnf_matrix
    plot_confusion(cnf_matrix, "Confusion Multi Class DecisionTree",True)

def dtc_classificador_multi_classe_sem_stem():
    multi_class = pickle.load(open('multiclass.p','rb'))
    test = multi_class['test']
    train = multi_class['train']

    tamanho = 25626
    trainDicTrimmed = pickle.load(open('trainDic_sem_stem' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_sem_stem' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    """Discriminante Logístico"""
    dt_classifier = DecisionTreeClassifier(random_state=0).fit(stemVocabTrainTransform, train)
    results = dt_classifier.score(stemVocabTestTransform, test)
    print 'Prob Acertos: %.2f' %(results*100.)

    ## Matriz de confusão
    prediction = dt_classifier.predict(stemVocabTestTransform)
    cnf_matrix = confusion_matrix(test, prediction)
    print "Matriz de confusão: \n", cnf_matrix
    plot_confusion(cnf_matrix, "Confusion Multi Class DecisionTree sem stem",True)

def regressao_linear_binaria():
    ## Ficheiro com os textos de treino
    trainDic = pickle.load(open('trainDic.p', 'rb'))
    text_train = trainDic["text_train"]
    class_train = trainDic["target"]

    ## Ficheiro com os textos de teste
    testDic = pickle.load(open('testDic.p', 'rb'))
    text_test = testDic["text_test"]
    class_test = testDic["target"]

    tamanho = 16988
    trainDicTrimmed = pickle.load(open('trainDic_' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    regr = linear_model.LinearRegression()
    regr.fit(stemVocabTrainTransform,class_train)
    results = regr.score(stemVocabTestTransform, class_test)
    print 'Prob Acertos: %.2f' %(results*100.)
    prediction = regr.predict(stemVocabTestTransform)
    plt.figure()
    plt.title('Regressao Linear Binaria')
    plt.scatter(class_test, prediction, color='black')
    plt.scatter([0,1],[0,1],color='red')
    plt.ylabel('Predicted')
    plt.xlabel('True class')   
    plt.savefig('regressao_binaria.png', bbox='tight', transparent=False)
    plt.show()

def regressao_linear_binaria_sem_stem():
    ## Ficheiro com os textos de treino
    trainDic = pickle.load(open('trainDic.p', 'rb'))
    text_train = trainDic["text_train"]
    class_train = trainDic["target"]

    ## Ficheiro com os textos de teste
    testDic = pickle.load(open('testDic.p', 'rb'))
    text_test = testDic["text_test"]
    class_test = testDic["target"]

    tamanho = 25626
    trainDicTrimmed = pickle.load(open('trainDic_sem_stem' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_sem_stem' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    regr = linear_model.LinearRegression()
    regr.fit(stemVocabTrainTransform,class_train)
    results = regr.score(stemVocabTestTransform, class_test)
    print 'Prob Acertos: %.2f' %(results*100.)
    prediction = regr.predict(stemVocabTestTransform)
    plt.figure()
    plt.title('Regressao Linear Binaria sem stem')
    plt.scatter(class_test, prediction, color='black')
    plt.scatter([0,1],[0,1],color='red')
    plt.ylabel('Predicted')
    plt.xlabel('True class')   
    plt.savefig('regressao_binaria_sem_stem.png', bbox='tight', transparent=False)
    plt.show()

def regressao_linear_multi_class():
    multi_class = pickle.load(open('multiclass.p','rb'))
    test = multi_class['test']
    train = multi_class['train']

    tamanho = 16988
    trainDicTrimmed = pickle.load(open('trainDic_' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    regr = linear_model.LinearRegression()
    regr.fit(stemVocabTrainTransform,train)
    results = regr.score(stemVocabTestTransform, test)
    print 'Prob Acertos: %.2f' %(results*100.)
    prediction = regr.predict(stemVocabTestTransform)
    plt.figure()
    plt.title('Regressao Linear Multi Class')
    plt.scatter(test, prediction, color='black')
    plt.xticks(range(11),['0','1','2','3','4','5','6','7','8','9','10'], rotation='horizontal')
    plt.scatter([1,2,3,4,7,8,9,10],[1,2,3,4,7,8,9,10],color='red')
    plt.savefig('regressao_multi_class.png', bbox='tight', transparent=False)
    plt.ylabel('Predicted')
    plt.xlabel('True class')        
    plt.show()

def regressao_linear_multi_class_sem_stem():
    multi_class = pickle.load(open('multiclass.p','rb'))
    test = multi_class['test']
    train = multi_class['train']

    tamanho = 25626
    trainDicTrimmed = pickle.load(open('trainDic_sem_stem' + str(tamanho) + '.p', 'rb'))
    testDicTrimmed = pickle.load(open('testDic_sem_stem' + str(tamanho) + '.p', 'rb'))

    stemVocabTrain = trainDicTrimmed['stemVocab']
    targetTrain = trainDicTrimmed['target']
    stemVocabTest = testDicTrimmed['stemVocab']
    targetTest = testDicTrimmed['target']

    tfidf = trainDicTrimmed['tfidf']

    ## Aplicar o tfidf ao texto e transformá-lo em vectores
    stemVocabTrainTransform = tfidf.transform(stemVocabTrain)
    stemVocabTestTransform = tfidf.transform(stemVocabTest)

    regr = linear_model.LinearRegression()
    regr.fit(stemVocabTrainTransform,train)
    results = regr.score(stemVocabTestTransform, test)
    print 'Prob Acertos: %.2f' %(results*100.)
    prediction = regr.predict(stemVocabTestTransform)
    plt.figure()
    plt.title('Regressao Linear Multi Class')
    plt.scatter(test, prediction, color='black')
    plt.xticks(range(11),['0','1','2','3','4','5','6','7','8','9','10'], rotation='horizontal')
    plt.scatter([1,2,3,4,7,8,9,10],[1,2,3,4,7,8,9,10],color='red')
    plt.savefig('regressao_multi_class.png', bbox='tight', transparent=False)
    plt.ylabel('Predicted')
    plt.xlabel('True class')        
    plt.show()

if __name__ == "__main__":
    # data_to_pickle()
    # limpeza_dos_pickles()
    # classificar_binario()
    # multi_class_to_pickle()
    # classificar_multi_classe()
    # dtc_classificador_binario()
    # dtc_classificador_multi_classe()
    # regressao_linear_binaria()
    # regressao_linear_multi_class()

    # limpeza_dos_pickles_sem_stem()
    # classificar_binario_sem_stem()
    # classificar_multi_classe_sem_stem()
    # dtc_classificador_binario_sem_stem()
    # dtc_classificador_multi_classe_sem_stem()

    # regressao_linear_binaria_sem_stem()
    # regressao_linear_multi_class_sem_stem()


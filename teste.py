"""
Modos de leitura de arquivos:
- "r" é de leitura
- "w" é de escrita
- "a" é de escrita, mas começa um arquivo em branco e apaga se já existir
"""
from sklearn.svm import LinearSVC
import numpy as np 
from sklearn.datasets import make_classification

#from sklearn import svm, tree
from sklearn.svm import SVC
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
#from sklearn.ensemble import RandomForestClassifier
#from sklearn import tree

def predictSVM_RH():
    
    fileh = open("features/rh.txt", "r")
    
    conteudo = fileh.readlines()
    
    fileh.close()
    
    # Agora que vocês sabem que a variável "conteúdo" é um vetor,
    # faça um laço de repetição para mostrar na tela os nomes do arquivo
    
    # Controla o ID da pessoa
    pessoa = 1
    # Quantas amostras das 5 serão utilizadas no treinamento
    amostras_treino = 3
    # Conta as amostras de cada pessoa
    cont = 1
    
    # Vetor para treinamento do modelo e rótulos
    train_feat = []
    # Criação das labens (rótulos/classes) para o classificador
    train_label = []
    
    ''' Será usado para o classificador '''
    # Vetor para teste de predict
    test_feat = []
    # Criação das labens (rótulos/classes) para o classificador
    test_label = []
    
    for linha in range(len(conteudo)):
    
        # A cada 5 amostras troca-se a pessoa
        if linha > 0 and linha % 5 == 0:
            pessoa += 1
            cont = 1
    
        # Usa no treinamento se o cont for até a quantidade de amostras para treino
        if cont <= amostras_treino:
            train_feat.append(conteudo[linha].split())
            train_label.append(str(pessoa))
        # Se não, joga a amostra para o conjunto de teste
        else:
            test_feat.append(conteudo[linha].split())
            test_label.append(str(pessoa))
        # Conta mais uma amostra para a próxima rodada do for
        cont += 1    
        
        
    fileTextFeat = open("features/train_featRH.txt", "w")
    linhas = len(train_feat)
    colunas = len(train_feat[0])
    
    cont_feat = 0
    classe = 0
    for i in range(linhas):
        if i > 0 and i % 3 == 0:
            classe += 1
            cont = 0
        if cont_feat < amostras_treino:
            fileTextFeat.write(str(classe)+" ")
            cont += 1
            for j in range(colunas):
                fileTextFeat.write(str(j)+":"+str(train_feat[i][j])+" ")
        if(i < linhas):
          fileTextFeat.write("\n")
    fileTextFeat.close()
        
    C_range = np.logspace(-5, 9, 10)
    gamma_range = np.logspace(-9, 3, 5)

    param_grid = dict(kernel=['rbf'], gamma=gamma_range, C=C_range)

    clf = GridSearchCV(SVC(probability=True), param_grid)
  #clf = svm.SVC(kernel='rbf', probability=True)

  # Treina o modelo com os vetores de características e o rótulo (classe/identificador) de cada um
    clf.fit(train_feat, train_label)

  # Classifica cada amostra do seguinte vetor
    predict = clf.predict_proba(test_feat)
    predict_labels = clf.predict(test_feat)

    
  # Ele retorna a label que acha que é para cada uma das imagens
    #print("Predict: ", predict)
    #fileLabel = open("labels/label_")
  #  print("Rotulos de treino: ", train_label)
    print("Rotulos de teste: ", test_label)
    print("Predict RH: ", predict_labels)
    print("The best parameters with RH are %s with a score of %0.2f"
        % (clf.best_params_, clf.best_score_))
    
    fileLabelRH = open("labels/predict_RH.txt","w")

    for i in range(len(predict_labels)):
        #if(predict_labels[i] == test_label[i]):
        fileLabelRH.write(str(predict_labels[i]+"\n"))
    fileLabelRH.close()
    
    return predict

  #print()
  #print("Número de acertos: ", acertos)
  #print("Porcentagem de acerto: ", ((acertos/len(predict))#*100))
  
def predictSVM_LBP():
    
    fileh = open("features/lbp.txt", "r")
    
    conteudo = fileh.readlines()
    
    fileh.close()
    
    # Agora que vocês sabem que a variável "conteúdo" é um vetor,
    # faça um laço de repetição para mostrar na tela os nomes do arquivo
    
    # Controla o ID da pessoa
    pessoa = 1
    # Quantas amostras das 5 serão utilizadas no treinamento
    amostras_treino = 3
    # Conta as amostras de cada pessoa
    cont = 1
    
    # Vetor para treinamento do modelo e rótulos
    train_feat = []
    # Criação das labens (rótulos/classes) para o classificador
    train_label = []
    
    ''' Será usado para o classificador '''
    # Vetor para teste de predict
    test_feat = []
    # Criação das labens (rótulos/classes) para o classificador
    test_label = []
    
    for linha in range(len(conteudo)):
    
        # A cada 5 amostras troca-se a pessoa
        if linha > 0 and linha % 5 == 0:
            pessoa += 1
            cont = 1
    
        # Usa no treinamento se o cont for até a quantidade de amostras para treino
        if cont <= amostras_treino:
            train_feat.append(conteudo[linha].split())
            train_label.append("{:02d}".format(pessoa))
        # Se não, joga a amostra para o conjunto de teste
        else:
            test_feat.append(conteudo[linha].split())
            test_label.append("{:02d}".format(pessoa))
        # Conta mais uma amostra para a próxima rodada do for
        cont += 1    

    fileTextFeat = open("features/train_featLBP.txt", "w")
    linhas = len(train_feat)
    colunas = len(train_feat[0])
    
    cont_feat = 0
    classe = 0
    for i in range(linhas):
        if i > 0 and i % 3 == 0:
            classe += 1
            cont = 0
        if cont_feat < amostras_treino:
            fileTextFeat.write(str(classe)+" ")
            cont += 1
            for j in range(colunas):
                fileTextFeat.write(str(j)+":"+str(train_feat[i][j])+" ")
        if(i < linhas):
          fileTextFeat.write("\n")
    fileTextFeat.close()

    '''
    Apenas para teste
    '''    
    fileLabel = open("labels/labelSVM.txt","w")
    fileTrainLabel = open("labels/labelTrain.txt","w")
    
    for i in range(len(test_label)):
#        if i < 10:
#            fileLabel.write(str("0"+test_label[i])+"\n")
#        else:
#            fileLabel.write(str(test_label[i])+"\n")
        fileLabel.write(str(test_label[i])+"\n")
        fileTrainLabel.write(str(test_feat[i])+"\n")
    
    fileLabel.close()
    fileTrainLabel.close()


    C_range = np.logspace(-5, 9, 10)
    gamma_range = np.logspace(-9, 3, 5)
    param_grid = dict(kernel=['rbf'], gamma=gamma_range, C=C_range)

   # train_feat, train_label = make_classification(n_features=4, random_state=0)
   # clf = LinearSVC(random_state=0, tol=1e-5)
   # clf = LinearSVC(random_state=0, tol=1e-5)
    clf = GridSearchCV(SVC(probability=True), param_grid)

    # Treina o modelo com os vetores de características e o rótulo (classe/identificador) de cada um
    clf.fit(train_feat, train_label)

    # Gera as labels que ele acha que é
    # predict = clf.predict(test_feat)
    # print("Labels que o SVM acha que é:", predict)
    
    # Gera a taxa de acerto
    # predict = clf.score(test_feat, test_label)
    # print("Taxa de acerto (acurácia):", predict)
    
    # Gera a matriz de probabilidades
    
    #predict = clf.decision_function(test_feat)
    #print("Matriz de probabilidades:\n", predict[0])
    
    # gets a dictionary of {'class_name': probability}
    #prob_per_class_dictionary = dict(zip(clf.classes_, predict[0]))
    #print("Prob por classe:\n", prob_per_class_dictionary)

    # gets a list of ['most_probable_class', 'second_most_probable_class', ..., 'least_class']
    #results_ordered_by_probability = map(lambda x: x[0], sorted(zip(clf.classes_, predict[0]), key=lambda x: x[1], reverse=True))
    #print("\nProb por classe (ordenado):\n", results_ordered_by_probability)

    predict = clf.predict_proba(test_feat)
    predict_labels = clf.predict(test_feat)
    
    
    print("Rotulos de teste: ", test_label)
    print("Predict RH: ", predict_labels)
    print("The best parameters with LBP are %s with a score of %0.2f"
        % (clf.best_params_, clf.best_score_))
       
    fileLabelLBP = open("labels/predict_LBP.txt","w")
    
    for i in range(len(predict_labels)):
        #if(predict_labels[i] == test_label[i]):
        fileLabelLBP.write(str(predict_labels[i]+"\n"))
    fileLabelLBP.close()
    
    
    return predict
    
  
def gerarArquivoSVM_LBP():
    
    fileSVM = open("predicts/predictSVM_LBP.txt","w")

    conteudoSVM = predictSVM_LBP()
    linhas = len(conteudoSVM)
    colunas = len(conteudoSVM[0])
    
    print(colunas)
    print(conteudoSVM)
    
    cont = 0
    amostra_teste = 2
    classe = 0
    for i in range(linhas):
        if i > 0 and i % 2 == 0:
            classe += 1
            cont = 0
        if cont < amostra_teste:
            fileSVM.write(str(classe)+" ")
            cont += 1
            for j in range(colunas):
                fileSVM.write(str(j)+":"+str(conteudoSVM[i][j])+" ")
        if(i < linhas):
          fileSVM.write("\n")
    fileSVM.close()
    
def gerarArquivoSVM_RH():
    
    fileSVM = open("predicts/predictSVM_RH.txt","w")

    conteudoSVM = predictSVM_RH()
    linhas = len(conteudoSVM)
    colunas = len(conteudoSVM[0])
    
    print(colunas)
    print(conteudoSVM)
    cont = 0
    amostra_teste = 2
    classe = 0
    for i in range(linhas):
        if i > 0 and i % 2 == 0:
            classe += 1
            cont = 0
        if cont < amostra_teste:
            fileSVM.write(str(classe)+" ")
            cont += 1
            for j in range(colunas):
                fileSVM.write(str(j)+":"+str(conteudoSVM[i][j])+" ")
        if(i < linhas):
          fileSVM.write("\n")
    fileSVM.close()
    
gerarArquivoSVM_LBP()
gerarArquivoSVM_RH()
    


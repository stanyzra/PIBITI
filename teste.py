"""
Modos de leitura de arquivos:
- "r" é de leitura
- "w" é de escrita
- "a" é de escrita, mas começa um arquivo em branco e apaga se já existir
"""
import numpy as np 
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
        
    C_range = np.logspace(-2, 4, 5)
    gamma_range = np.logspace(-9, 3, 5)

    param_grid = dict(kernel=['rbf'], gamma=gamma_range, C=C_range)

    clf = GridSearchCV(SVC(probability=True), param_grid)
  #clf = svm.SVC(kernel='rbf', probability=True)

  # Treina o modelo com os vetores de características e o rótulo (classe/identificador) de cada um
    clf.fit(train_feat, train_label)

  # Classifica cada amostra do seguinte vetor
    predict = clf.predict_proba(test_feat)
  # Ele retorna a label que acha que é para cada uma das imagens
    #print("Predict: ", predict)
    #fileLabel = open("labels/label_")
    print("Rotulos de treino: ", train_label)
    print("Rotulos de teste: ", test_label)
 # a = 0
 # acertos = 0

 #while(a < len(predict)):
      
#      if(predict[a] == test_label[a]):
#          print("Posição do acerto do vetor: ", a) 
#          acertos += 1 
        
#      a += 1

    print("The best parameters with RH are %s with a score of %0.2f"
        % (clf.best_params_, clf.best_score_))
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
            train_label.append(str(pessoa))
        # Se não, joga a amostra para o conjunto de teste
        else:
            test_feat.append(conteudo[linha].split())
            test_label.append(str(pessoa))
        # Conta mais uma amostra para a próxima rodada do for
        cont += 1    
        
    fileLabel = open("labels/labelSVM.txt","w")
    
    for i in range(len(test_label)):
        fileLabel.write(str(test_label[i])+"\n")
    
    fileLabel.close()
    
    C_range = np.logspace(-2, 4, 5)
    gamma_range = np.logspace(-9, 3, 5)
    param_grid = dict(kernel=['rbf'], gamma=gamma_range, C=C_range)

    clf = GridSearchCV(SVC(probability=True), param_grid)
  #clf = svm.SVC(kernel='rbf', probability=True)

  # Treina o modelo com os vetores de características e o rótulo (classe/identificador) de cada um
    clf.fit(train_feat, train_label)

  # Classifica cada amostra do seguinte vetor
    predict = clf.predict_proba(test_feat)
    
    print("Rotulos de treino: ", train_label)
    print("Rotulos de teste: ", test_label)
  # Ele retorna a label que acha que é para cada uma das imagens
    #print("Predict: ", predict)
 # print("Rotulos de teste: ", test_label)
 # a = 0
 # acertos = 0

 #while(a < len(predict)):
      
#      if(predict[a] == test_label[a]):
#          print("Posição do acerto do vetor: ", a) 
#          acertos += 1 
        
#      a += 1

    print("The best parameters with LBP are %s with a score of %0.2f"
        % (clf.best_params_, clf.best_score_))
    return predict

  #print()
  #print("Número de acertos: ", acertos)
  #print("Porcentagem de acerto: ", ((acertos/len(predict))#*100))
  
def gerarArquivoSVM_LBP():
    
    fileSVM = open("predicts/predictSVM_LBP.txt","w")

    conteudoSVM = predictSVM_LBP()
    linhas = len(conteudoSVM)
    colunas = len(conteudoSVM[0])
    print(linhas)
    print(conteudoSVM)
    for i in range(linhas):
      for j in range(colunas):
          fileSVM.write(str(conteudoSVM[i][j])+" ")
      if(i < linhas):
          fileSVM.write("\n")
    fileSVM.close()
    
def gerarArquivoSVM_RH():
    
    fileSVM = open("predicts/predictSVM_RH.txt","w")

    conteudoSVM = predictSVM_RH()
    linhas = len(conteudoSVM)
    colunas = len(conteudoSVM[0])
    
    print(linhas)
    print(conteudoSVM)
    for i in range(linhas):
      for j in range(colunas):
          fileSVM.write(str(conteudoSVM[i][j])+" ")
      if(i < linhas):
          fileSVM.write("\n")
    fileSVM.close()

gerarArquivoSVM_LBP()
gerarArquivoSVM_RH()


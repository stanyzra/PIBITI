"""
Modos de leitura de arquivos:
- "r" é de leitura
- "w" é de escrita
- "a" é de escrita, mas começa um arquivo em branco e apaga se já existir
"""
import numpy as np 
#from sklearn import svm, tree
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
#from sklearn.ensemble import RandomForestClassifier
#from sklearn import tree

def predictSVM():
  
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
  print("Predict: ", predict)
 # print("Rotulos de teste: ", test_label)
 # a = 0
 # acertos = 0

 #while(a < len(predict)):
      
#      if(predict[a] == test_label[a]):
#          print("Posição do acerto do vetor: ", a) 
#          acertos += 1 
        
#      a += 1

  print("The best parameters are %s with a score of %0.2f"
      % (clf.best_params_, clf.best_score_))
  return predict    
  #print()
  #print("Número de acertos: ", acertos)
  #print("Porcentagem de acerto: ", ((acertos/len(predict))#*100))

def predictKNN():
  #weight_options = ['uniform', 'distance']
  # define the parameter values that should be searched
# for python 2, k_range = range(1, 31)
  k_range = list(range(1, 31))
  #C_range = np.logspace(-2, 4, 5)
  #gamma_range = np.logspace(-9, 3, 5)

  param_grid = dict(n_neighbors=k_range)
  for k in k_range:
    # 2. run KNeighborsClassifier with k neighbours
    knn = KNeighborsClassifier(n_neighbors=k)
  clf = GridSearchCV(knn, param_grid,scoring='accuracy')

  #clf = svm.SVC(kernel='rbf', probability=True)

  # Treina o modelo com os vetores de características e o rótulo (classe/identificador) de cada um
  clf.fit(train_feat, train_label)

  # Classifica cada amostra do seguinte vetor
  predict = clf.predict_proba(test_feat)
  # Ele retorna a label que acha que é para cada uma das imagens
  print("Predict: ", predict)
 # print("Rotulos de teste: ", test_label)
 # a = 0
 # acertos = 0

 #while(a < len(predict)):
      
#      if(predict[a] == test_label[a]):
#          print("Posição do acerto do vetor: ", a) 
#          acertos += 1 
        
#      a += 1

  print("The best parameters are %s with a score of %0.2f"
      % (clf.best_params_, clf.best_score_))
  return predict  

fileh = open("lbp.txt", "r")

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


""" Testes para ver os resultados """


#for i in range(len(train_feat)):
   #print(train_feat[i])
   #valTrain = train_feat[i].split() #splitando o conteudo do train_feat
   #train_feat.append(train_feat[i].split())
#for i in range(len(test_feat)):
#   valTest = test_feat[i].split() #splitando o conteudo do train_feat

#print(pessoa)
#print("\nvalTrain: ", valTrain)
#print("\nvalTest: ", valTest)
#print("\ntrain feat: ", train_feat)
#print("----------------------------------------------------------------------")
#print("\ntest feat: ", test_feat)
#print("\ntrain label: ", train_label)
#print("\ntest label: ", test_label)

# Parâmetros para o GridSearch
#param_grid = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9],
#                     'C': [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]},
#                    {'kernel': ['linear'], 'gamma': [1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9],
#                     'C': [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]}]

fileSVM = open("predicts/predictSVM.txt","w")

conteudoSVM = predictSVM()
linhas = len(conteudoSVM)
colunas = len(conteudoSVM[0])

print(linhas)
for i in range(linhas):
  for j in range(colunas):
    fileSVM.write(str(conteudoSVM[i][j])+" ")


fileSVM.close()

"""

fileKNN = open("predictKNN.txt","w")

conteudoKNN = predictKNN()
linhas = len(conteudoKNN)
colunas = len(conteudoKNN[0])

print(linhas)
for i in range(linhas):
  for j in range(colunas):
    fileKNN.write(str(conteudoKNN[i][j])+" ")


fileKNN.close()
"""
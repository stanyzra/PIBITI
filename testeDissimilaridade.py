import numpy as np

fileh = open("features/mfcc50.txt", "r")
    
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
        np.array(train_feat.append(conteudo[linha].split()))
        train_label.append(str(pessoa))
    # Se não, joga a amostra para o conjunto de teste
    else:
        test_feat.append(conteudo[linha].split())
        test_label.append(str(pessoa))
    # Conta mais uma amostra para a próxima rodada do for
    cont += 1

# n é o numero de amostras do treinamento
n = 240
# p é a quantidade de amostras por pessoa
p = 3
# vp é o array de vetores positivos
vp = []
x = np.array(train_feat)

for i in range(0, n, p):
    
    v1 = np.float16(x[i]) - np.float16(x[i+1]) 
    v2 = np.float16(x[i]) - np.float16(x[i+2])
    v3 = np.float16(x[i+1]) - np.float16(x[i+2])
	
    vp.append(v1)
    vp.append(v2)
    vp.append(v3)
        
# vp é o array de vetores negativos
vn = []

for i in range(0, n-p):

	v1 = np.float16(x[i]) - np.float16(x[i+p])

	vn.append(v1)    

labels_vp = []
labels_vn = []

for linha in range(len(vp)):
    vp.append("1 ")
    
    
    
    
    
    
    
    
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

#aqui geramos os arquivos .txt do vetor POSITIVO com sua label e sua respectiva característica
def gerarArquivoVP():  
    fileVP = open("features/vetPos.txt","w")

    conteudoVp = vp
    
    linhas = len(conteudoVp)
    colunas = len(conteudoVp[0])
   
    cont = 0
    amostra_train = 3
    classe = 0
    contCol = 0
    
    for i in range(linhas):
        if i > 0 and i % 3 == 0:
            classe += 1
            cont = 0
            if cont < amostra_train:
                #fileVP.write(str(classe)+" ")
                cont += 1   
                for j in range(colunas):
                    fileVP.write(str(contCol+1)+":"+str(conteudoVp[i][j])+" ")
                    contCol += 1
                    if j > colunas:
                        contCol = j
            if(i < linhas):
              fileVP.write("\n")
    fileVP.close()
    
#aqui geramos os arquivos .txt do vetor NEGATIVO com sua label e sua respectiva característica
def gerarArquivoVN():
    fileVN = open("features/vetNeg.txt","w")

    conteudoVn = vn
    
    linhas = len(conteudoVn)
    colunas = len(conteudoVn[0])
           
    cont = 0
    amostra_train = 3
    classe = 0
    contCol = 0
    
    for i in range(linhas):
        if i > 0 and i % 3 == 0:
            classe += 1
            cont = 0
            if cont < amostra_train:
                #fileVN.write(str(classe)+" ")
                cont += 1   
                for j in range(colunas):
                    fileVN.write(str(contCol+1)+":"+str(conteudoVn[i][j])+" ")
                    contCol += 1
                    if j > colunas:
                        contCol = j
            if(i < linhas):
              fileVN.write("\n")
    fileVN.close()

gerarArquivoVP()
gerarArquivoVN()   
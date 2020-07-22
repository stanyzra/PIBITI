import numpy as np
"""
fileDiss = open("libsvm-3.24/tools/vetor_diss_teste.txt.predict","r")

conteudoDiss = fileDiss.readlines()

fileDiss.close()


linhas = len(conteudoDiss)
p = 160 #passo
pos_vetor = 0

vetDiss = [] #vetor que separa as caracteristicas em colunas para facilitar as operações

for i in range(linhas):
    np.array(vetDiss.append(conteudoDiss[i].split()))


vetPos = []
colunas = len(vetDiss[0])

#print(np.argmax(vetDiss[2]))

# Dados para  calcular a acurácia
acertos = 0
total_amostras = 160

# Para verificar se a amostra foi classificada corretamente, faz esse passo
# para verificar qual a maior probabilidade de ser positivo
# Posição do vetor que é ele - ele: 1, 162, 323, 484... +161
for i in range(1, linhas, p):

    # vetor que é ele - ele    
    pos_vetor += 1
    
    # Encontrar a posição do vetor que deve ser o maior acerto positivo
    if pos_vetor %2 == 0:
        certo_pos = pos_vetor-1
    else:
        certo_pos = pos_vetor+1
        
    # Variáveis para encontrar onde está o maior acerto positivo
    maior_pos = 0
    maior_taxa = 0
    
    # Percorre os 160 vetores para saber qual é o maior acerto positivo
    # Faz um for com base no intervalo
    for j in range(i, i+160): #de 1 até 160, pois a linha 0 são as labels
    
        if j == pos_vetor:
            pass
    
        if float(vetDiss[j][1]) > maior_taxa:
            maior_taxa = float(vetDiss[j][1])
            maior_pos = j
            
    print("Posição do maior {} com taxa {}".format(maior_pos, maior_taxa))
            
    if maior_pos == certo_pos:
        acertos += 1
            
    print("Vetor atual {}, onde ver o vetor certo {}, Maior posição {}".format(pos_vetor, certo_pos, maior_pos))
            
    pos_vetor += 160
    
print("Acertos: {}/160 = {}%".format(acertos, (acertos/160)*100))
"""
fileDiss = open("libsvm-3.24/tools/vetor_diss_teste.txt.predict","r")
conteudoDiss = fileDiss.readlines()
fileDiss.close()

# Converte as linhas de string para matriz
linhas = len(conteudoDiss)
vetDiss = [] #vetor que separa as caracteristicas em colunas para facilitar as operações
for i in range(linhas):
    np.array(vetDiss.append(conteudoDiss[i].split()))


# Função para encontrar posição do maior valor
#print(np.argmax(vetDiss[2]))

# Conta as colunas do arquivo: % classe1 classe2 .... classeN
colunas = len(vetDiss[0])
# Dados para  calcular a acurácia
acertos = 0
# Total de amostras no teste, não o total de vetores de dissimilaridade no teste
total_amostras = 160
# Passo é igual o total de amostras
p = total_amostras
# Posição correta do vetor positivo
pos_vetor = 0

# Para verificar se a amostra foi classificada corretamente, faz esse passo
# para verificar qual a maior probabilidade de ser positivo
# Posição do vetor que é ele - ele: 1, 162, 323, 484... +161
for i in range(1, linhas, p):
    
    # vetor que é ele - ele    
    pos_vetor += 1

    # Zera a % do vetor que é ele - ele
    vetDiss[pos_vetor] = ['0']*colunas
    
    # Encontrar a posição do vetor que deve ser o maior acerto positivo
    if pos_vetor %2 == 0:
        certo_pos = pos_vetor-1
    else:
        certo_pos = pos_vetor+1
        
    # Variáveis para encontrar onde está o maior acerto positivo
    maior_pos = 0
    maior_taxa = 0
    
    # Percorre os 160 vetores para saber qual é o maior acerto positivo
    # Faz um for com base no intervalo
    for j in range(i, i+total_amostras): #de 1 até 160, pois a linha 0 são as labels
    
        if j == pos_vetor:
            pass
    
        if float(vetDiss[j][1]) > maior_taxa:
            maior_taxa = float(vetDiss[j][1])
            maior_pos = j
            
    print("Posição do maior {} com taxa {}".format(maior_pos, maior_taxa))
            
    if maior_pos == certo_pos:
        acertos += 1
        print("acertou")
            
    print("Vetor atual {}, onde ver o vetor certo {}, Maior posição {}".format(pos_vetor, certo_pos, maior_pos))
            
    pos_vetor += total_amostras
    
print("Acertos: {}/{} = {}%".format(acertos, total_amostras, (acertos/total_amostras)*100))


"""

Vetores de características

1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
1 2 3 4
10 10 10 10
11 11 11 11
12 12 12 12
13 13 13 13
10 11 12 13
20 20 20 20
21 21 21 21
22 22 22 22
23 23 23 23
20 21 22 23
30 30 30 30
31 31 31 31
32 32 32 32
33 33 33 33
30 31 32 33

for i in range(0, linhas, p):
    print(i)
    if i < linhas:
        for j in range(i, i+p):
            if j < linhas and vetDiss[i][1] > vetDiss[j][1]:
                print("j: {}".format(j))
                pos = j
"""
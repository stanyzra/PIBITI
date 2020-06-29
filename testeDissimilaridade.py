import numpy as np

fileDiss = open("libsvm-3.24/tools/vetor_diss_teste.txt.predict","r")

conteudoDiss = fileDiss.readlines()

fileDiss.close()


linhas = len(conteudoDiss)
p = 80 #passo

vetDiss = [] #vetor que separa as caracteristicas em colunas para facilitar as operações

for i in range(linhas):
    np.array(vetDiss.append(conteudoDiss[i].split()))

vetPos = []
colunas = len(vetDiss[0])

#print(np.argmax(vetDiss[2]))

#for que percorre o vetDiss à um passo de 80

"""

for i in range(0, linhas, p):
    for j in range(1, 80): #de 1 até 80, pois a linha 0 são as labels
        if vetDiss[i][1] > vetDiss[j][1]:
            pos = j
            print(pos)

for i in range(0, linhas, p):
    print(i)
    if i < linhas:
        for j in range(i, i+p):
            if j < linhas and vetDiss[i][1] > vetDiss[j][1]:
                print("j: {}".format(j))
                pos = j
"""
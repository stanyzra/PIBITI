import numpy as np
"""
filePos = open("features/vetPos.txt", "r")
fileNeg = open("features/vetNeg.txt", "r")

conteudoPos = filePos.readlines()
conteudoNeg = fileNeg.readlines()

filePos.close()
fileNeg.close()

conteudoVet = []
vet = []
contCol = 0

for i in range(len(conteudoPos)):
    conteudoVet.append(conteudoPos[i].split())
    colunas = len(conteudoVet[0])
    for j in range(colunas):
        if j < colunas:
            #conteudoVet.append(conteudoPos[i].replace(":",""))
            contCol = str(j)+":"
            conteudoPos[i].replace(contCol,"")

          
for i in range(len(conteudoNeg)):
    conteudoVet.append(conteudoNeg[i].split())
    contCol = len(conteudoVet[0])


#x = np.array(conteudoVet)

for i in range(len(conteudoVet)):
    for j in range(len(conteudoVet)):
        vet_test = np.float16(conteudoVet[i].replace(conteudoVet[0],"").replace(" ","").split(":")) - np.float16(conteudoVet[j].replace(conteudoVet[0],"").replace(" ","").split(":"))

"""
def teste(vetor_teste):
    
    x = np.array(vetor_teste)
    vetor_diss = []
    linha = len(x)
    
    for i in range(linha):
        for j in range(linha):
#            if i == j:
#                continue
            v = np.float16(x[i]) - np.float16(x[j])
            vetor_diss.append(v)
            
   #print(vetor_diss)
    file_vetor_diss = open("predicts/vetor_diss.txt","w")
   
    conteudo_diss = vetor_diss
    
    linhas = len(conteudo_diss)
    colunas = len(conteudo_diss[0])
   
    cont = 0
    amostra_test = 2
    classe = 0
    
    for i in range(linhas):
        if i > 0 and i % 2 == 0:
            classe += 1
            cont = 0
            if cont < amostra_test:
                file_vetor_diss.write("0 ")
                cont += 1   
                for j in range(colunas):
                    file_vetor_diss.write(str(j+1)+":"+str(conteudo_diss[i][j])+" ")
            if(i < linhas):
              file_vetor_diss.write("\n")
    file_vetor_diss.close()
       
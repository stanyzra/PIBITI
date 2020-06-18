import numpy as np

def teste(vetor_teste):
    
    x = np.array(vetor_teste)
    vetor_diss = []
    linha = len(x)
    #print(range(linha))
    #print(range(len(linha)))
    
    for i in range(linha):
        for j in range(linha):
#            if i == j:
#                continue
            v = np.float16(x[i]) - np.float16(x[j])
            vetor_diss.append(v)
            
   #print(vetor_diss)
    file_vetor_diss = open(".gitignore/vetor_diss.txt","w")
   
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
       
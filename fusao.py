# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:33:11 2019

@author: aleix
"""
import numpy as np

def lerLBP():
    fileh = open("predicts/predictSVM_LBP.txt","r")
    
    conteudo = fileh.readlines()
    
    fileh.close()
    
    return conteudo

def lerRH():
    fileh = open("predicts/predictSVM_RH.txt","r")
    
    conteudo = fileh.readlines()
    
    fileh.close()
    
    return conteudo

conteudoLBP = (lerLBP())
conteudoRH = (lerRH())

# Cria os vetores para armazenar a fusão
vetSoma = []
vetProduto = []
vetMax = []

for lin in range(len(conteudoLBP)):

    # Gera o vetor com os predicts somente do 0 até o 79, porque 80 (classes) não conta
    vetPredictLBP = conteudoLBP[lin].replace('\n', '').split(" ")[0:80]
    vetPredictRH = conteudoRH[lin].replace('\n', '').split(" ")[0:80]
    # vetor[inicio:fim]
    
    # Mostra a última posição do vetor
    # print("Vet predict:", vetPredictLBP[-1])

    # Faz a fusão
    linhaSoma = [float(x) + float(y) for x, y in zip(vetPredictLBP, vetPredictRH)]
    linhaProduto = [float(x) * float(y) for x, y in zip(vetPredictLBP, vetPredictRH)]
    linhaMax = [x if float(x) >= float(y) else y for x, y in zip(vetPredictLBP, vetPredictRH)]

    # Adiciona a linha que foi fundida ao vetor com todos os valores
    vetSoma.append(linhaSoma)
    vetProduto.append(linhaProduto)
    vetMax.append(linhaMax)

# Criar os arquivos do zero no modo escrita
fileSoma = open("predicts/predictSoma.txt", "w")
fileProduto = open("predicts/predictProduto.txt", "w")
fileMax = open("predicts/predictMax.txt", "w")

for lin in range(len(vetSoma)):
    linhaSoma = str(vetSoma[lin]).replace("[", "").replace("]", "").replace(",", "")
    linhaProduto = str(vetProduto[lin]).replace("[", "").replace("]", "").replace(",", "")
    linhaMax = str(vetMax[lin]).replace("[", "").replace("]", "").replace(",", "")

    fileSoma.write(linhaSoma.replace("'","")+"\n")
    fileProduto.write(linhaProduto.replace("'", "")+"\n")
    fileMax.write(linhaMax.replace("'", "")+"\n")

fileSoma.close()
fileProduto.close()
fileMax.close()

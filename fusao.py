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

conteudoLBP =(lerLBP())
conteudoRH = (lerRH())
linhas = len(conteudoLBP)
colunas = len(conteudoLBP[0])
print("linhas: ",linhas)
print("colunas: ",colunas)

for i in range(int(linhas/2)):

    print(i)
    numLBP = conteudoLBP[i].replace('\n','').split(" ")
    numRH = conteudoRH[i].replace('\n','').split(" ")
    #del(numLBP[80])
    #del(numRH[80])
    numLBP = np.delete(numLBP,80)
    numRH = np.delete(numRH,80)
    #fusaoSaidas = sum((numLBP), (numRH))
    fusaoSaidas = np.maximum(numLBP.astype(np.float),numRH.astype(np.float))
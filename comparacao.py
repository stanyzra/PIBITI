# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:44:57 2019

@author: aleix
"""
import numpy as np

# lendo os arquivos de predict e label criados anteriormente
conteudoSoma = np.loadtxt("predicts/predictSoma.txt")
conteudoProduto = np.loadtxt("predicts/predictProduto.txt")
conteudoMax = np.loadtxt("predicts/predictMax.txt")
conteudoLabelSVM = np.loadtxt("labels/labelSVM.txt")

# criando vetores e variáveis para a comparação
label_soma = []
label_produto = []
label_max = []
test_label = []
acertoSoma = 0
acertoProduto = 0
acertoMax = 0

#for para atribuir aos vetores o índice do maior coluna de uma linha (classe de uma amostra)
for lin in range(len(conteudoSoma)):

    label_soma = np.array(conteudoSoma[lin].copy())
    label_soma = np.argmax(conteudoSoma[:,1:], 1)+1
    
    label_produto = np.array(conteudoProduto[lin].copy())
    label_produto = np.argmax(conteudoProduto[:,1:], 1)+1
    
    label_max = np.array(conteudoMax[lin].copy())
    label_max = np.argmax(conteudoMax[:,1:], 1)+1
    
# salvando os resultados em um arquivo de texto    
np.savetxt('labels/label_soma.txt', label_soma, fmt='%d')
np.savetxt('labels/label_produto.txt', label_produto, fmt='%d')
np.savetxt('labels/label_max.txt', label_max, fmt='%d')

# for para comparar os valores dos labels das fusões com o test_label
for a in range(len(conteudoLabelSVM)):
    test_label = np.array(conteudoLabelSVM.copy()).astype(int)
    
    if label_soma[a] == test_label[a]:
        acertoSoma = acertoSoma + 1
    
    if label_produto[a] == test_label[a]:
        acertoProduto = acertoProduto + 1
    
    if label_max[a] == test_label[a]:
        acertoMax = acertoMax + 1
        
print("Acertos do método da soma: ",acertoSoma)
print("Acertos do método do produto: ",acertoProduto)
print("Acertos do método do máximo: ",acertoMax)
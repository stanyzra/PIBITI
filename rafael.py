# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:44:57 2019

@author: aleix
"""
import numpy as np


def gerar_labels(arquivo):
    # lendo os arquivos de predict e label criados anteriormente
    conteudo = np.loadtxt(arquivo)

    # Gera o nome do arquivo certo
    if "/" in arquivo:
        nome_arquivo_label = arquivo.split("/")[1]

    # Remove o .txt
    nome_arquivo_label = nome_arquivo_label.replace(".txt", "")
    nome_arquivo_label = "labels/{}_label.txt".format(nome_arquivo_label)

    # Cria o arquivo
    arquivo_label = open(nome_arquivo_label, "w")

    # for para atribuir o índice do maior coluna de uma linha (classe de uma amostra)
    for lin in range(len(conteudo)):

        # Copia a linha de posição "lin" do arquivo e transforma num vetor
        linha_predict = np.array(conteudo[lin].copy())
        # O argmax retorna a posição do maior valor. Como o vetor começa em 0 e nossas labels em 1, fiz + 1
        label = np.argmax(linha_predict) + 1
        print(label)
        # salvando os resultados em um arquivo de texto
        arquivo_label.write("{}\n".format(label))

    # Fecha o arquivo
    arquivo_label.close()

    # Retorna o nome do arquivo de labels que ele gerou
    return nome_arquivo_label


def comparar_labels(label_correta, label_gerada):
    # lendo os arquivos de predict e label criados anteriormente
    conteudo_correto = np.loadtxt(label_correta)
    conteudo_gerada = np.loadtxt(label_gerada)
    print(conteudo_gerada)
    # Conta os acertos
    acertos = 0

    # Percorre os arquivos de labels
    for lin in range(len(conteudo_correto)):

        # Se as linhas forem iguals, conta um acerto... Desde que não seja vazio nem \n
        if conteudo_correto[lin] == conteudo_gerada[lin] and conteudo_correto[lin] != "" and conteudo_correto[lin] != "\n":
            acertos += 1

    print("O total de acertos do arquivo {} foi de {}.".format(label_gerada, acertos))


resultado = gerar_labels("predicts/predictSVM_LBP.txt")
comparar_labels("labels/labelSVM.txt", resultado)

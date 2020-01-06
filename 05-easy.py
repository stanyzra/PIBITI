# -*- coding: utf-8 -*-
"""
@author: Rafael Zottesso
@descprition: Faz a chamada para o SVM e também a validação cruzada para os N folds
@Date: 03/11/2015
"""
import os, sys

def execLIBSVM(dir_origem, folds_qtde, tipo, zona, escala, early_fusion, early):

    # Guarda as informações dos arquivos e do processo
    info = open('_info.txt', 'w')
    conteudo = 'Origem: ' + dir_origem + '\n'
    info.write(conteudo)
    info.close()

    # Faz as chamadas para os folds
    for i in range(1, folds_qtde+1):

        # Cria a referência para os arquivo de treino e teste
        # treino = dir_origem + 'treino-menos-f' + str(i) + '.svm'
        # teste = dir_origem + "fold-" + ("%02d" % i) + '-lbp.svm'
        # predict_cp = teste + '.predict' #onde ficará a cópia
        # predict = dir_svm + "fold-" + ("%02d" % i) + '-lbp.svm.predict' # onde está o original

        # Cria a referência para os arquivo de treino e teste
        treino = 'treino-menos-f' + ("%02d" % i) + escala + zona + '.svm'
        teste = 'fold-' + ("%02d" % i) + escala + zona + '-' + early + tipo + '.svm'
        nohup = teste + '.nohup'
        
        # Executa o libsvm
        comando_easy = 'nohup python easyDiego.py %s%s %s%s > %s ' %(dir_origem,treino,dir_origem,teste,nohup)
        os.system(comando_easy)
        print comando_easy
        #print comando_easy

        # Copia os models para a pasta dos folds
        #comando_copy = 'cp %s.{model,range,scale,scale.out,scale.png} %s' % (treino,dir_origem)
        comando_copy = 'mv %s.* %s' % (treino,dir_origem)
        os.system(comando_copy)
        #print comando_copy
        
        # Copia os predicts para a pasta dos folds
        #comando_copy = 'cp %s.{scale,predict.nohup} %s' % (teste,dir_origem)
        comando_copy = 'mv %s.* %s' % (teste,dir_origem)
        os.system(comando_copy)
        #print comando_copy
        
        # Apenas para separar com uma linha os resultados
        #print '\n=================================================================='
#####################################################################


# Verifica se é Windows ou Linux
is_win = (sys.platform == 'win32')
# Se for windows...
if not is_win:
	dir_origem = '/media/rafael/Dados/Mestrado/'
# Se for Linux...
else:
    dir_origem = 'D:/Mestrado/'

#dir_svm = "/home/rafael/Dropbox/UEM Mestrado/TCC/libsvm-3.20/tools/"
dir_svm = "./libsvm-3.20/tools/"

# Vai para a pasta do libsvm
os.chdir(dir_svm)

#####################################################################
# Origem origem dos folds
dir_origem += 'base_juliano_segmentada_manual_concatenada_6s_rp/'
# Quantidade de folds
folds_qtde = 10
# Tipo dos arquivos (descritor de textura)
tipo = 'rp'
# Se a imagem não foi "zoneada" deixe o parâmetro como vazio = ""
# Se foi 'zoneada', defina a quantidade de zonas 
zonas = ''
# Defina o nome da escala (que está no arquivo) 
# Sempre com um menos, ex: -mel ou -bark ou -nome
escala = ''
# Foi feita a fusão de vetores? (early fusion): 1 = sim, 0 = não
early_fusion = 0
# Este conteúdo será adicionado ao nome do arquivo
if early_fusion:
    early = 'early-'
else:
    early = ''
#####################################################################

# Executa o script várias vezes caso existam diversas zonas
if zonas != '':
    # Executa a função para todas as zonas
    for z in range(1, zonas+1 ):
        # Cria o parâmetro zona pra ser usado na nomeclatura dos arquivos
        zona = '-' + str(z)
        execLIBSVM(dir_origem, folds_qtde, tipo, zona, escala, early_fusion, early)
# Caso não existam zonas...
else:
    execLIBSVM(dir_origem, folds_qtde, tipo, zonas, escala, early_fusion, early)
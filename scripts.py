""" 
Arquivo que possui as funções para editar arquivos e rodar o SVM
"""

'''
@Descrição
Função que recebe um arquivo "cru" de características por parâmetro e
transforma no jeito certo para usar no LibSVM.
@Parâmetros
Nome do arquivo com as características
Número total de características por linha
Número de classes
Quantidade de amostras por classe
Quantidade de amostras (linhas) que ficaram no arquivo de TREINO
Quantidade de amostras (linhas) que ficaram no arquivo de TESTE
@Entrada
c1 c2 c3 ... cn
c1 c2 c3 ... cn
c1 c2 c3 ... cn
c1 c2 c3 ... cn
@Saída
Classe 1:c1 2:c2 3:c3 ... n:cn
'''
def features_to_svm(arquivo_caract, num_caract, num_classes, amostras_por_classe, qtde_treino, qtde_teste):

    # Abre o arquivo, lê o conteúdo para um vetor e fecha
    arquivo = open(arquivo_caract, "r")
    conteudo = arquivo.readlines()
    arquivo.close()

    # Controla o ID da amostra
    classe_amostra = 0
    
    # Conta as amostras por classe
    cont_por_classe = 0

    # Vetor para treino e teste
    treino = []
    teste = []
    treino_classes = []
    teste_classes = []


    for linha in range(len(conteudo)):

        # Verifica se a linha não está vazia
        if conteudo[linha].strip() == "" or conteudo[linha].strip() == "\n":
            continue

        # Conta 1 amostra
        cont_por_classe += 1

        # Troca a classe da amostra
        if linha > 0 and linha % amostras_por_classe == 0:
            cont_por_classe = 1
            classe_amostra += 1

        # Usa no treinamento se o cont for até a quantidade de amostras para treino
        if cont_por_classe <= qtde_treino:
            treino.append(conteudo[linha])
            treino_classes.append(classe_amostra)
        # A amostra vai para para o conjunto de teste
        elif cont_por_classe <= qtde_teste + qtde_treino:
            teste.append(conteudo[linha])
            teste_classes.append(classe_amostra)
        # Se ainda sim sobrar amostras, pula essa amostra
        else:
            continue

        # Fim da separação das amostras...
    
    # Abre o arquivo de saída de treino
    arquivo_treino = open("treino.txt", "w")

    # Para cada amostra no treino...
    for i in range(len(treino)):

        # Escreve no arquivo a classe dessa amostra "i"
        arquivo_treino.write("{} ".format(treino_classes[i]))

        # Transforma a linha inteira que é um str em um vetor, quebrando nos espaços
        caracteristicas = treino[i].split()

        # Enumera as características
        enum = 1

        # Para cada característica..
        for c in caracteristicas:

            # Escreve "n:característica" com espaço no final 
            arquivo_treino.write("{}:{} ".format(enum, c))

            enum += 1
        
        # Quebra linha
        arquivo_treino.write("\n")
    
    # Fecha o arquivo
    arquivo_treino.close()

    # Abre o arquivo de saída de treino
    arquivo_teste = open("teste.txt", "w")

    # Para cada amostra no teste...
    for i in range(len(teste)):

        # Escreve no arquivo a classe dessa amostra "i"
        arquivo_teste.write("{} ".format(teste_classes[i]))

        # Transforma a linha inteira que é um str em um vetor, quebrando nos espaços
        caracteristicas = teste[i].split()

        # Enumera as características
        enum = 1

        # Para cada característica..
        for c in caracteristicas:

            # Escreve "n:característica" com espaço no final
            arquivo_teste.write("{}:{} ".format(enum, c))

            enum += 1

        # Quebra linha
        arquivo_teste.write("\n")

    # Fecha o arquivo
    arquivo_teste.close()
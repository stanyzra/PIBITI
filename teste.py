"""
Modos de leitura de arquivos:
- "r" é de leitura
- "w" é de escrita
- "a" é de escrita, mas começa um arquivo em branco e apaga se já existir
"""
fileh = open("lbp.txt", "r")

conteudo = fileh.readlines()

fileh.close()

# Agora que vocês sabem que a variável "conteúdo" é um vetor,
# faça um laço de repetição para mostrar na tela os nomes do arquivo

# Controla o ID da pessoa
pessoa = 1
# Quantas amostras das 5 serão utilizadas no treinamento
amostras_treino = 3
# Conta as amostras de cada pessoa
cont = 1

# Vetor para treinamento do modelo e rótulos
train_feat = []
# Criação das labens (rótulos/classes) para o classificador
train_label = []

''' Será usado para o classificador '''
# Vetor para teste de predict
test_feat = []
# Criação das labens (rótulos/classes) para o classificador
test_label = []

for linha in range(len(conteudo)):

    # A cada 5 amostras troca-se a pessoa
    if linha > 0 and linha % 5 == 0:
        pessoa += 1
        cont = 1

    # Usa no treinamento se o cont for até a quantidade de amostras para treino
    if cont <= amostras_treino:
        train_feat.append(conteudo[linha])
        train_label.append(str(pessoa))
    # Se não, joga a amostra para o conjunto de teste
    else:
        test_feat.append(conteudo[linha])
        test_label.append(str(pessoa))

    # Conta mais uma amostra para a próxima rodada do for
    cont += 1


""" Testes para ver os resultados """

print(pessoa)
# print("\ntrain feat: ", train_feat)
print("\ntrain label: ", train_label)
# print("\ntest feat: ", test_feat)
print("\ntest label: ", test_label)

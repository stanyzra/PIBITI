"""
Modos de leitura de arquivos:
- "r" é de leitura
- "w" é de escrita
- "a" é de escrita, mas começa um arquivo em branco e apaga se já existir
"""
fileh = open("lbp.txt","r")

conteudo = fileh.readlines()

fileh.close()

# Agora que vocês sabem que a variável "conteúdo" é um vetor,
# faça um laço de repetição para mostrar na tela os nomes do arquivo
l = 0
pessoa = 0
cont = 0
#while l < len(conteudo) :
#    print( conteudo[l] )
#    l+=1

# A mesma coisa com for
#for linha in conteudo:
#    print(linha)

# Vetor para treinamento do modelo e rótulos
train_feat = []
# Criação das labens (rótulos/classes) para o classificador
train_label = []

''' Será usado para o classificador '''
# Vetor para teste de predict
test_feat = []
# Criação das labens (rótulos/classes) para o classificador
test_label = []

for l in range( len(conteudo) ):
    #print( conteudo[l] )
    if l % 5 == 0:
        pessoa += 1
        if cont < 3:
            train_feat.append( conteudo[l] )
            train_label.append( str(pessoa) )
            cont += 1

        else:
            if cont < 5:
                test_feat.append( conteudo[l] )
                test_label.append( str(pessoa) )
                cont += 1                
                if cont == 5:
                    cont = 0
print(pessoa)
print("train feat: ", train_feat)
print()
print("train label: ", train_label)
print()
print("test feat: ", test_feat)
print()
print("test label: ", test_label)
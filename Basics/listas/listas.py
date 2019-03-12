# criando uma lista de nomes
print('Criando uma lista na mão e imprimindo ela: \n')
nomes = ['Pedro','Gabriel','Felipe']

# Imprimindo a lista
print(nomes)

# Andando entre os valores da lista
# tipo 1: andando na lista com uma variavel criada
print('\nAndando na lista com variavel criada: ')
for nome in nomes:
    print(nome)

# tipo 2: andando na lista com range()

print('\nandando na lista com range(): ')
for i in range(len(nomes)):
    print(nomes[i])


# Adicionando mais um nome no fim da lista
nomes.append('Bruno')
print('\n1) Adicionado o elemento bruno com append():\n')
print(nomes)

# Adicionando mais um elemento na segunda posicao
print('\n2) Colocamos a pessoa Fulano na segunda posicao da lista:\n')
nomes.insert(1,'Fulano')
print(nomes)

# Adicionando uma valor com input()

# com append()
print('\nTeste de insercao com append(): \n')
nome_input = input('Digite um nome para colocar na lista: \n')
nomes.append(nome_input)
print(nomes)

# com insert()
print('\nTeste de insercao com insert() e input(): \n')
posicao = input('Digite a posicao onde deseja adicionar: ')
nome_input = input('Digite o nome que deseja salvar: \n')

nomes.insert(int(posicao),nome_input)
print(nomes)

# Adicionando um valor com funções

# funcao usando append()
def add_final(valor,lista):
    lista.append(valor)
    print("valor adicionado: ",valor,'\n')

# funcao usando insert()
def add_pos(posicao,valor,lista):
    lista.insert(int(posicao),valor)
    print('Valor adicionado: ',valor,'\n')


# Chamada de Funções
add_final('LARISSA',nomes)

add_pos(2,'RODRIGO',nomes)

print(nomes)

# Retirando o ultimo elemento
print('\n2) Retirado o ultimo elemento com pop()\n')
elemento_retirado = nomes.pop()
print('Elemento retirado: ', elemento_retirado)
print('Lista: ', nomes)

# Retirando o segundo elemento da lista
print('\nRetirado o segundo elemento da lista')
elemento_retirado_2 = nomes.pop(1)()
print('Elemento removido: ', elemento_retirado_2)
print('Lista: ', nomes)

# Removendo o elemento Johhny
print('Adicionando o elemento Johnny para testar o remove()')

# Descobrindo o tamanho da lista
tamanho = len(nomes)
print('\ntamanho da lista: ', tamanho)

# Ordenando uma lista
nomes.sort()
print('\nLista Ordenada: ', nomes)

# Mostrando a lista de forma inversa
nomes.reverse()
print('\nLista Reversa: ', nomes)

# Lendo os elementos da lista com um laço for
print('\nLendo uma lista com um For')
for nome in nomes:
    print(nome)

# usando o limitador para pegar os 2 elementos finais
print('\npegando os ultimos elementos da lista')
for nome in nomes[2:]:
        print(nome)
print('\npegando os primeiros elementos da lista')
for nome in nomes[:2]:
    print(nome)
print('\ncopiando toda a lista')
copia_nome = nomes[:]
print(copia_nome)
    


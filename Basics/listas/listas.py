# criando uma lista de nomes
nomes = ['Pedro','Gabriel','Felipe']

# Imprimindo a lista
print(nomes)

# Adicionando mais um nome no fim da lista
nomes.append('Bruno')
print('\n1) Adicionado o elemento bruno com append()\n')
print(nomes)

# Retirando o ultimo elemento
elemento_retirado = nomes.pop()
print('\n2) Retirado o ultimo elemento com pop()\n')
print('Elemento retirado: ', elemento_retirado)
print('Lista: ', nomes)

# Retirando o segundo elemento da lista
elemento_retirado2 = nomes.pop(1)
print('\nRetirado o segundo elemento da lista')
print('Elemento removido: ', elemento_retirado2)
print('Lista: ', nomes)

# Adicionando novamente os elementos na lista
nomes.append(elemento_retirado)
nomes.append(elemento_retirado2)
print('\nColocados os elementos retirados de volta')
print('Lista completa: ', nomes)

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
    


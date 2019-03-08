# Arquivo Python para teste de For

# Lendo uma lista de nomes com for
nomes = ['Pedro','Gabriel','Lili','Dodo']

print('\nLendo os nomes um por um: ')
for nome in nomes:
    print(nome)

# criando os valores de um vetor de numeros de 1 á 10
print('\nLendo os valores criados na hora de 1 a 10')
for valor in range(1,11):
    print(valor)

# criando uma lista de valores de 1 á 20
print('\nCriando e lendo uma lista de numeros de 1 a 20')
valores = [] # lista vazia criada
for valor in range(1,21):
    valores.append(valor)
print('\nLista de valores: ',valores)

# criando uma lista de pares
print('\nCriando uma lista de Pares')
pares = []
for valor in range(1,11):
    par = valor*2 #definindo os valores como pares
    pares.append(par) #colocando os valores na lista
print('\nLista de Pares: ', pares)

# da lista de valores de 1 á 20, pegar de 10 á 20
print('\nPegando os valores de 10 a 20')
for valor in valores[9:]:
    print(valor)
 

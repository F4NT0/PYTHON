# ---------------------------
# CRIANDO E UTILIZANDO LISTAS
# ---------------------------

# Criando uma Lista manualmente
lista = ['A','B','C','D']

# Criando uma Lista vazia
lista2 = []

# Imprimindo a Lista em formato Lista
print(lista)

# Pegando o primeiro valor da Lista
print("Primeiro valor da Lista: " + lista[0])

# Pegando o ultimo valor da Lista
print("Ultimo valor da Lista: " + lista[-1])

#
# ADICIONAR 
#

# Adicionando um valor no final da Lista
lista.append('E')
print("\nUltimo valor da Lista após o append(): " + lista[-1])
print(lista)

# Adicionando um valor na primeira posição de lista2
lista2.insert(0,'A')
print("\nPrimeiro valor da Lista2 usado o insert(): " + lista2[0])
print(lista2)

#
# REMOVER
#

# Retirando o ultimo valor da lista usando a função pop()
valor_retirado = lista.pop()
print("\nValor Retirado do final da Lista: " + valor_retirado)
print(lista)

# Retirando um valor específico da lista pela posição usando pop()
valor_retirado = lista.pop(2)
print("\nValor Retirado da Posição 2: " + valor_retirado)
print(lista)

# Removendo um valor específico da Lista usando a Função remove()
valor_retirado = lista.remove('A')
print("\nUsado o remove() para retirar o valor A")
print(lista)

#
# ORDENAÇÃO
#

# Ordenando uma lista de forma permanente e crescente(alfabeto)
lista = ['B','C','A','D']
lista.sort()
print("\nOrdenado permanentemente a lista de forma alfabetica e crescente")
print(lista)

# Ordenando uma lista de forma permanente e crescente(numeros)
lista2 = [3,2,1,4]
lista2.sort()
print("\nOrdenando permanentemente a lista de forma numerica e crescente")
print(lista2)

# Ordenando de forma decrescente utilizando o Atributo reverse = True
lista3 = [4,3,2,1]
lista3.sort(reverse = True)
print("\nOrdenando permanentemente a lista de forma decrescente")
print(lista3)

# Invertendo a Lista permanentemente usando a Função reverse()
lista3.reverse()
print("\nReordenando de forma inversa a Lista anterior")
print(lista3)

# Ordenando de forma temporária a Lista
lista4 = ['B','C','A','D']
print("\nOrdenando de forma temporária sem mexer na lista original")
print(sorted(lista4))
print("Original: ")
print(lista4)
 
#
# TAMANHO DA LISTA
#

# Pegando o tamanho da Lista e salvando esse valor, tamanho da lista é o numero de elementos não as posições

tamanho_lista = len(lista)
print("\nPegando o tamanho da Lista")
print(lista)
print("Tamanho da Lista armazenada em variavel: " + str(tamanho_lista)) #por ser numero deve transformar em String
print("Tamanho da Lista direto no print: " + str(len(lista))) #por ser numero deve transformar em String

#
# CRIANDO UMA LISTA NUMERICA USANDO LIST()
#

lista5 = list(range(1,11)) #pega todos os numeros de 1 á 10
print("\nCriando uma lista de 1 á 10 usando list() e range()")
print(lista5)

#
# PEGANDO O VALOR MAIOR E MENOR VALOR DE UMA LISTA NUMÉRICA
#

lista6 = [1,2,3,4,5,6,7,8,9,10]
minimo = min(lista6)
maximo = max(lista6)
print("\nPegando o Maximo e o Minimo de uma Lista")
print(lista6)
print("Valor Maximo da Lista: " + str(maximo))
print("Valor Minimo da Lista: " + str(minimo))

#
# SOMANDO TODOS OS VALORES DE UMA LISTA NUMÉRICA
# 

soma = sum(lista6)
print("\nSomando todos os valores de uma lista numérica")
print(lista6)
print("Soma de todos os valores: " + str(soma))

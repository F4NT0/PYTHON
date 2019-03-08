# TRABALHANDO COM LISTAS

* As listas permitem armazenar conjuntos de informações em um só lugar
* As listas possuem uma organização em espaços de posição de 0 á quanto for necessário
* Podemos colocar qualquer tipo de informação dentro de uma lista

```python

# 1) CRIANDO LISTAS

# Criando uma lista com valores de 0 á 9
lista = [0,1,2,3,4,5,6,7,8,9]
# Podemos imprimir cada posição na tela
print(lista[0])
print(lista[1])
...

# Criando uma lista com Strings
lista2 = ['nome1','nome2','nome3','nome4']
#podemos imprimir cada posição na tela
print(lista2[0])
print(lista2[1])
...

# 2) ADICIONANDO ELEMENTOS NA LISTA

# Concatenando um novo elemento no fim da lista
lista2 = ['nome1','nome2']
lista2.append('nome3')
# lista fica: lista2 = ['nome1','nome2','nome3']

# 3) RETIRANDO ELEMENTOS DA LISTA

# Com o método pop() podemos retirar elementos da lista
lista2 = ['nome1','nome2','nome3']

# 3.1) RETIRANDO SEMPRE O ULTIMO ELEMENTO
retirando_elemento = lista2.pop()
# lista2 fica: lista2 = ['nome1','nome2']
# podemos imprimir o elemento retirado
print(retirando_elemento)

# 3.2) RETIRANDO QUALQUER ELEMENTO
retirando_primeiro_elemento = lista2.pop(0)
# lista fica: lista2 = ['nome2','nome3']
retirando_segundo_elemento = lista2.pop(1)
# lista fica: lista2 = ['nome3']
# em um vetor e lista a posição começa em zero

# 3.3) REMOVENDO UM ELEMENTO ESPECIFICO
lista3 = ['nome1','nome2','nome3']
lista3.remove('nome1')
# lista fica: lista3 = ['nome2','nome3']

# 4) ORDENANDO UMA LISTA

# 4.1) ORDENANDO DE FORMA DEFINITIVA EM ORDEM ALFABETICA
# usamos o método sort() para ordenar a lista

lista_desordenada = ['b','a','d','c']
lista_desordenada.sort()
# lista fica: lista_desordenada = ['a','b','c','d']

# 4.2) EXIBINDO UMA LISTA EM ORDEM INVERSA
# usamos o metodo reverse() para inverter a lista
lista_reversa = ['d','c','b','a']
lista_reversa.reverse()
# lista fica: lista_reversa = ['a','b','c','d']

# 5) DESCOBRINDO O TAMANHO DA LISTA
# usamos o metodo len(lista) para descobrir o tamanho
lista_tamanho = ['1','2','3','4']
tamanho = len(lista_tamanho)
print(tamanho)
# saida vai ser: 4

# 6) PERCORRENDO A LISTA COM UM LAÇO FOR
# o laço for funciona da seguinte forma:
#     a) colocamos a palavra for no inicio
#     b) criamos uma variavel que ira extrair um elemento da lista
#     c) dizemos de qual lista queremos retirar um elemento
#     d) enquanto existir elementos na lista, ele vai continuar na lista
magicos = ['merlin','gandalf','saruman']
for magico in magicos:
    print(magico)
# se lê: para cada mágico da lista mágicos, imprima o mágico desejado


# 7) TRABALHANDO COM PARTE DE UMA LISTA


# Podemos definir os limites de uma lista com [:]
# Estrutura: lista[PosicaoInicial:PosicaoFinal]
lista = ['1','2','3','4','5']
print(lista[0:3]) # Saída: ['1','2','3']
# se não definir a posição inicial, ele começa do inicio
print(lista[:3]) # Saída: ['1','2','3']
# se não definir a posição final, ele vai até o final
print(lista[0:]) # Saída: ['1','2','3','4','5']
print(lista[3:]) # Saída: ['3','4','5']

# 8) COPIANDO UMA LISTA INTEIRA

# podemos copiar uma lista inteira com o limitador da lista
lista1 = ['1','2','3','4']
lista2 = lista1[:] # ele irá copiar toda a lista para a outra
# não podemos fazer a copia de outra forma
```
# TRABALHANDO COM LISTAS

* As listas permitem armazenar conjuntos de informações em um só lugar
* As listas possuem uma organização em espaços de **posição de 0 á quanto for necessário**
* Podemos colocar **qualquer tipo de informação** dentro de uma lista
* é importante colocar o **nome da lista no plural** para facilitar o trabalho com for

```python

# 1) CRIANDO LISTAS

# Criando uma lista com valores de 0 á 9
numeros = [0,1,2,3,4,5,6,7,8,9]
# Podemos imprimir cada posição na tela
print(numeros[0])
print(numeros[1])
...

# Criando uma lista com Strings
nomes = ['nome1','nome2','nome3','nome4']
#podemos imprimir cada posição na tela
print(nomes[0])
print(nomes[1])
...

# 2) ADICIONANDO ELEMENTOS NA LISTA

# Concatenando um novo elemento no fim da lista
nomes = ['nome1','nome2']
nomes.append('nome3')
# lista fica: lista2 = ['nome1','nome2','nome3']

# 3) RETIRANDO ELEMENTOS DA LISTA

# Com o método pop() podemos retirar elementos da lista
nomes = ['nome1','nome2','nome3']

# 3.1) RETIRANDO SEMPRE O ULTIMO ELEMENTO
retirando_elemento = nomes.pop()
# lista2 fica: lista2 = ['nome1','nome2']
# podemos imprimir o elemento retirado
print(retirando_elemento)

# 3.2) RETIRANDO QUALQUER ELEMENTO
retirando_primeiro_elemento = nomes.pop(0)
# lista fica: lista2 = ['nome2','nome3']
retirando_segundo_elemento = nomes.pop(1)
# lista fica: lista2 = ['nome3']
# em um vetor e lista a posição começa em zero

# 3.3) REMOVENDO UM ELEMENTO ESPECIFICO
nomes_2 = ['nome1','nome2','nome3']
nomes_2.remove('nome1')
# lista fica: lista3 = ['nome2','nome3']

# 4) ORDENANDO UMA LISTA

# 4.1) ORDENANDO DE FORMA DEFINITIVA EM ORDEM ALFABETICA
# usamos o método sort() para ordenar a lista

letras = ['b','a','d','c']
letras.sort()
# lista fica: letras = ['a','b','c','d']

# 4.2) EXIBINDO UMA LISTA EM ORDEM INVERSA
# usamos o metodo reverse() para inverter a lista
letras_reversas = ['d','c','b','a']
letras_reversas.reverse()
# lista fica: letras_reversas = ['a','b','c','d']

# 5) DESCOBRINDO O TAMANHO DA LISTA
# usamos o metodo len(lista) para descobrir o tamanho
numeros_2 = ['1','2','3','4']
tamanho = len(numeros_2)
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
numeros = ['1','2','3','4','5']
print(numeros[0:3]) # Saída: ['1','2','3']
# se não definir a posição inicial, ele começa do inicio
print(numeros[:3]) # Saída: ['1','2','3']
# se não definir a posição final, ele vai até o final
print(numeros[0:]) # Saída: ['1','2','3','4','5']
print(numeros[3:]) # Saída: ['3','4','5']

# 8) COPIANDO UMA LISTA INTEIRA

# podemos copiar uma lista inteira com o limitador da lista
numeros = ['1','2','3','4']
numeros_2 = numeros[:] # ele irá copiar toda a lista para a outra
# não podemos fazer a copia de outra forma
```
# Entendendo Listas em Python

Lista é uma estrutura de dados que nos permitem armazenar conjuntos de dados em um só lugar, sendo esses dados do mesmo tipo.

---

## Construindo uma Lista

Podemos construir uma Lista manualmente, onde colocamos os dados entre colchetes **[** e **]** em uma variável.

Ex: 

```python
lista = ['A','B','C','D']
```

Podemos também construir uma variável lista vazia, para adicionarmos depois os itens

```python
lista = []
```

---

## Imprimindo uma Lista Completa

Sem utilizar o <code style="color: cyan">For</code>,<code style="color: green">While</code> podemos imprimir uma lista em forma de lista pelo terminal, com a Função **print()**

```python
print(lista)

# Saida: ['A','B','C','D']
```

---

## Imprimindo valores da Lista

Podemos pegar somente um valor de uma lista, onde as posições começam por **0**

Podemos pegar um valor e adicionarmos em uma Variável ou imprimir ela no terminal

```python
lista = ['A','B','C','D']

# Pegando valor da primeira posição
primeira_posicao = lista[0] # A

# Imprimindo valor da segunda posição
print(lista[1]) # B
```

Se colocarmos valores negativos, iremos começar a pegar os valores do final da Lista

```python
lista = ['A','B','C','D']

# Pegando o valor da ultima posição
ultima_posicao = lista[-1]

# Imprimindo o valor da penultima posição
print(lista[-2])
```

---

## Adicionando valores em uma Lista

Podemos adicionar valores de diferentes formas

1) Adicionando no final da lista

Utilizamos a Função **append(value)** para adicionar um valor no final da lista:

```python
lista = ['A','B','C','D']

lista.append('E')

print(lista)
#Saida: ['A','B','C','D','E']
```

2) Adicionando em uma posição específica da lista

Utilizamos a Função **insert(pos,value)** para adicionarmos um valor em uma posição específica

```python
lista = ['A','B','C','D']

lista.insert(1,'B1')

print(lista)
#Saida: ['A','B1','C','D']
```

---

## Retirando valores de uma Lista

Podemos retirar valores de 3 formas de uma Lista

1) Removendo o ultimo valor da Lista

Com a Função **pop()** podemos remover o ultimo valor da lista, onde podemos salvar ele em uma variável

```python
lista = [1,2,3,4]

ultimo_valor = lista.pop()

print(ultimo_valor) # Saida: 4
print(lista) # Saida: [1,2,3]
```

2) Removendo um valor pela sua posição na Lista

Com a Função **pop()** passando como atributo o valor da posição que deseja remover podemos retirar o valor dessa posição específica:

```python
lista = [1,2,3,4]

valor_retirado = lista.pop(1)
print(valor_retirado) #Saida: 2

print(lista)
#Saida: [1,3,4]
```

3) Removendo procurando por um valor

Utilizando a Função **remove()** passamos como Atributo o valor específico que queremos retirar

```python
lista = [1,2,3,4,5]

lista.remove(2)

print(lista)
#Saida: [1,3,4,5]
```
Retirando com **remove()** não se consegue guardar o valor retirado

---

## Ordenando uma Lista de forma Permanente

Existem algumas Funções que podem nos ajudar a ordenar a Lista de forma alfabética

1) Ordenar permanentemente uma lista em ordem alfabética e crescente usando a Função **sort()**

```python
lista = ['B','D','A','C']

lista.sort()

print(lista)
#Saida: ['A','B','C','D']
```

2) Essa ordenação usando **sort()** funciona também com números

```python
lista = [3,2,1,4]

lista.sort()

print(lista)
#Saida: [1,2,3,4]
```

3) Ordenar de forma decrescente usando como Atributo **reverse = True** na Função **sort()**

```python
lista = [1,2,3,4]

lista.sort(reverse = True)

print(lista)
#Saida: [4,3,2,1]
```

4) Invertendo a Lista utilizado a função **reverse()**

```python
lista = [1,2,3,4]

lista.reverse()

print(lista)
#Saida: [4,3,2,1]
```

---

## Ordenando de forma temporária uma Lista

Podemos usar a Função **sorted()** para alterar a lista de forma temporária

```python
lista = [1,2,3,4]

print(sorted(lista)) # Saida: [4,3,2,1]
print(lista) #Saida: [1,2,3,4]
```

---

## Pegando o tamanho da Lista

Podemos pegar ou testar o tamanho da lista utilizando a Função **len()**

o **len()** vai pegar o numero de itens, não o número de posições

Se deseja transmitir o valor no **print()**, deve-se transformar em String usando **str()**

```python
lista = [0,1,2,3]

tamanho = len(lista)

print(str(tamanho)) #Saida: 4
print(str(len(lista))) #Saida: 4
``` 

---

## Saidas de exemplo

Temos o seguinte código de exemplo completo dessas Funções e interações com as Listas

```python
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
```

Esse código vai ter as Seguinte informações no Terminal, usando python 3:

```text
['A', 'B', 'C', 'D']
Primeiro valor da Lista: A
Ultimo valor da Lista: D

Ultimo valor da Lista após o append(): E
['A', 'B', 'C', 'D', 'E']

Primeiro valor da Lista2 usado o insert(): A
['A']

Valor Retirado do final da Lista: E
['A', 'B', 'C', 'D']

Valor Retirado da Posição 2: C
['A', 'B', 'D']

Usado o remove() para retirar o valor A
['B', 'D']

Ordenado permanentemente a lista de forma alfabetica e crescente
['A', 'B', 'C', 'D']

Ordenando permanentemente a lista de forma numerica e crescente
[1, 2, 3, 4]

Ordenando permanentemente a lista de forma decrescente
[4, 3, 2, 1]

Reordenando de forma inversa a Lista anterior
[1, 2, 3, 4]

Ordenando de forma temporária sem mexer na lista original
['A', 'B', 'C', 'D']
Original: 
['B', 'C', 'A', 'D']

Pegando o tamanho da Lista
['A', 'B', 'C', 'D']
Tamanho da Lista armazenada em variavel: 4
Tamanho da Lista direto no print: 4
```
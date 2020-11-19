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

## Criando uma lista por um grupo de numeros

Podemos criar uma lista utilizando a Função **list()**, onde podemos colocar dela uma Função chamada **range()** que vai possuir um valor inicial e um valor final + 1.

Se quisermos construir uma Lista de valores de 1 á 10, criamos uma Função **range()** que vai de 1 á 11(10+1):

```python
lista = list(range(1,11))
print(lista)
#Saida: [1,2,3,4,5,6,7,8,9,10]
```

---

## Maximo e o Mínimo de uma lista

Usamos as funções **max()** e **min()** em listas numéricas para podermos pegar o maior e o menor valor da lista

```python
lista6 = [1,2,3,4,5,6,7,8,9,10]
minimo = min(lista6)
maximo = max(lista6)
print("Valor Maximo da Lista: " + str(maximo))
print("Valor Minimo da Lista: " + str(minimo))
```

A saída tem que sair usando a Função **str()** porque é um valor numérico.

---

## Somando todos os valores de uma lista

Usamos a Função **sum()** para somar todos os valores numéricos de uma lista numérica

```python
soma = sum(lista6)
print("\nSomando todos os valores de uma lista numérica")
print(lista6)
print("Soma de todos os valores: " + str(soma))
```
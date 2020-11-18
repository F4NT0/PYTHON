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

Com a Função **pop()** passando como atributo o valor da posição que deseja remover podemos 

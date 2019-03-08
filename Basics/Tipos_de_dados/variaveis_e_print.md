# Arquivo de informações rápidas sobe python

* colocar uma "#" faz com que toda a linha vire um comentário
* print() serve para imprimir uma mensagem na tela
 ```python
# esta linha é um comentário
print('Esta é uma forma de imprimir informação')
print("Esta tambem é uma forma de imprimir informação")
 ```

* Esta é uma forma de apresentar variáveis em Python

```python
nome = "F4NT0"
print(nome) # vai sair a informação armazenada na variável
nome_complexo = 'F4NT0 D3V'
print(nome_complexo) # imprime o nome complexo como na primeira variavel
```

### Números armazenados em Variáveis
```python

# Números inteiros
inteiro = 3

# Números Flutuantes
flutuante = 2.5

# Cálculos com os números
divisao = 4 / 2 # na variavel será armazenada o numero 2
divisao_float = 5 / 3 # sera armazenado um valor em float
multiplicação = 2 * 4 # na variavel será armazenado o numero 8
soma = 2 + 2 # na variavel será armazenado o numero 4
subtracao = 2 - 2 # na variavel será armazenado o numero 0

# Calculos usando o print()
print(2+2) # ira imprimir o resultado da soma
print(divisao + 3) # irá pegar o valor da divisao armazenada e adicionar 3


# mudando o tipo da variavel
# para mudar o tipo da variavel só altere o valor dela
numero = 3
print(numero)
numero = 3.5
print(numero)

# Exponencial
# para fazer uma exponenciação, usamos **
exp = 2 ** 2 # o resultado é 4, por ser 2 elevado na 2


# Modulo
# Modulo serve para poder conseguir o resto de uma divisão
resto = 4 % 2  # o valor va variavel será zero, porque não tem resto
resto_segundo = 5 % 3 # o valor da variavel será 1 devido que sobra 1 da divisão
```

### Trabalhando com Strings

```python
# Concatenação de Strings
# usando o + podemos concatenar strings, mas elas se tornam juntas
nome = 'gabriel'
sobrenome = 'fanto'
tudo_junto = nome + sobrenome # fica gabrielfanto

tudo_junto_arrumado = nome + " " + sobrenome # fica gabriel fanto
print(tudo_junto)
print(tudo_junto_arrumado)

# usando a função str() podemos colocar numero dentro de uma string
string1 = 'mellhor de ' 
numero = 3
tudo_junto = string1 + str(numero)

# podemos colocar tudo junto usando virgulas no print
print(string1,numero) # saida: 'melhor de 3'


# atualizando um valor
# forma de atualização comum:
numero = 2
numero = numero + 2 # atualiza o valor do numero para quatro

# podemos colocar espaços e novas linhas
print("\tPython") #coloca um tab no texto
print("\nPython") #colocao texto numa nova linha
```

### Tipo de Dado Booleano
* Booleano é sempre `True` ou `False`
```python
# CRIANDO VARIAVEL BOOLEANA
valor = True
valor_2 = False

# Podemos usar os valores booleanos para teste condicionais
# Para mais informações, visite á págin sobre if/else
```

## Criando Funções em Python

* `Funções` são blocos de códigos nomeados,criados para fazer uma tarefa especifica
* Quando precisamos executar uma tarefa em particular, onde temos uma função para isso, chamamos o nome da função responsável por ela
* Já utilizamos funções nas outras partes deste repositório, como: 
    * `str()` : transforma um numero em string
    * `print()` : envia uma mensagem de output
    * `int() e float()`: transforma String em inteiro/flutuante
    * `input()` : recebe um dado externo e armazena
* utilizamos várias funções em programação, agora iremos aprender a construir e utilizar nossas proprias funções

### Definindo uma função

* começamos uma função com a palavra reservada `def`
    * **def** informa ao python que o que vier depois é uma função
* após o def, definimos o `nome` de nossa função e seus `atributos` dentro de parenteses obrigatórios
    * as funções **podem ter atributos ou não**
    * Podemos colocar quantos atributos queremos em uma função
    * Podemos definir um `atributo default`, ou seja,podemos definir um valor especifico eternamente
    * **`Atributos`** são informações que o usuario ira colocar na função,pode ser uma variavel ou um valor direto
* tudo que vier dentro da identação da função faz parte da função, como nos exemplos abaixo

```python
# FUNÇÃO SEM ATRIBUTOS
def nome_funcao():
    info

# FUNÇÃO COM ATRIBUTOS
def nome_funcao(atributo):
    info

def nome_funcao(atributo_1,atributo_2):
    info

# FUNÇÃO COM ATRIBUTO DEFAULT
def nome_funcao(atributo=valor):
    info
```

### Colocando texto Docstring nas funções

* `Docstring` é um texto curto para dizer para que serve a função, para que quando for criado a documentação da `classe de funções` possa se saber o que ela faz
* Docstrings são definidas com **3 aspas duplas de cada lado**

```python
def nome_funcao(atributo):
    """Função de teste com Docstring."""
```

### Parâmetro e Argumento

* Tem duas coisas que precisamos saber primeiro, o que é `Parâmetro` e o que é `Argumento`:
    * **`Parâmetro`** é quando chamamos o nome de uma função para utilizarmos a função
    * **`Argumento`** é quando chamamos uma variavel ou valor em um atributo 
* Entendo essas duas coisas podemos trabalhar com as Funções

```python
# Exemplo de Função
def get_nome(nome):
    print(nome)

# Exemplo de Utilização
get_nome('Gabriel') 
# PARAMETRO: get_nome()
# ARGUMENTO: 'Gabriel'
```

### Tipos de Argumentos

* Existem duas formas de Definir argumentos:
    * 1) **`Argumento Posicional`** : é uma forma de definir os argumentos, colocando seus valores na chamada de parâmetro mesmo, sem a utilização de variáveis
    * 2) **`Argumento Nomeado`** : podemos fazer de duas formas esse argumento, podemos criar a variavel externamente ou internamente no Parâmetro
        * Se for feito **Externamente** não importa o nome que dermos para a variavel
        * Se for **Internamente** deve ser dito exatamente qual **atributo estamos argumentando**
```python
# Função
def bicho(nome_bicho,tipo_bicho):
    print('O nome do bicho e ',nome_bicho,' e ele é um(a) ',tipo_bicho)

# ARGUMENTO POSICIONAL
bicho('Bili','Cachorro')

# ARGUMENTO NOMEADO 1
bicho(nome_bicho = 'Bili',tipo_bicho = 'Cachorro')

# ARGUMENTO NOMEADO 2
nome = 'Bili'
tipo = 'Cachorro'
bicho(nome,tipo)

```

### Chamando Funções

* Como explicado acima, `chamar uma função é dar um parametro e um argumento`
* Podemos chamar uma função quantas vezes quisermos 
* Podemos armazenar a saida da função em uma variavel

```python
# CRIANDO DUAS FUNÇÕES
def dando_nome(nome):
    print('Seu nome agora e ',nome)

def soma(valor_1,valor_2):
    soma = valor_1 + valor_2
    return soma

# CHAMANDO AS FUNÇÕES

# Chamando quantas vezes quisermos
dando_nome('Billi')
dando_nome('Leopoldo')
dando_nome('Charlie')

# Armazenando o resultado em variavel

valor = soma(2,3) # valor = 5
valor_2 = soma(5,5) # valor_2 = 10 
```

### Palavra reservada return

* **`return`** serve para podermos definir qual será a Saída de uma função, ou seja, o que ela retorna para o que desejamos
* podemos criar funções com Saídas usando `print()` ou `return`

```python

# SAIDA COM RETURN
def soma(valor_1,valor_2):
    saida = valor_1 + valor_2
    return saida # vai retornar o valor 

# SAIDA COM PRINT()
def nome(nome):
    print(nome) # saida vai ser o nome entrado

# CHAMADAS DE CADA UMA DELAS

# como a função tem return, armazenamos o valor de saida
valor = soma(1,1)

# com a funcao de nome é print(), somente chamamos

nome('Gabriel')
```

### Passando um numero arbitrário de argumentos

* Tem vezes que não sabemos quantos argumentos podemos ter em uma função, por isso podemos construir um `argumento arbitrário` que cria uma tupla vazia que ira aceitar quantos argumentos forem necessários
    * Dizemos que um argumento é arbitrario quando colocamos um asterisco(*) antes do nome do argumento
* Com isso podemos criar uma lista de valores que serão armazenadas na tupla e depois podem ser pegas

```python

# CRIANDO UMA FUNÇÃO COM ARGUMENTO ARBITRARIO
def lista_compras(*produtos):
    """ Serve para criar uma lista de compras."""
    for produto in produtos:
        print(produto)

# Chamando a função

lista_compras('Cebola','Alface','Pepino')
lista_compras('Queijo','Presunto')
lista_compras('Banana')

```
### Trabalhando com Módulos

* `Módulo` é um arquivo separado onde ficam as funções que desejam
* Sempre definimos as funções com nomes descritivos para facilitar
* Após definidos as funções e criado o Módulo que as armazenam, `importamos` o módulo nos programas que desenvolvemos.
* **Usar Módulos facilita a reutilização de funções em vários programas**
* Módulos devem ficar no mesmo Diretório que o arquivo do programa a ser desenvolvido
* `Import` é a forma de transmitir as funções do Módulo no arquivo que desejamos desenvolver, assim deixamos o código limpo para poder trabalhar, o sistema de import funciona da seguinte forma:
    * `import nomeModulo`: nomeModulo é o nome do arquivo que é o módulo
    * `nomeModulo.nomeFuncao()`: quando queremos chamar uma função do arquivo de Módulo, dizemos qual módulo e o nome da função como mostrado.

**EXEMPLO:**

1. _ARQUIVO QUE É O MÓDULO_

Nome do arquivo: calculadora.py
```python

def nome():
    print('Bem vindo ao Módulo de Calculadora! ')

def soma(valor_1,valor_2):
    """ Função para fazer uma soma."""
    soma = valor_1 + valor_2
    return soma

def sub(valor_1,valor_2):
    """ Função para fazer uma subtração."""
    sub = valor_1 - valor_2
    return sub

def multi(valor_1,valor_2):
    """ Função para fazer uma multiplicação."""
    multi = valor_1 * valor_2
    return multi

def div(valor_1,valor_2):
    """ Função para fazer uma divisão."""
    if valor_1 < valor_2:
        div = valor_2 / valor_1
        return div
    elif valor_1 > valor_2:
        div = valor_1 / valor_2
        return div
    else:
        div = valor_1 / valor_2
        return div

def pot(base,expoente):
    """ Função para fazer uma exponenciação."""
    pot = base ** expoente
    return pot
```

2. _ARQUIVO PRINCIPAL_

* Arquivo no qual vai ser usado o Módulo
* Este arquivo deve estar dentro do Diretório do Módulo

**OBS:** se as funções tem return, devem ser armazenados em uma variavel, senão somente chama a função

```python

import calculadora # Fazendo um import 

calculadora.nome() # chamada de uma função com print

valor_1 = input('Digite o primeiro valor: ')
valor_2 = input('Digite o segundo valor: ')

# Transformando os valores de entrada em inteiros

valor_1 = int(valor_1)
valor_2 = int(valor_2)

soma = calculadora.soma(valor_1,valor_2) # chamada de uma função com return
print('Soma dos dois valores: ',soma)
```






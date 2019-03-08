# Instruções if/else

if/else é uma instrução que permite verificar qualquer condição, onde ele ele faz uma avaliação booleana (true ou false) chamada de **teste condicional**

Se o resultado do teste condicional for **True**, ele entra na instrução do `if`

Se o resultado do teste condicional for **False**, ele entra na instrução do `else`

Os **testes condicionais** que se usa em Python são:
* **Igualdade**
  * o simbolo para igualdade é `==`
  * o teste retorna true se as duas informações forem iguais
* **Diferença**
  * o simbolo para diferenca é `!=`
  * o teste retorna true se as duas informações forem diferentes
* **Comparações**
  * existem 5 tipos de comparações
    * IGUAL: funciona como a igualdade, o simbolo é `==`
    * MENOR: verifica se o valor é menor que o outro, simbolo: `<`
    * MAIOR: verifica se o valor é maior que o outro, simbolo: `>`
    * MENOR OU IGUAL: simbolo: `<=`
    * MAIOR OU IGUAL: simbolo: `>=`

Podemos testar várias condições ao mesmo tempo utiizamos as seguintes palavras reservadas:
    * Multiplos testes com `and`: **and** testa para que todos os testes das variaveis ou valores deem verdadeiro ou falso como na tabela lógica
    * Multiplos testes com `or`: **or** teste para que pelo menos uma das variaveis ou valores sejam True para poder ser True

### EXEMPLO DE TESTES CONDICIONAIS

```python

# IGUALDADE

3 == 3 # True
4 == 3 # False

# DIFERENÇA

3 != 4 # True
4 != 4 # False

# COMPARAÇÕES

a = 3
b = 4

a < b # True
a > b # False

a <= b # True
a >= b # False

# TESTE DE VÁRIAS CONDIÇÕES
a = 1
b = 2
c = 1
d = 3

a >= c # True
b == d # False
d > a  # True
a > b  # False


# TESTE DO AND

b == d and a > b  # False and False = False
a >= c and b == d # True  and False = False
a > b and d > a   # False and True  = False
a >= c and d > a  # True  and True  = True

# TESTE DO OR

b == d or a > b   # False or False = False
a >= c or b == d  # True  or False = True
a > b  or d > a   # False or True  = True
a >= c or d > a   # True  or True  = True   
```
### Verificando elementos em uma lista

Podemos verificar elementos de uma lista no if/else tambem

**Verificando se está na lista:**
* usamos a palavra reservada `in` para ver se existe o elemento
```python
# PRIMEIRA FORMA
lista = ['Gabriel','Pedro','Igor']

'Gabriel' in lista  # True
'Fulano'  in lista  # False

lista2 = [1,2,3,4]

1 in lista2  # True
6 in lista2  # False

# SEGUNDA FORMA
lista = ['Gabriel','Pedro','Igor']
variavel_1 = 'Gabriel'
variavel_2 = 'Fulano'

variavel_1 in lista # True
variavel_2 in lista # False

lista2 = [1,2,3,4]
variavel_1 = 1
variavel_2 = 6

variavel_1 in lista2 # True
variavel_2 in lista2 # False
```
**Verificando se não está na lista:**
* usamos a palavra reservada `not in` para ver se não existe o elemento
```python
# PRIMEIRA FORMA
lista = ['Gabriel','Pedro','Igor']

'Gabriel' not in lista  # False
'Fulano'  not in lista  # True

lista2 = [1,2,3,4]

1 not in lista2  # False
6 not in lista2  # True

# SEGUNDA FORMA
lista = ['Gabriel','Pedro','Igor']
variavel_1 = 'Gabriel'
variavel_2 = 'Fulano'

variavel_1 not in lista # False
variavel_2 not in lista # True

lista2 = [1,2,3,4]
variavel_1 = 1
variavel_2 = 6

variavel_1 not in lista2 # False
variavel_2 not in lista2 # True

```

### Usando variaveis booleanas 

* Podemos usar uma variavel booleana e depois alterar seu valor dentro de uma instrução if/else
```python
# Exemplo de Variaveis booleanas
valor  = True
valor_1 = False

# Podemos mudar o valor delas dentro de um if/else
```

## CONSTRUÇÃO DE UMA INSTRUÇÃO IF/ELSE

Existem algumas formas de fazer essas instruções:

**INSTRUÇÃO DE IF UNICO**
* podemos somente ter uma instrução if ou vários if juntos, usando cada um dos testes condicionais
```python
# CONSTRUÇÃO DE UM IF NORMAL VAZIO

if condicao:
    pass
# quando é criado uma instrução vazia usamos pass

# USANDO IF COM CADA CONDIÇÃO VISTA

# IGUALDADE

if 3 == 3: # este if é iniciado porque deu True o teste
    print(3) # imprime na tela o numero

if 3 == 4: # este if NÃO É INICIADO(deu false o teste)
    print(3) # NÃO IMPRIME 

# DIFERENÇA

if 3 != 4: # este if é iniciado porque deu True o teste
    print(3)

if 3 != 3: # este if NÃO É INICIADO(deu false o teste)
    print(3) # NÃO IMPRIME 

# COMPARAÇÃO

a = 3
b = 4

if a < b:  # True, if iniciado
if a > b:  # False, if não iniciado

if a <= b: # True, if iniciado
if a >= b: # False, if não iniciado

# MULTIPLOS TESTES

if a < b and a <= b: # TRUE AND TRUE  = TRUE
if a > b and a <= b: # FALSE AND TRUE = FALSE
if     


```

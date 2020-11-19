# IF-ELSE em python

---

## Teste condicionais

Testes condicionais servem para fazer uma verificação e entregarem como resultado um valor Booleano

Tipos de valores booleanos possiveis:

```python
True #primeira letra maiuscula
False #segunda letra maiuscula
```

Tipos de Condicionais:

```python
== # Verifica igualdade
!= # Verifica a diferença
> # Verifica se é maior
< # Verifica se é menor
>= # Verifica se é maior ou igual
<= # verifica se é menor ou igual
```

Quando testamos mais de uma condicional de uma vez:

```python
and # Se as duas condições forem True, será True
or # Se uma das condições é True, será True
```

Verificando se um valor existe em uma Lista:

```python
in # verifica se o valor existe na lista
not in #verfica se o valor não existe na lista
```

---

## IF simples

IF simples é somente a estrutura do if, sem um else incluido

um IF somente vai acontecer se o resultado do Teste condicional for **True**

Estrutura do if:

```python
if teste_condicional:
    faça algo
```

Exemplo:

```python
age = 29

if age > 18:
    print("Maior de Idade")
```

---

## IF-ELSE normal

Se der **False** um teste condicional, podemos fazer com que o ELSE lide com essa condição

Estrutura de um IF-ELSE:

```python
if teste_condicional:
    faz algo
else:
    faz outra coisa
```

Exemplo de utilização de um IF-ELSE:

```python
age = 7

if age > 18:
    print("Maior que 18 anos")
else:
    print("Menor que 18 anos")
```

---

## ELIF

utilizamos o ELIF quando queremos lidar com muito mais opções do que somente duas, onde podemos colocar quantos ELIF quisermos

Exemplo de um ELIF:

```python
age = 7

if age > 18:
    print("Maior que 18 anos")
elif age == 7:
    print("Idade é igual a 7")
else: 
    print("Menor de 18 anos")
```


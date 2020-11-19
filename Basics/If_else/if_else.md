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

---

## Exemplos

1) Pegando dados por **Input** e fazendo a verificação completa:

```python
# entrada de texto para testar
valor1 = input('Entre o primeiro valor para teste: ')
# toda entrada entra como string, vamos definir como inteiro
valor1 = int(valor1)

valor2 = input('Entre o segundo valor para teste: ')
valor2 = int(valor2)

if valor1 > valor2:
    print('Primeiro valor é maior!')
elif valor1 < valor2:
    print('Primeiro valor é menor!')
else:
    print('Os dois valores são iguais')
```

2) Lendo uma Lista e verificando se o nome existe nela

```python
nomes = ['Gabriel','Pedro','Vini','Dodo']
meu_nome = input('Seu nome e? ')
contador = 0 # para finalizar a passagem dentro do for
for nome in nomes:
    if meu_nome in nome: # se tiver o nome na lista
         print('meu nome esta na lista!')
         break # finaliza o for
    elif contador == 3 and meu_nome not in nome: # se não tiver
         print('Nao estou na lista!')
    else:
         pass
    contador += 1
# Quando o contador chega no tamanho da lista, testa o elif
```
---



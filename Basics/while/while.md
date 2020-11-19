# While em Python

---

##  Loop infinito

Loop infinito é quando um While não finaliza, onde isso pode ser proposital ou um problema

Um exemplo de Loop inifinito:

```python
while True:
    print("Loop Infinito")
```

---

## Testes Condicionais

Assim como no IF, utilizamos os testes condicionais

```python
> # Valor maior que outro
< # Valor menor que outro
>= # Valor maior ou igual que outro
<= # Valor menor ou igual que outro
== # Valor igual que outro
```

No **While** ele só continua enquanto o teste condicional for **True**, quando der **False** a condicional o While para.

Exemplo: Somar um valor até ele chegar em um valor limite

```python
base = 0

while base < 10:
    base = base + 1

print(base) #Saida: 10
```

Nesse While, ele vai fazendo o while enquanto o valor da variável base for menor que 10, quando chega em 10 ele para

---

## Transformando um valor decimal em binário

Podemos utilizar o While para fazer divisões consecutivas por 2 e salvar os restos em uma Lista

Essa lista vai ter somente 0 e 1 que em sua ordem é o Binário do número

```python
decimal = 10
binario = []

while decimal > 0:
    binario.append(decimal%2)
    decimal  = int(decimal/2)
print(binario) #Saida: [0,1,0,1]
```

1. Enquanto o valor do decimal que queremos transformar em binário é maior que zero, o resto da divisão (decimal%2) vai ser salvo na lista binario
2. Depois de salvo o valor original do decimal é dividido por 2, onde devemos ter que usar a Função **int()** para fazer com que a divisão seja um valor inteiro
3. Assim, no final, a lista binario é o nosso binário oficial

## Transformando o valor binário em decimal

Se quisermos fazer o contrário, podemos utilizar o For para pegarmos os valores da lista e calcularmos de volta em decimal

```python
binario = [0,1,0,1]
novo_decimal = 0
for i in range(len(binario)):
    if binario[i] == 1:
        novo_decimal = novo_decimal + 2**i
print(novo_decimal)
```

1. Pegamos o tamanho da nossa lista (_len(binario)_) e iremos fazer com que o valor do _i_ ande até o limite do binário (no nosso caso vai até 3)
2. Se o valor na posição da lista binário for **1**, essa posição vai ser pegar como expoente e será feito potenciação com a base 2, como abaixo:
   1. 2^pos
3. Essa potenciação vai ser salvo junto com o valor já armazenado dentro da variável *novo_decimal*
4. A variável *novo_decimal* após o final do For vai ter o valor em Decimal da lista binario

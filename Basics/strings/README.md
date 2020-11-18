# Mexendo com Strings em Python

---

### Criando uma String

Strings podem ser utilizando aspas simples(**'**) ou aspas duplas(**"**).

```python
"mensagem"
```

```python
'mensagem'
```

---

### Pegando uma parte da String

Pegar uma parte da String se chama Substring.

Strings são vetores de Characteres, por isso podemos definir qual o tamanho de caracteres que desejamos.

A estrutura para pegarmos uma Substring: **char inicial:char final + 1**:

* Character inicial e Character final

```python
nome = "Gabriel Fanto"

# pegar somente o primeiro nome
# ['G','a','b','r','i','e','l']
# posições no String original: [0,1,2,3,4,5,6]
# por isso o tamanho vai de 0 até 7 (pos 6 + 1)

primeiro_nome = nome[0:7]
print(primeiro_nome)

# Saida: Gabriel
```

* Character até o limite final

Podemos somente definir até qual character que desejamos, como no exemplo acima é até a posição 6 + 1:

```python
nome = "Gabriel Fanto"

primeiro_nome = nome[:7]
print(primeiro_nome)

# Saida: Gabriel
```

* Character de um limite incial até o fim

Se queremos pegar o sobrenome, podemos dizer somente a posição inicial e pegar todo o resto:

```python
nome = "Gabriel Fanto"

sobrenome = nome[7:]
print(sobrenome)

# Saida: Fanto
```

---

# Definindo uma String como Título

Podemos fazer com que as primeiras letras de cada String como maiusculas.

Usamos a Função **title()** para colocar as primeiras letras maiusculas

```python
nome = "gabriel fanto"

titulo = nome.title()

print(titulo)

# Saida: Gabriel Fanto
```

---

# Colocando todas as letras em maiusculas

Usamos a Função **upper()** para colocar todas as letras em maiusculas.

```python
palavra = "alfabeto"

maiusculo = palavra.upper()

print(maiusculo)

# Saida: ALFABETO
```

---

# Colocando todas as letras em minusculas

Usamos a Função **lower()** para colocar todas as letras em minusculas.

```python
palavra = "ALFABETO"

minusculo = palavra.lower()

print(minusculo)

# Saida: alfabeto
```

---

# Retirando os espaços em branco da String

Usamos a Função **strip()** para retirar qualquer espaço em branco de uma String.

Existe o **lstring()** que retira da Esquerda e **rstring()** da Direita.

```python
palavra = "pessoal tecnico"

nova_string = palavra.strip()

print(nova_string)

# Saida: "pessoaltecnico"
```

---

# Dividindo uma String em várias

Podemos dividir uma String em varias Strings.

Com a Função **split(string)** podemos definir que cada String de cada lado de uma String definida seja uma String separada dentro de um vetor.

Vamos por exemplo criar uma String que cada palavra é dividida por **:**

```python
palavras = "Gabriel:Fanto:Stundner"
```

Agora podemos dividir em um Vetor cada uma das palavras entre os **:**

```python
palavras = "Gabriel:Fanto:Stundner"

print(palavras.split(":"))

# Saida: ['Gabriel','Fanto','Stundner']
```

Como a palavra virou um Vetor, podemos pegar as posições deles e utilizar eles:

```python
palavras = "Gabriel:Fanto:Stundner"

vetor = palavras.split(":")

primeiro_nome = vetor[0]
segundo_nome = vetor[1]
terceiro_nome = vetor[2]

print(primeiro_nome)
print(segundo_nome)
print(terceiro_nome)

# Saida:
# Gabriel
# Fanto
# Stundner
```
---
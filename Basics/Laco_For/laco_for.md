# For em Python

---

## Usando For em uma Lista

Utilizamos o For para andarmos dentro de uma Lista e pegarmos individualmente os dados internos.

Assim como vimos no IF, usamos alguns testes condicionais para verificarmos:

```python
in # Verificar se o elemento está dentro da Lista
not in # Verificar se o elemento NÃO está dentro da Lista
```

Com esse teste condicional, podemos andar por toda a Lista e imprimir os dados, como abaixo:

```python
caracteres = ['a','b','c','d']

for caracter in caracteres:
    print("Letra: " + caracter)
```

No exemplo acima, sempre que tiver um **caracter** na lista de **caracteres** podemos pegar esse dado e imprimir

Podemos agora modificar nossa Lista como quisermos:

1) Removendo um item específico da Lista

```python
lista1 = ["Pepe","A","B","Pepe","C"]

for item in lista1:
    if "Pepe" in lista1:
        lista1.remove("Pepe")
print(lista1)
# Saida: ["A","B","C"]
```
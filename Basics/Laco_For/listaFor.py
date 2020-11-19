# -----------------------------
# Modificando uma Lista com For
# -----------------------------

# Removendo um Item específico

lista1 = ["Pepe","A","B","Pepe","C"]

for item in lista1:
    if "Pepe" in lista1:
        lista1.remove("Pepe")
print(lista1)

# Pegando somente os Números Pares

lista2 = [1,2,3,4,5,6]
listaNumber = []

for number in lista2:
    if number%2 == 0:
        listaNumber.append(number)
print(listaNumber)

# Pegando somente os Números Impares

lista3 = [1,2,3,4,5,6]
listaNumber2 = []

for number in lista3:
    if number%2 != 0:
        listaNumber2.append(number)
print(listaNumber2)

# Criando uma lista de Números em um intervalo de 1 á 10

lista4 = []

for number in range(1,11):
    lista4.append(number)
print(lista4)

# Criando uma lista de somente pares de um intervalo de 1 á 10

lista5 = []

for number in range(1,11):
    if number%2 == 0:
        lista5.append(number)
print(lista5)

# Criando uma lista de somente impares de um intervalo de 1 á 10

lista6 = []

for number in range(1,11):
    if number%2 != 0:
        lista6.append(number)
print(lista6)
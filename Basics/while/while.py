# ---------------
# TESTE DE WHILE
# ---------------

# Loop infinito

# while True:
#     print("Loop Infinito")

# Somando até chegar em um valor específico
value = 0

while value < 10:
    value = value + 1
print(value)

# Transformando Decimal em Binário

decimal = 10
binario = []

while decimal > 0:
    binario.append(decimal%2)
    decimal  = int(decimal/2)
print(binario)

# Transformando Binário para Decimal

novo_decimal = 0
for i in range(len(binario)):
    if binario[i] == 1:
        novo_decimal = novo_decimal + 2**i
print(novo_decimal)

# 

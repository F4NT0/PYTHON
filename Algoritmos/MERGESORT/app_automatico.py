# app de teste e criação de um arquivo com valores automaticos

# IMPORTS
import random
import time
import mergesort

# VARIAVEIS
lista = []
loop = True
incrementador = 1

while loop:
    valor = 10*incrementador
    for i in range(valor):
        lista.append(random.randint(0,valor))

    inicio = time.time()
    mergesort.mergeSort(lista)
    fim = time.time()
    
    tempo_final = int((fim-inicio)*1000000)

    arquivo = open('mergesort.txt', 'a')
    texto = str(valor) + ' ' + str(tempo_final) + '\n'
    arquivo.write(texto) 
    arquivo.close()

    incrementador += 1

    if valor == 1000:
        break
    else:
        continue



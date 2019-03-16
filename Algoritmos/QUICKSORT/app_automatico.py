# app de teste e criação de um arquivo com valores automaticos

# IMPORTS
import random
import time
import quicksort

# VARIAVEIS
lista = []
loop = True
incrementador = 1

while loop:
    valor = 10*incrementador
    for i in range(valor):
        lista.append(random.randint(0,valor))

    inicio = time.time()
    quicksort.quicksort(lista,0,valor) # quicksort(lista,pos_inicio,pos_fim)
    fim = time.time()
    
    tempo_final = int((fim-inicio)*1000000)

    arquivo = open('quicksort.txt', 'a')
    texto = str(valor) + ' ' + str(tempo_final) + '\n'
    arquivo.write(texto) 
    arquivo.close()

    incrementador += 1

    if valor == 10000:
        break
    else:
        continue

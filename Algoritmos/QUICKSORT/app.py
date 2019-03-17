# Algoritmo do QuickSort

# IMPORTS

import random # cria numeros aleatorios
import time # calcula o tempo
import quicksort

# VARIAVEIS
lista = []
loop = True


# LOOP
while loop:

    # 1) Criação de uma lista de valores aleatorios

    valor_maximo = input('Numero Inteiro: ')    
    valor_maximo = int(valor_maximo)

    for i in range(valor_maximo):
        lista.append(random.randint(0,valor_maximo)) #random.randomint(minimo,maximo) cria valores aleatorios inteiros


    # 2) calculando o tempo

    inicio = time.time() # tempo de inicio do quicksort
    quicksort.quickSort(lista,0,len(lista)-1) # quicksort(lista,posicaoInicial,posicaoFinal)
    fim = time.time() # tempo final do quicksort

    tempo_final = int((fim-inicio)*1000000) # tempo em milisegundos

    # 3) criando um arquivo que salva o valor_maximo e o tempo
    arquivo = open('quicksort.txt', 'a') # txt esta no mesmo dir que este arquivo/ a significa que vai ser add nova linha no final

    texto = str(valor_maximo) + ' ' + str(tempo_final) + '\n'
    arquivo.write(texto)


    arquivo.close() # fecha o arquivo

    # 4) reiniciando o while
    restart = input(' Deseja fazer um novo teste?: 1 = Sim e 0 = Não :  ')
    restart = int(restart)
    if restart == 1:
        continue
    elif restart == 0:
        break
    else:
        print('Valor Inválido! ')
        break 
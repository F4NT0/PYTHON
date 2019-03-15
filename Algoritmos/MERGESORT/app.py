# Arquivo de teste do mergesort

 # este arquivo serve para poder fazer testes do mergesort e armazenar os valores em um arquivo

 # IMPORTS
import random
import time
import mergesort

# VARIAVEIS
lista = []
loop = True

# LOOP DE TESTES

while loop:

    # 1. Criação de uma lista de valores aleatórios

    valor_maximo = input('Numero Inteiro: ')    
    valor_maximo = int(valor_maximo)

    for i in range(valor_maximo):
        lista.append(random.randint(0,100)) #random.randomint(minimo,maximo) cria valores aleatorios inteiros

    # 2. Calculando o tempo de resolução do Algoritmo

    inicio = time.time() # tempo de inicio do algoritmo(antes de começar)
    mergesort.mergeSort(lista) # usado o algoritmo do mergeSort()
    fim = time.time() # tempo final do algoritmo

    tempo_final = int((fim-inicio)*1000000) # tempo em milisegundos

    # 3. Criando um arquivo que salva os valores obtidos

    arquivo = open('mergesort.txt', 'a') # cria um .txt e adiciona o valor numa nova linha
    texto = str(valor_maximo) + ' ' + str(tempo_final) + '\n'
    arquivo.write(texto) 
    arquivo.close() # fecha o arquivo

    # 4. Teste para ver se faz mais testes
    restart = input('Deseja fazer um novo teste? : 1 = Sim/0 = Nao : ')
    restart = int(restart)
    if restart == 1:
        continue # volta para o inicio deste while
    elif restart == 0:
        break #para o processo
    else:
        print('Valor Inválido!')
        break

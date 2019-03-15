# ARQUIVO DO ALGORITMO DO MERGESORT

def mergeSort(lista):
    """ Função do Algoritmo de MergeSort"""
    if len(lista) > 1:
        meio = len(lista) // 2 # // é divisão inteira
        metade_esq = lista[:meio] # lista vai da posição 0 até (meio - 1)
        metade_dir = lista[meio:] # lista vai da posição do meio até o final

        # fazendo uma recursão da função com cada metade das listas
        mergeSort(metade_esq)
        mergeSort(metade_dir)

        # CONTADORES PARA AS LISTAS
        contador_1 = 0 # da lista da metade esquerda
        contador_2 = 0 # da lista da metade direita
        contador_3 = 0 # da lista total

        while contador_1 < len(metade_esq) and contador_2 < len(metade_dir)

            if metade_esq[contador_1] < metade_dir[contador_2]:
                lista[contador_3] = metade_esq[contador_1]
                contador_1 += 1
            else:
                lista[contador_3] = metade_esq[contador_2]
                contador_2 += 1
            contador_3 += 1

        
        while contador_1 < len(metade_esq):
            lista[contador_3] = metade_esq[contador_1]
            contador_1 += 1
            contador_3 += 1
        
        while contador_2 < len(metade_dir):
            lista[contador_3] = metade_dir[contador_2]
            contador_2 += 1
            contador_3 += 1


# ARQUIVO COM AS FUNÇÕES DO QUICKSORT

def partition(lista, pos_inicio, pos_fim):
    """ Função de Partição do QuickSort. (Versão Professor)"""
    q = pos_inicio
    pos_fim -= 1
    for j in range(pos_inicio,pos_fim):
        if lista[j] <= lista[pos_fim]:
            lista[j], lista[q] = lista[q], lista[j]
            q += 1
    lista[pos_fim], lista[q] = lista[q], lista[pos_fim]
    return q


def quicksort(lista, pos_inicio, pos_fim):
    """ Função de QuickSort (Versão do Professor)"""
    if pos_inicio < pos_fim:
        q = partition(lista, pos_inicio, pos_fim)
        quicksort(lista, pos_inicio, q-1)
        quicksort(lista, q+1, pos_fim)






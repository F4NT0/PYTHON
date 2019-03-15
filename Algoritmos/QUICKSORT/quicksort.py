# ARQUIVO COM AS FUNÇÕES DO QUICKSORT

def partition(data, p, r):
    """ Função de Partição do QuickSort. (Versão Professor)"""
    q = p;
    for j in range(p,r):
        if data[j] <= data[r]:
            data[j], data[q] = data[q], data[j]
            q += 1
    data[r], data[q] = data[q], data[r]
    return q


def quicksort(data, p, r):
    """ Função de QuickSort (Versão do Professor)"""
    if p < r:
        q = partition(data, p, r);
        quicksort(data, p, q-1);
        quicksort(data, q+1, r);






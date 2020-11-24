#
# Teste de Dicionários
#

# Pegando dados do dicionário pela chave

dic = {
    'Color': 'Green',
    'Pepe': 1,
    True: 5
}

print("Primeiro dado do Dicionario: " + dic['Color'])
print("Segundo dado do Dicionario: " + str(dic['Pepe']))
print("Terceiro dado do Dicionario: " + str(dic[True]))

# Definindo todas as Chaves como Numeros

dic2 = {
    1 : 3,
    2 : 4,
    3 : 5 
}

print("\nPrimeiro Valor do Dic2: " + str(dic2[1]))
print("Segundo Valor do Dic2: " + str(dic2[2]))
print("Terceiro Valor do Dic2: " + str(dic2[3]))
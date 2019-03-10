# TESTANDO COMO SE FAZ FUNÇÕES

print('Teste de Argumentos: \n')

def bicho(nome_bicho,tipo_bicho):
    """ Serve para dizer qual nome e tipo de bicho"""
    print('Nome do bicho: ',nome_bicho,' e ele e um(a) ',tipo_bicho)

# Argumento posicional
bicho('Bili','Cachorro')

# Argumento nomeado 1
bicho(nome_bicho='Marry',tipo_bicho='Gato')

# Argumento nomeado 2
nome = 'Zoobomafoo'
tipo = 'Macaco'
bicho(nome,tipo)

print('Teste com return e print() de saida: \n')

def soma(valor_1,valor_2):
    saida = valor_1 + valor_2
    return saida

# chamando a funcao soma com return

valor_soma = soma(1,1)
print('Valor da soma de 1 + 1: ',str(valor_soma))


def nome(nome):
    print(nome)

# Chamando o nome da função dentro da função

nome('Gabriel')


print('Teste com argumento arbitrario')

def lista_compras(*produtos):
    """ Serve para criar uma lista de compras."""
    for produto in produtos:
        print(produto)

# Chamando a função com argumento arbitrario

print('Lista 1: ')
lista_compras('Cebola','Alface','Pepino')
print('\nLista 2: ')
lista_compras('Queijo','Presunto')
print('\nLista 3: ')
lista_compras('Banana')




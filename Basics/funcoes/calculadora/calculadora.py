# ESTE ARQUIVO É UM MÓDULO,SERVE PARA FAZER IMPORT

def nome():
    print('Bem vindo ao Módulo de Calculadora! ')

def soma(valor_1,valor_2):
    """ Função para fazer uma soma."""
    soma = valor_1 + valor_2
    return soma

def sub(valor_1,valor_2):
    """ Função para fazer uma subtração."""
    sub = valor_1 - valor_2
    return sub

def multi(valor_1,valor_2):
    """ Função para fazer uma multiplicação."""
    multi = valor_1 * valor_2
    return multi

def div(valor_1,valor_2):
    """ Função para fazer uma divisão."""
    if valor_1 < valor_2:
        div = valor_2 / valor_1
        return div
    elif valor_1 > valor_2:
        div = valor_1 / valor_2
        return div
    else:
        div = valor_1 / valor_2
        return div

def pot(base,expoente):
    """ Função para fazer uma exponenciação."""
    pot = base ** expoente
    return pot
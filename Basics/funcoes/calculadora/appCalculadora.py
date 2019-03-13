# ESTE ARQUIVO É UM TESTE DO MÓDULO

# Fazendo o import do arquivo calculadora
import calculadora

# importando uma função com print() de retorno
calculadora.nome()

# importando uma função com return de retorno
valor_1 = input('Digite o primeiro valor: ')
valor_2 = input('Digite o segundo valor: ')

# Transformando os valores de entrada em inteiros

valor_1 = int(valor_1)
valor_2 = int(valor_2)

soma = calculadora.soma(valor_1,valor_2)
print('Soma dos dois valores: ',soma)

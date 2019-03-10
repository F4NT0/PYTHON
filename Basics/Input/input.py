# testes com input

print('TESTE COM ENTRADA DE INTEIROS')
valor = input('Entre com um valor inteiro: ')
valor = int(valor)

valor_2 = input('Entre com outro valor inteiro: ')
valor_2 = int(valor_2)

soma = valor + valor_2

print('A soma dos valores: ',str(soma))


print('TESTE COM ENTRADA DE PONTOS FLUTUANTES')
valor = input('Entre com um valor de ponto flutuante: ')
valor = float(valor)

valor_2 = input('Entre com outro valor de ponto flutuante: ')
valor_2 = float(valor_2)

soma = valor + valor_2

print('A soma dos valores: ',str(soma))

print('MEXENDO COM LISTAS DE NUMEROS: ')
# Atributos
numeros = []
contador_pos = 0
contador_for = 0
booleano = True

# While
while booleano:
    print('Diga um numero inteiro para a posicao [',contador_pos,']')
    entrada = input('Diga o valor: ')
    entrada = int(entrada)
    numeros.append(entrada)
    restart = input('Deseja adicionar mais um valor? S/N : ')
    if restart.upper() == 'S' or restart.lower() == 's':
        contador_pos += 1
        booleano = True
    elif restart.upper() == 'N' or restart.lower() == 'n':
        booleano = False
    else:
        print('Entrada invalida, finalizando...')
        break

# for de leitura
for numero in numeros:
    print('Posicao [',contador_for,']: ',numero)
    contador_for += 1



# TESTE DO LAÇO WHILE

# Se desejar testar um while infinito, descomente abaixo

# booleano = True
# valor = 0
# while booleano:
#     valor += 1
#     print('Valor agora é: ',str(valor))

# WHILE FINITO NATURAL
print('WHILE COM ALTERACAO DE VALOR')

valor = 2
contador = 1

while valor > 0:
    print('Interacao do while numero ',str(contador))
    contador += 1
    valor -= 1

# WHILE ALTERANDO O VALOR BOOLEANO

print('WHILE COM ALTERACAO DE VALOR BOOLEANO')

booleano = True

while booleano:
    stop = input('Deseja parar o While? S/N : ')
    
    if stop == 'S' or stop == 's':
        print('Parando o While...')
        booleano = False
    elif stop == 'N' or stop == 'n':
        print('Continuando o While...')
    else:
        print('Valor não aceito!')
        break


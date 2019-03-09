# TESTE DE ENTRADA DE VALORES EXTERNOS E COLOCANDO EM UMA LISTA
# IREMOS UTILIZAR O CONHECIMENTO DE IF/ELSE,LISTA,FOR,WHILE E INPUT PARA ISSO
# upper() coloca em letras maiusculas e lower() coloca em minusculas (ex = nome.upper() ou nome.lower())

valores = [] # criado uma lista vazia
contador_posicao = 0 # criado um contador para saber qual posicao esta sendo adicionada
contador_posicao_2 = 0
booleano = True # serve para controlar o while
print('Criando uma lista de valores inteiros')

while booleano:
    print('Adicione o valor na posicao [',contador_posicao,']: ')
    valor_entrada = input('Adicione o valor: ')
    valor_entrada = int(valor_entrada) # transforma a string de entrada em um valor inteiro
    valores.append(valor_entrada) # adicionado o valor na posicao
    contador_posicao += 1 # incrementando o contador
    restart = input('Deseja adicionar mais valores? S/N : ')
    if restart.lower() == 's' or restart.upper() == 'S':
        booleano = True
        pass
    elif restart.lower() == 'n' or restart.upper() == 'N':
        booleano = False
        reinicio = False
        pass
    else:
        print('Entrada invalida! ')
        break
for valor in valores:
    print('[',contador_posicao_2,']:',valor)
    contador_posicao_2 += 1







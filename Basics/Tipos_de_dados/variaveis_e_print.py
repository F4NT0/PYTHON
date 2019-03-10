# trabalhando com variaveis e print

variavel_inteira = 3
variavel_ponto_flutuante = 3.2
variavel_string = 'saida da string'

print('teste de inteiro: ', variavel_inteira)
print('teste de ponto flutuante: ', variavel_ponto_flutuante)
print('teste de string: ', variavel_string)


print('\nSOMA')
v_1 = 3
v_2 = 2
soma = v_1 + v_2
soma_2 = 2 + 3
print('Valores: ',str(v_1),'',str(v_2),' Soma: ',str(soma),' ou ',str(soma_2))

print('\nSUBTRACAO')
v_1 = 3
v_2 = 2
sub = v_1 - v_2
sub_2 = 3 - 2
print('Valores: ',str(v_1),'',str(v_2),' Sub: ',str(sub),' ou ',str(sub_2))

print('\nMULTIPLICACAO')
v_1 = 3
v_2 = 2
multi = v_1 * v_2
multi_2 = 3 * 2
print('Valores: ',str(v_1),'',str(v_2),' multi: ',str(multi),' ou ',str(multi_2))

print('\nDIVISAO')
v_1 = 3
v_2 = 2
div = v_1 / v_2
div_2 = 3 / 2
print('Valores: ',str(v_1),'',str(v_2),' div: ',str(div),' ou ',str(div_2))

print('\nEXPONENCIAL')
v_1 = 3
v_2 = 2
exp = v_1 ** v_2
exp_2 = 3 ** 2 # seria 3^2
print('Valores: ',str(v_1),'',str(v_2),' exp: ',str(exp),' ou ',str(exp_2))

print('\nMODULO')
v_1 = 3
v_2 = 2
mod = v_1 % v_2
mod_2 = 3 % 2
print('Valores: ',str(v_1),'',str(v_2),' exp: ',str(mod),' ou ',str(mod_2))


print('\nSTRINGS')
nome = 'Gabriel'
nome_2 = "Pedro"

# verificando se '' e "" fazem a mesma coisa
print('nome 1: ', nome)
print("nome 2: ", nome_2)

# concatenando
juntando = nome + ' ' + nome_2
print(juntando)

# tab e nova linha
print('\tdando tab')
print('\ndando nova linha')

print('\nBOOLEANO')

valor_1 = True
print('o valor booleano e: ',valor_1)
valor_2 = False
print('o valor booleano e: ',valor_2)

print('\nALTERACAO DE VALOR DE VARIAVEL')
soma = 1
sub = 2
multi = 2
div = 4

soma += 1 # 1 + 1 = 2
print('Incrementando: ',soma)
sub -= 1 # 2 - 1 = 1
print('Decrementando: ',sub)
multi *= 2 # 2 * 2
print('Multiplicando: ',multi)
div /= 2 # 4 /2 = 2
print('Dividindo: ',div)



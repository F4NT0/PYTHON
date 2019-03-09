# TESTES DE IF/ELSE

# entrada de texto para testar
valor1 = input('Entre o primeiro valor para teste: ')
# toda entrada entra como string, vamos definir como inteiro
valor1 = int(valor1)

valor2 = input('Entre o segundo valor para teste: ')
valor2 = int(valor2)

if valor1 > valor2:
    print('Primeiro valor é maior!')
elif valor1 < valor2:
    print('Primeiro valor é menor!')
else:
    print('Os dois valores são iguais')
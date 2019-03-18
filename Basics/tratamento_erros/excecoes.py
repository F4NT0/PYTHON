try:
    valor = 10
    print(valor + 'é um número') # vai ocorrer uma exceção TypeError
    print(valor / 2) # vai ocorrer uma exceção ValueError
except ZeroDivisionError:  # não irá acontecer
    print('Nao pode dividir por zero!')
except TypeError: # irá ocorrer
    print('Arrumando a saida...')
    print(str(valor) + ' é um número')
except ValueError: # irá ocorrer
    print('Arrumando a Saida...')
    print(str(valor/2))
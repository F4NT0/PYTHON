# if/else com uma lista

nomes = ['Gabriel','Pedro','Vini','Dodo']
meu_nome = input('Seu nome e? ')
contador = 0 # para finalizar a passagem dentro do for
for nome in nomes:
    if meu_nome in nome: # se tiver o nome na lista
         print('meu nome esta na lista!')
         break # finaliza o for
    elif contador == 3 and meu_nome not in nome: # se não tiver
         print('Nao estou na lista!')
    else:
         pass
    contador += 1
# Quando o contador chega no tamanho da lista, testa o elif

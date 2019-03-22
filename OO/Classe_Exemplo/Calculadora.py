class Calculadora:
    # Método Construtor
    def __init__(self,valor_1,valor_2):
        self.valor_1 = valor_1
        self.valor_2 = valor_2

     # Métodos da Calculadora

    def soma(self):
        """ Método de soma de valores."""
        soma = self.valor_1 + self.valor_2
        return soma

    def multi(self,valor_1,valor_2):
        """ Métodos de multiplicação de valores."""
        multi = valor_1 * valor_2
        return multi

      # Método de Print de valores

    def imprime(self,multi,soma):
        print("Multiplicacao: ",int(multi))
        print("Soma: ",int(soma))

    
# Chamando os Métodos fora da Classe
valor_1 = 2
valor_2 = 2

calculo = Calculadora(valor_1,valor_2) # criando um objeto
soma = calculo.soma() # chamando o metodo com return soma
multi = calculo.multi(2,2) # chamando o metodo com return multi
calculo.imprime(multi,soma) # vai fazer os dois métodos 
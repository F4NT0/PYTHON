# para criar uma classe, faça como abaixo
class Metodos_Calculadora(): # classes são organizadas por identação, se sabe que as infos estão dentro da classe por existir um tab 
    
    
    # OBSERVAÇÃO:  todos os métodos dentro de uma classe deve iniciar com self
    
    # como se cria um método vazio em python, se coloca o pass
    def metodo_vazio(self):
        pass

    # para iniciar valores dentro de uma classe se usa o método init
    # o método init serve para iniciar um objeto de uma classe
    # é o "método construtor" do python
    
    # EXEMPLO: método construtor de duas variaveis para cálculos
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    
    # Encima desse método construtor, iremos construir os outros métodos para calculos

    # SOMA DE DOIS VALORES
    def soma(self):
        soma = self.a + self.b
        return soma
    
    # SUBTRAÇÃO DE DOIS VALORES
    def subtracao(self):
        sub = self.a + self.b
        return subtracao

    # MULTIPLICAÇÃO DE DOIS VALORES
    def multiplicacao(self):
        multi = self.a * self.b
        return multi
    
    # DIVISÃO DE DOIS VALORES
    def divisao(self):
        # abaixo uma estrutura de if/else
        if self.a > self.b:
            div = self.b / self.a 
        else:
            div = self.a / self.b
        return div
    

    # COM ESSES MÉTODOS, TEMOS UMA CLASSE COM MÉTODOS DE CALCULO
    # ESSA CLASSE IRÁ SER CHAMADA PARA OUTRO ARQUIVO CHAMADO APP_CALCULO

    # cria-se uma instancia da classe importada, dando os valores de entrada
instancia_classe = Metodos_Calculadora(4,5)
print("Soma dos valores de entrada: ", instancia_classe.soma())
print("Subtração dos valores de entrada: ", instancia_classe.subtracao())
print("Multiplicação dos valores de entrada: ", instancia_classe.multiplicacao)
print("Divisao dos valores de entrada: ", instancia_classe.divisao())
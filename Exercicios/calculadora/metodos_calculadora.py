class Metodos_Calculadora(): 
    
    def metodo_vazio(self):
        pass

    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def soma(self):
        soma = self.a + self.b
        return soma

    def sub(self):
        sub = self.a - self.b
        return sub

    def multi(self):
        multi = self.a * self.b
        return multi
    
    def div(self):
        if self.a > self.b:
            div = self.b / self.a 
        else:
            div = self.a / self.b
        return div

# instancia_classe = Metodos_Calculadora(4,5)
# print("Soma dos valores de entrada: ", instancia_classe.soma())
# print("Subtracao dos valores de entrada: ", instancia_classe.sub())
# print("Multiplicacao dos valores de entrada: ", instancia_classe.multi())
# print("Divisao dos valores de entrada: ", instancia_classe.div())
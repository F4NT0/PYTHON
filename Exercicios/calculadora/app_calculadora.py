# ESTE ARQUIVO É PARA TESTAR E COMPILAR OS MÉTODOS DO ARQUIVO metodos_calculadora.py

# agora iremos importar os métodos do arquivo metodos_calculadora do diretorio calculadora
# from nome_diretorio import nome_arquivo
import Metodos_Calculadora

# cria-se uma instancia da classe importada, dando os valores de entrada
instancia_classe = Metodos_Calculadora(4,5)
print("Soma dos valores de entrada: ", instancia_classe.soma())
print("Subtração dos valores de entrada: ", instancia_classe.subtracao())
print("Multiplicação dos valores de entrada: ", instancia_classe.multiplicacao)
print("Divisao dos valores de entrada: ", instancia_classe.divisao())

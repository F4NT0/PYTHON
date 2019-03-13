# ESTA CLASSE SERVE PARA TESTAR OS METODOS DO ARQUIVO CLASSE
# Para podermos utilizar os metodos do arquivo classe.py, devemos:
# 1) dizer de qual arquivo python queremos pegar os metodos
# 2) dizer qual classe do arquivo queremos pegar os metodos
# 3) no nosso caso, pegamos a classe Classe() do arquivo classe.py
from classe import Classe

# agora iremos fazer uma instancia da classe Classe
# iremos usar a construcao do init, usando o nome da classe de vez de __init__
instancia_da_classe = Classe(4,5)

# agora podemos usar os metodos criados na classe Classe()

print("Soma: ", instancia_da_classe.soma())
print("Subtracao: ", instancia_da_classe.sub())
print("Multiplicacao: ", instancia_da_classe.multi())
print("Divisao: ", instancia_da_classe.div())


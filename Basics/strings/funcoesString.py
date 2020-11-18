# ----------------------------------------
# Exemplo de Funções para usar com String
# ----------------------------------------

nome = "gabriel fanto"
maiusculas = "letras maiusculas"
minusculas = "LETRAS MINUSCULAS"
espacoDireita = ' inicio'
espacoEsquerda = 'inicio '
dividindoEmDois = "nome:sobrenome"

# Colocando como Tíitulo
print(nome.title())

# Colocando todas as letras em maiusculas
print(maiusculas.upper())

# Colocando todas as letras em minusculas
print(minusculas.lower())

# Removendo o espaço branco da direita
print(espacoDireita.strip())

# Removendo o espaço branco da esquerda
print(espacoEsquerda.strip())

# Dividindo a String em duas separadas pelo :
print(dividindoEmDois.split(":"))
vetor = dividindoEmDois.split(":")
print(vetor[0])
print(vetor[1])

# Criando uma Substring, [primeiro char:ultimo char desejado+1]
primeiro_nome = nome[:7]
print(primeiro_nome)
ultimo_nome = nome[7:]
print(ultimo_nome)



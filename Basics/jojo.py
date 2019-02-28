
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.diz_oi = 'oi'

class JOJO(Pessoa):
    def __init__(self, nome='UNKNOWN'):
        super().__init__(nome)
        self.potato = "Eu sou uma batata"



jojones = JOJO()

print(jojones.potato)
print(jojones.nome)
print(jojones.diz_oi)
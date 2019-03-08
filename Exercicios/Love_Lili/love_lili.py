# Criando um while infinito do meu amor pela Lili
from time import sleep
import os 

amor = 1
lili = 1000000 
while amor <= lili:
    print('Fanto deu ',amor,' beijos em sua rainha!')
    amor += 1 # aumenta o meu amor
    lili += 10000 # aumenta o amor da lili
    sleep(1) # tempo entre beijos
    os.system('cls') limpa o terminal do windows

# Criando um while infinito do meu amor pela lili
from time import sleep
import os

amor = 1
lili = 1000000
while amor <= lili:
    print('Fanto deu ',amor,' beijos em sua rainha!')
    amor += 1
    lili += 10000
    sleep(1)
    os.system('clear') # limpa o terminal do linux

# Escreva um codigo que
# jokepo com o computador
from random import choice
print('\033[1;35mBem Vindo ao JOGOOOO\nVamos jogar Jokepo\033[m')
jogador = input('Qual sua jogada:')
computador = choice(['pedra','papel','tesoura'])
print(computador)
if jogador == computador:
    print('Empate')
elif jogador == 'pedra' and computador == 'papel':
    print('Eu ganhei esta.')
elif jogador == 'papel' and computador == 'tesoura':
    print('Eu ganhei esta.')
elif jogador == 'tesoura' and computador == 'pedra':
    print('Eu ganhei esta.')
elif jogador == 'pedra' and computador == 'tesoura':
    print('Você ganhou, Nice')
elif jogador == 'tesoura' and computador == 'papel':
    print('Você ganhou, Nice')
elif jogador == 'papel' and computador == 'pedra':
    print('Você ganhou, Nice')
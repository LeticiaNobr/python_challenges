# Escreva um programa que solicite nomes ao usuario e escolha aleatoriamente um
from random import choice
n = input('Digite os nomes:')
n = choice(seq=n)
print('O aluno que apagara o quadro é: {}'.format(n))
# Escreva um programa que solicite nomes e mostre um sequencia aleatoria deste
from random import choice
n = input('Digite os nomes:')
lista=(n)
print('A sequencia de apresentação é {},{},{},{}'.format(choice(lista),choice(lista),choice(lista),choice(lista)))
# Escreva um programa que solicite um número real e mostre sua parte inteira.
from math import trunc
n = float(input('Digite um número real:'))
print('O número {} tem a parte inteira {}.'.format(n,trunc(n)))
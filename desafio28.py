# Escreva um programa que pense em um número e solicte ao usuario tentar adivinha-lo 
import random
print('Vou pensar em um número tente adivinhar')
print('='*20)
n = int(input('Digite o número de aposta:'))
p = random.randrange(0,5)
if n == p:
    print('Af ... você venceu')
else:
    print('Você .... Perdeuuuu!! Eu ganhei, eu pensei no {} e você no {}'.format(p,n))
print('='*20)
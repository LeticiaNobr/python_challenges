# Escreva um programa que solicite um algulo e forneça seu seno, cosseno e tangente
from math import cos,sin,tan,radians
n = float(input('Digite o angulo:'))
print('O seno deste angulo é {:.2f} o cosseno é {:.2f} e sua tangente é {:.2f}'.format(sin(radians(n)),cos(radians(n)),tan(radians(n))))
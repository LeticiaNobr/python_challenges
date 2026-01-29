# Escreva um programa que solicite cateter oposto, adjacente e mostre a hipotenusa do triangulo
from math import sqrt
co = float(input('Digite o valor do cateter oposto:'))
ca = float(input('Digite o valor do cateter adjacente:'))
print('O comprimento da hipotenusa do triângulo retangulo é:{:.1f}'.format(sqrt((co**2)+(ca**2))))
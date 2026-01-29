# Escreva um programa que diga se os valores fornecidos formam um triangulo
a = float(input('Digite o primeiro segmento:'))
b = float(input('Digite o segundo segmento:'))
c = float(input('Digite o terceiro segmento:'))
if c+a>b and c+b>a and a+b>c:
 print('\033[4;31;43mEsse tres segmentos formam um triangulo\033[m')
else:
 print('Esses segmentos não formam um triangulo')

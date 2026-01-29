# Escreva um programa que caso o salario seja maior que 1250 receba 10% de aumento caso menor 15%
s = float(input('Digite o valor de seu salário: '))
if s > 1250.00:
 print('Seu salário com aumento de 10% equivale a: R$ {:.2f}'.format((10+100)/100*s))
else:
 print('Seu salário com aumento de 15% equivale a: R$ {:.2f}'.format((15+100)/100*s))
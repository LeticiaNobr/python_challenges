#Escreva um programa que leia um numero inteiro e diga se ele e ou nao um numero primo
n = int(input('Digite um número para verificar se o mesmo e primo: '))
div = 0
for c in range(1,n + 1):
    if n % c == 0:
       div = div + 1
if div == 2:
    print('Este número é um número primo')
else:
    print('Este número não e um número primo')
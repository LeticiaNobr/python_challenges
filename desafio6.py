# Escreva um programa que leia um número fornecido pelo usuario e mostre seu dobro, triplo e raiz quadrada
n= int(input('Digite um número:'))
print('O dobro do número digitado é: {}\n O triplo do número digitado é: {}\nA raiz quadrada do número digitado é: {:.2f}'.format(n*2,n*3,n**(1/2)))
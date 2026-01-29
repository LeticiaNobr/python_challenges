# Escreva um programa que pergunte o valor de um produto e o desconto a ser aplicado e mostre o valor atualizado
prod = float(input('Digite o valor do produto:'))
des = float(input('Digite o desconto aplicado:'))
print('O valor original do produto é R$: {:.2F}\n com o desconte de: {}% aplicado,\n teremos o valor atualizado para R$: {:.2F}.'.format(prod,des,prod -(prod*des/100)))
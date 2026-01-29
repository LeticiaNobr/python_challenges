# Escreva um programa que inique quantos dolares um usuario pode comprar com o valor que possui.
n = float(input('Digite quanto de dinheiro possui: R$ '))
print('Com R$ {:.2F} é possivel comprar: US$ {:.2F}'.format(n,n/5.41))
# Escreva um programa que pergunte a largura e altura de um local e mostre sua area e quantos litros de tinta e preciso para pinta-lo
l = float(input('Qual a largura do local a ser pintado:'))
a = float(input('Qual a altura do local a ser pintado:'))
print('A area do local é de: {}. Sendo necessario {} litros de tinta.'.format(a*l,(a*l)/2))
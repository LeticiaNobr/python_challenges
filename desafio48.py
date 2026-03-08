#Crie um programa que calcule a soma de todos os numero impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500
soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
     soma = soma + c
print('A soma de todos os números impares de 1 a 500 divisiveis por 3 e igual a {}'.format(soma))
  
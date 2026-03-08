#Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas dos que forem pares se for impar desconsidere 
for c in range(0,7):
    if c%2 == 0:
        print(c)
        soma = c+c
print('A soma dos numeros pares e {}'.format(soma))
#ou caso solicitado pelo usuario
for n in range(1,7):
 n = int(input('Digite um numero: '))
 if n%2 == 0:
    soma = n+n
for n in range(0,7):
 if n %2 == 0:
  print('Os numeros pares digitados foram {}'.format(n))  
print('A soma dos numeros pares e {}'.format(soma))
# Versão do usuario simplificada:
for c in range (0,6):
 n = int(input('Digite um número:'))
if n % 2 == 0:
 soma = n + n 
 print('A soma dos numeros pares e {}'.format(soma))
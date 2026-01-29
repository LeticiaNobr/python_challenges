# Escreva um programa que mostre True se o nome da cidade informada pelo usuario seja santos 
n = str(input('Digite o nome da sua cidade:'))
n= n.split()
print('santo'in n[0].lower())
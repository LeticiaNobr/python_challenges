# Escreva um programa que mostre o valor de uma viagem acima de 200 e abaixo de 200km
km = float(input('Digite quantos km tem sua viagem: '))
if km <= 200:
 print('Sua viagem deu o valor total de: R$ {:.2f' \
 '}'.format(km*0.50))
else:
 print('Sua viagem deu o valor total de: R$ {:.2f}'.format(km*0.45))
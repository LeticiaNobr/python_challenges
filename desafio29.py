# Escreva um programa que multe o usuario se estiver acima de 80 km 
km = float(input('Digite a quantos km está:'))
if km > 80:
 print('Você foi multado!')
 m = km - 80
 print('O valor da multa é de: R$ {}'.format(m*7.00))
else:
 print('Pode seguir caminho')
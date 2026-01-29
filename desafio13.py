# Escreva um programa que obtenha o salario do usuario e aplique 15% de aumento mostrando o valor atualizado
salario = float(input('Digite o valor de seu sálario:'))
print('Seu sálario atual é de: {} com o aumento de 15 sera de: {:.2f}'.format(salario,(15+100)/100*salario))
# Escreva um programa que leia um nome digitado pelo usuario, escreva ele todo em maiusculo, minisculo, quantdades de letras do nome, quantidade do primeiro nome apenas e qual o primeiro nome
name = str(input('Digite seu nome:'))
print(name,'\n',name.upper(),'\n',name.lower())
print(len(name.strip()))
name = name.split()
name = name[0]
print(len(name))
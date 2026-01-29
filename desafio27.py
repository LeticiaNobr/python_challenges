# Escreva um codigo que leia o nome de uma pessoa e mostre seu primeiro nome e seu ultimo nome
n = str(input('Qual seu nome:')).strip()
n=n.split()
print('primeiro nome: {}\n seu ultimo nome é: {}'.format(n[0],n[len(n)-1]))
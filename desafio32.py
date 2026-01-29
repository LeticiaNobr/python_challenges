# Escreva um codigo que diga se o ano digitado e bissexto
ano = int(input('Digite o ano:'))
if ano%4 == 0 :
    print('Este ano e bissexto')
else:
    print('Este ano não é bissexto')

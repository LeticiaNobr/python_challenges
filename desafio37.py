#Escreva um programa que:
# leia um númeor
# deixe o usuario escolher a base de converção
# 1 para binario 2 para octal e 3 para hexadecimal
numero = int(input('Digite o número que deseja converter:'))
conversao = int(input('Para escolher a conversão digite:\n 1 - para binário\n 2 - para octal\n 3 - para hexadecimal\n Conversão desejada: '))
if conversao == 1 :
    print('O número {} convertido para binário é {}'.format(numero,bin(numero)))
elif conversao == 2:
    print('O número {} convertido para octal é {}'.format(numero,oct(numero)))
else:
    print('O número {} convertido para hexadecimal é {}'.format(numero,hex(numero)))


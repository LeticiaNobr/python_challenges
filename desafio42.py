# Escreva um codigo que reforça o desafio 035
# Se puder forma um triangulo
#  Equilatero todos os lados igual
#  Isosceles dois lados igual
#  Escaleno todos os lados diferentes

a = float(input('Digite o primeiro segmento:'))
b = float(input('Digite o segundo segmento:'))
c = float(input('Digite o terceiro segmento:'))
if c+a>b and c+b>a and a+b>c:
 print('\033[4;31;43mEsse tres segmentos formam um triangulo\033[m')
if c == a and a == b and b == c:
 print('Você tem um triangulo \033[7;33;42mequilatero\033[m')
elif c == a or a == b or b == c:
 print('Você tem um triangulo \033[7;33;41misosceles\033[m')
elif c != a and a != b and b != c:
 print('Você tem um triangulo \033[7;33;45mescaleno\033[m')
else:
 print('Esses segmentos não formam um triangulo')
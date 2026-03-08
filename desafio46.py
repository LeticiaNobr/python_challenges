#Faça um programa que:
#mostre na tyela uma contagem regressiva para estouro dos fogos de artificios indo de:
#0 ate 10
#com pausa de 1 seg entre eles
from time import sleep
s=sleep(1)
for c in range(10,0,-1):
    sleep(1)
    print(c)
for c in range(0,4):
 sleep(1)
 print('''\033[1;31m
        .            .            .
        .            .            .
        .            .            .
     '  :  '      '  :  '      '  :  '
----: - * - :----: - * - :----: - * - :----
     '  :  '      '  :  '      '  :  '
        '            '            '
        .            .            .
        .            .            .
      \033[m''')
print('Feliz Ano Novo!!!')
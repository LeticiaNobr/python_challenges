#Desenvolva um programa quie leia o primeiro termo e a razao de uma pa. no final mostre os 10 primeirois termos dessa progressao
termo = int(input('Digite o primeiro termo de sua pa: '))
r = int(input('Digite a razão da sua pa:'))
decimo = termo + (10-1)*r
soma = decimo + r
for c in range(termo, soma, r):
 print(c,end=',...')
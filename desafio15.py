# Escreve um programa que mostre o total a pagar de um usuario baseado nos dias que um carro foi alugado e km percorridos 
d = int(input('Por quantos dias o carro foi alugado:'))
km = float(input('Por quantos km ele andou:'))
print('O total a pagar é R${:.2f}'.format((d*60)+(km*0.15)))
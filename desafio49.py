#Refaça o exercicio 9 mostrando a tabuada de um numero de escolha do usuario usando for 
n = int(input('Digite um número: '))
print('Segue tabuada do numero {}:'.format(n))
print('-'*15)
for c in range(0,11):
 soma=n*c
 print('{} x {} = {}'.format(n,c, soma))
print('-'*15)
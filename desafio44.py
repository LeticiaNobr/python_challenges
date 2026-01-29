# Escreva um codigo que:
# calcule o valor a ser pago pelo produto considerando:
# preço normal 
# consição de pagamento
# a vista dinheiro ou cheque 10% de desconto
# a vista no cartão 5% de desconto
# em ate 2x no cartão preço normal
# 3x ou mais 20% de juros
print('\033[4;31;43m-\033[m'*50)
preco = float(input('Digite o valor do produto: '))
escolha = int(input('Escolha a forma de pagamento:\n0 para dinheiro a vista ou cheque\n1 para cartão a vista\n2 para parcelamentos no cartão:\n'))
if escolha == 0:
 desconto0 = preco*0.10
 print('O valor a ser pago neste forma de pagamento é de:\nR${} devido desconto de 10%'.format(preco-desconto0))
elif escolha == 1:
 desconto1 = preco*0.05
 print('O valor a ser pago neste forma de pagamento é de:\nR${} devido desconto de 5%'.format(preco-desconto1))
elif escolha == 2:
 parcelas = int(input('Digite as parcelas desejadas: '))
 juros = preco * 0.20
 if parcelas <= 2:
  print('O valor a ser pago neste forma de pagamento é de:\nR${}'.format(preco))
 else:
  print('O valor a ser pago neste forma de pagamento é de:\nR${} devido juros de 20%'.format(preco+juros))
print('\033[4;31;43m-\033[m'*50)

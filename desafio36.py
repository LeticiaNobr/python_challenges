#Escreva um programa de aprovação de emprestimo bancario
#O programa deve perguntar:
 #valor da casa
 #salrio
 #quantos anos para pagar
#O valor da prestação deve ser calculado de forma que não exceda 30% do salario ou o esprestimo e negado.
casa = float(input('Qual o valor do imovel desejado:'))
salario = float(input('Qual o sálario do comprador:'))
parcelas = int(input('Em quantos anos pretende pagar o imovel:'))
imovel = casa//parcelas
salario30 = 0.30*salario 
if  salario30 >= imovel :
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')
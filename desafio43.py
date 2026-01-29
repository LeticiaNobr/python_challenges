# Escreva um codigo que leia o peso 
# altura
# calcule imc
# e mostre status
# abaixo de 18.5 abaixo do PermissionErrorentre 18.5 e 25 peso ideal
# 25 a 30 sobrepeso
# 30 ate 40 obesidade
# acima de 40 obesidade morbida
print('\033[4;35;46m-\033[m'*50)
print('\033[4mInclua seus dados para analise de seu imc\033[m')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/(altura*altura)
print('Seu imc é de {:.2f}, se classificando em :'.format(peso/(altura*altura)))
if imc <= 18.5:
    print('Abaixo do peso,\nindicamos ganho de massa')
elif imc >= 18.5 and imc < 25:
    print('Peço ideal.')
elif imc >=25 and imc < 30:
    print('Atenção sobrepeso,\ncuidado com alimentação e exercicio leve')
elif imc >=30 and imc < 40:
    print('Atenção obesidade\nindicação de cuidado com alimentação e exercicio de frequencia')
else:
    print('Atenção obesidade morbida\nindicação para procura de profissional qualificado pra acompanhamento')
print('\033[4;35;46m-\033[m'*50)
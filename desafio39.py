#Escreva um codigo que:
#leia a idade de uma pessoa e informe
#Se ainda vai ter alistamento militar
#Se já ta na hora de se alistar
#Se já passou do tempo
#tambem deve mostrar tempo que falta ou ja passou
print('\033[1;33;42m=\033[m'*20,'\033[1;33;42mAlistamento militar\033[m','\033[1;33;42m=\033[m'*20)
sexo = input('Digite seu sexo:')
idade = int(input('Digite sua idade:'))
if idade == 18 and sexo != 'feminino':
    print('Você se encontra na idade de alistamento, pode seguir com seu cadastro.')
elif idade == 18 and sexo == 'feminino':
    print('Você se encontra na idade para alistamento, mas não e obrigatório, se aliste caso quera prestar voluntário.')
elif idade > 18 and sexo == 'masculino':
    print('Você já passou da idade para alistamento militar a {} ano(s), se apresente!'.format(idade-18))
elif idade < 18  and sexo == 'masculino' or sexo == 'feminino':
    print('Você ainda não esta na idade para alistamento militar, faltam {} ano(s).'.format(18-idade))
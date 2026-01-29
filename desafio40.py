#Crie um programa que leia as duas notas de um aluno
#calcule sua media
#mostra media abaixo de 5 reprovado
# entre 5 e 6.9 recuperação
# acima de 7 aprovado
n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
media = (n1+n2)/2
if media <= 5 :
    print('Aluno reprovador com nota de \033[1;31m{}\033[m'.format(media))
elif media <= 6.9 and media > 5:
    print('Aluno sujeito a recuperação, com nota de \033[1;33m{}\033[m'.format(media))
else:
    print('Aluno aprovado, com nota de \033[1;32m{}\033[m'.format(media))
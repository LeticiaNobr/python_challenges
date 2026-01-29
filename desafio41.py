# Escreva um codigo que
# Leia o ano de nascimento
# categoria conforme idade
# ate 9 mirim
# ate 14 infantil
# ate 19 junior
# ate 20 senior
# e acima de 20 master
print('Digite sua data de nascimento:')
ano = int(input('Ano:'))
if ano >= 2016 and ano <= 2025 :
    print('Categoria Mirim')
elif ano >= 2011 and ano <= 2015:
    print('Categoria infantil')
elif ano == 2006:
    print('Categoria junior')
elif ano == 2005:
    print('Categoria senior')
elif ano <= 2004:
    print('Categoria master')

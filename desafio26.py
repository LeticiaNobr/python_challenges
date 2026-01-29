# Escreva um codigi que solicite uma frase ao usuario e mostre quantas letras a tem na frase, a premiera posição, a segunda, e a ultima
f = str(input('Digite uma frase:')).lower().strip()
print('A letra a aparece : {} vezes, a primeira vez aparece na posição : {} e a ultima vez aparece na posição: {}'.format(f.count('a'),f.find('a')+1,f.rfind('a')+1))
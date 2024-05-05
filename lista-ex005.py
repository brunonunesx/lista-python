#5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre 
#na tela a sua média na disciplina.
#Ex: 
#Nota 1: 4.5
#Nota 2: 8.5
#A média entre 4.5 e 8.5 é igual a 6.5

not1 = float(input('Nota 1: '))
not2 = float(input('Nota 2: '))

med = (not1 + not2)/2
 
print('A média entre {} e {} é igual a {}'.format(not1, not2, med))
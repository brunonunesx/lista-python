#7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a 
#sua terça parte.
#Ex: 
#Digite um número: 3.5
#O dobro de 3.5 é 7.0
#A terça parte de 3.5 é 1.16666

num = float(input('Digite um número: '))
dob = num * 2
ter = num/3

print('O Doblo de {} é {} \nA terça parte de {} é {:.2f}'.format(num, dob, num, ter))
#4) Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório 
#entre eles.
#Ex:
#Digite um valor: 8
#Digite outro valor: 5
#A soma entre 8 e 5 é igual a 13.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
soma = num1 + num2 
print('a soma entre {} e {} é igual a {}'.format(num1, num2, soma))
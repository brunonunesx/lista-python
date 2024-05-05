#20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou 
#ÍMPAR.

num = int(input('Digite um número inteiro: '))
par = num % 2 
if (par == 0):
    print('esse número é par')
else:
    print('esse número é ímpar')
    
    

#49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles 
#são pares e quantos são ímpares.

s = 0 
p = 0
i = 0 

for c in range (0, 6, 1):
    n = int(input('digite um número: '))
    if (n % 2 == 0):
        p = p + 1 
    else:
        i = i + 1    
print('O total de números pares foi {} \nO total de números impares foi {} '.format(p, i))
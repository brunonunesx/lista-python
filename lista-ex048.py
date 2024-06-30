#48) Faça um programa que leia 7 números inteiros e no final mostre o somatório 
#entre eles

s = 0 
for c in range (0, 7, 1):
    n = int(input('digite um número: '))
    s += n
print(s)
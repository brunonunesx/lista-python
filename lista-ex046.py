#46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 
#8 + 10 + 12 + 14 + ... + 98 + 100.

s = 0
for c in range (6, 100+2, 2):
    print(c)
    s = s + c
print(s)
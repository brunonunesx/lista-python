#51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela 
#qual foi o maior e qual foi o menor preço digitados.

s = 0
m = 1000000000
for c in range (0, 8):
    p = float(input('digite o valor do produto: ' ))
    if (s < p):
        s = p
    if (m > p):
        m = p
print ('O maio valor registrado foi {}R$'.format(s))
print ('O menor valor registrado foi {}R$'.format(m))
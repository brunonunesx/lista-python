#9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) 
#e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

num = float(input('Qual é o valor em R$'))
dol = num/3.45
print('O valor de {}R$ corresponde a um total de {:.2f}U$'.format(num, dol))
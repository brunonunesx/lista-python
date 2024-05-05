#12) Crie um programa que leia o preço de um produto, calcule e mostre o seu 
#PREÇO PROMOCIONAL, com 5% de desconto.

pp = float(input('Digite o valor do produto '))

promo = pp - (5 * pp /100)

print('O valor do produto com desconto  é R${}'.format(promo))
#21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não 
#BISSEXTO.

ano = int(input('Digite um ano para saber se ele é bissexto '))
# 2024 % 6 = 2:
bis = ano % 6 
if (bis == 2):
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
    
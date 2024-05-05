#23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos 
#para todos, mas especialmente para mulheres. Faça um programa que leia nome, 
#sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo 
#que:
 #- Homens ganham 5% de desconto
 #- Mulheres ganham 13% de desconto
 
nome = str(input('Qual seu nome? '))
sexo = str(input('Qual o seu sexo M/F? '))
valor = float(input('Qual o valor do produto? '))
 
homem = valor - (5 * valor)/100
mulheres = valor -(13 * valor)/100
 
if(sexo == 'M'):
     print('O valor que o senhor tem que paga é {}'.format(homem))
else:
     print('O valor que a senhora tem que paga e de {}'.format(mulheres))

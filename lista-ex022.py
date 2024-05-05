#22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua 
#situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o 
#alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do 
#alistamento.

nasc = int(input('Qual sua data de nascimento? '))
ano_atual = int(input('Qual ano estamos '))

ali = abs(ano_atual-nasc)
pas = abs(ali - 18)
fal = abs(ali - 18)

if(ali > 18):
    print('Ja se passaram {} anos '.format(pas))
else:
     print('ainda falta {} anos '.format(fal))
#18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade 
#dela e depois mostre se ela pode ou não votar.

ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = 2024
votar = ano_atual - ano_nasc
if (votar >= 18):
    print('vc pode votar')
else:
    print('vc não pode votar')

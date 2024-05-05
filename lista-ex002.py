# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-
#vindas para ela:
#Ex:
#Qual é o seu nome? João da Silva
#Olá João da Silva, é um prazer te conhecer!

nome = str(input('Digite seu nome: '))
print ('Olá {}, é um prazer te conhecer!'.format(nome))
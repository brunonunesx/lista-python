#42)Faça um algoritmo que pergunte ao usuário um número inteiro e positivo 
#qualquer e mostre uma contagem até esse valor:
#Ex: Digite um valor: 35
#Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!

n = int(input('digite um valor para a contagem '))

for c in range (1, n+1, 1):
    print(c)
print('acabou')    
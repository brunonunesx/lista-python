#50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e 
#mostre na tela:
#a) Quais foram os números sorteados
#b) Quantos números estão acima de 5
#c) Quantos números são divisíveis por 3 

import random 

for c in range (0, 20, 1):
    sor = random.randint(1, 10)
    if (sor > 5):
        print('\033[32m{} esse número e menor que 5 \033[m'.format(sor))
    elif (sor % 3 == 0):
        print('\033[33m{} esse número e divisível por 3 \033[m'.format(sor))
    else:
        print('{}'.format(sor))
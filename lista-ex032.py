#32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o 
#jogador vai tentar descobrir qual foi o valor sorteado.

import random 
print ('\033[1;34m=-\033[m'*20)
print ('\033[1;35m             Jogo de Sortear    \033[m')
print ('\033[1;34m=-\033[m'*20)

computador = random.randint(1,5)
player = int(input('digite sua escolha '))
if player == computador:
    print ('Voce ganhou')
else:
    print ('voce perdeu \nA escolha do computador foi {}'.format(computador))
    
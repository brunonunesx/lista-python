#31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
from random import choice
print('\033[1;35m-=\033[m'*20)
print ('\033[1;34m           JOGON de JOKENPO\033[m')
print('\033[1;35m-=\033[m'*20)
player = str(input('Escolha entre pedra, papel e tesoura: '))
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
print ('Sua escolha foi {} \nMinha escolha foi {}'.format(player, computador))
if (player == 'tesoura') and (computador == 'papel'):
    print ('vc ganhou ')   
elif (player == 'tesoura') and (computador == 'pedra'):
    print ('vc perdeu ')   
elif (player == 'tesoura') and (computador == 'tesoura'):
    print ('Empatamos ')
elif(player == 'pedra') and (computador == 'tesoura'):
    print ('vc ganhou ')   
elif (player == 'pedra') and (computador == 'papel'):
    print ('vc perdeu ')   
elif (player == 'pedra') and (computador == 'pedra'):
    print ('Empatamos ')
elif(player == 'pqpel') and (computador == 'pedra'):
    print ('vc ganhou ')   
elif (player == 'papel') and (computador == 'tesoura'):
    print ('vc perdeu ')   
elif (player == 'papel') and (computador == 'papel'):
    print ('Empatamos ')
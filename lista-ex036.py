#36) Um programa de vida saudável quer dar pontos atividades físicas que podem 
#ser trocados por dinheiro. O sistema funciona assim:
# - Cada hora de atividade física no mês vale pontos
# - até 10h de atividade no mês: ganha 2 pontos por hora
# - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
# - acima de 20h de atividade no mês: ganha 10 pontos por hora
# - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos) 
#Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, 
#calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.

print('\033[1;35m-=\033[m'*20)
print ('\033[1;34m           Programa de vida\033[m')
print('\033[1;35m-=\033[m'*20)

horas = int(input('Quantos horas de atividades físicas vc praticar mês? '))

if (horas <= 10):
    total = horas * 2 
    dinheiro = total * 0.05
    print ('O total de pontos adquirido foi de {} e a quantidade de dinheiro foi de {}R$'.format(total, dinheiro))
elif (horas > 10) and (horas <= 20):
    total = horas * 5
    dinheiro = total * 0.05
    print ('O total de pontos adquirido foi de {} e a quantidade de dinheiro foi de {}R$'.format(total, dinheiro))
else:
    total = horas * 10
    dinheiro = total * 0.05
    print ('O total de pontos adquirido foi de {} e a quantidade de dinheiro foi de {}R$'.format(total, dinheiro))
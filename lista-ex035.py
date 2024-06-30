#35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O 
#aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para 
#carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
#que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e 
#quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a 
#tabela a seguir:
 #- Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km
 #- Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km

print('\033[1;35m-=\033[m'*20)
print ('\033[1;34m     empresa de aluguel\033[m')
print('\033[1;35m-=\033[m'*20)

carro = str(input('Qual o carro utilizado(luxo ou popular)? '))
km = float(input('Qual a kilometragem percorrida? '))
dia = int(input('Quantos dias foram usados o carro? '))



if (carro == 'popular'):
    if (km < 100):
        popular = (dia * 90) + (km * 0.2)
        print ('O Valor a se paga é de {}RS'.format(popular))
    else:
        popular = (dia * 90) + (km * 0.1)
        print  ('O Valor a se paga é de {}RS'.format(popular))      
else:
    if (km < 200):
        luxo = (dia * 150) + (km * 0.3)
        print ('O Valor a se paga é de {}RS'.format(luxo))
    else:
        luxo = (dia * 150) + (km * 0.25)
        print ('O Valor a se paga é de {}RS'.format(luxo))      

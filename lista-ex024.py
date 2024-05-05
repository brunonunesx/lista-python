#24) Faça um algoritmo que pergunte a distância que um passageiro deseja 
#percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para 
#viagens até 200Km e R$0.45 para viagens mais longas.

distancia = float(input('Qual a distância desejar percorrer? '))

print('-=-'*15)
if(distancia <= 200):
    valor_200 = distancia * 0.5
    print('\033[31mA viagem percorrendo {}km, ficará em {:.2f}R$\033[m'.format(distancia, valor_200))
else:    
    valor_m200 = distancia * 0.45
    print('\033[32mA viagem percorrendo {}km, ficará em {:.2f}R$\33[m'.format(distancia, valor_m200))
print('-=-'*15)    
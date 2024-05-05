#14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva 
#um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, 
#sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

dia = int(input('Quantos dias rodados: '))
km = float(input('Quantos km foram percorridos '))

pt = (dia * 90) + (km * 0.2)

print('O valor total a se paga é {}'.format(pt))
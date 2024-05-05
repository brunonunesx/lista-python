#10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
#mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
#sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

areat = lar * alt 
tinta = areat / 2 

print('A área total da parede é de {}m² e irá gastar {}L'.format(areat, tinta))
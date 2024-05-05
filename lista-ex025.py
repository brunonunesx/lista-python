#25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. 
#Analise seus comprimentos e diga se é possível formar um triângulo com essas 
#retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento 
#de cada lado deve ser menor que a soma dos outros dois.

print ('-='*15)
print('Analisando um triângulo')
print ('-='*15)
seg1 = int(input('Digite um número para o primeiro segmento do triângulo '))
seg2 = int(input('Digite um número para o segundo segmento do triângulo '))
seg3 = int(input('Digite um número para o terceiro segmento do triângulo '))

if (seg1+seg2 > seg3) and (seg1 + seg3 > seg2) and (seg3 + seg2 > seg1):
    print('\033[0;32mOs três segmento formam um triângulo\033[m')
else:
    print('\033[31mOs três segmento não formam um triângulo\033[m')  
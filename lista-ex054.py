#54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando 
#no final:
#a) Qual foi a média de altura do grupo
#b) Quantas pessoas pesam mais de 90Kg
#c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
#d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

sa = 0
p9 = 0 
a = 0
b= 0

for c in range (0,7):
    peso = float(input('Qual o seu peso: '))
    altura = float(input('Qual a sua altura: '))
    sa = sa + altura 
    if (peso > 90):
        p9 = p9 + 1
    if (peso < 50) and (altura < 1.60):
        a = a + 1 
    if (peso > 100) and (altura > 1.90):
        b = b + 1     
        
ma = sa / 7 
print('A media de altura do grupo foi {:.2f}m \n {} pessoas pesam mais de 90kg \n {} pessoa(s) pesam menos de 50kg e tem menos de 1.60m de altura \n {} pessoa(s) pesam mais de 100kg e mede mais de 1.90m de altura'.format(ma, p9, a, b)) 
#52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
#a) Qual é a média de idade do grupo
#b) Quantas pessoas tem mais de 18 anos
#c) Quantas pessoas tem menos de 5 anos
#d) Qual foi a maior idade lida

s = 0
maior = 0
menor = 0
mi = 0 
for c in range (0, 10):
    idade = int(input('Qual a idade: '))
    s = s + idade 
    if (idade > mi):
        mi = idade 
    if (idade > 18):
        maior = maior + 1 
    if(idade < 5):
        menor = menor + 1    
#media    
m = s / 10
print('A media da idade é {} anos \nHa {} pessoa maiores de 18 anos \nHa {} pessoas menores de 5 anos \nA maior idade foi {}'.format(m, maior, menor, mi))

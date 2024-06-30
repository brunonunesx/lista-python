#37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um 
#aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, 
#o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. 
#No final, mostre o seu novo salário, baseado na tabela a seguir:
#- Mulheres
# - menos de 15 anos de empresa: +5%
# - de 15 até 20 anos de empresa: +12%
# - mais de 20 anos de empresa: +23%
#- Homens
# - menos de 20 anos de empresa: +3%
# - de 20 até 30 anos de empresa: +13%
# - mais de 30 anos de empresa: +25%

print ('\033[1;35m-=\033[m'*15)
print('\033[1;34mAnalisando um triângulo\033[m')
print ('\033[1;35m-=\033[m'*15)

salário = float(input('Qual o salário do funcionário? '))
sexo = str(input('Qual o sexo do funcionário [M, F]? '))
ano = int(input('Quantos anos o funcionário trabalha na empresa? '))

if (sexo == 'F' ):
    print ('Seu salário atual é te {}R$'.format(salário))
    if (ano < 15 ):
        salário = salário + (salário * 5)/100
        print('\033[33m Seu novo salário é {}R$ \033[m'.format(salário))
    elif (ano >= 15) and (ano < 20):
        salário = salário + (salário * 12)/100
        print('\033[33m Seu novo salário é {}R$ \033[m'.format(salário))  
    else:
        salário = salario + (salário * 23)/100
        print('\033[33m Seu novo salário é {}R$ \033[m'.format(salário))
else:
    if (ano < 20 ):
        salário = salário + (salário * 3)/100
        print('\033[33m Seu novo salário é {}R$ \033[m'.format(salário))
    elif (ano >= 20) and (ano < 30):
        salário = salário + (salário * 13)/100
        print('\033[33m Seu novo salário é {}R$ \033[m'.format(salário))  
    else:
        salário = salário + (salário * 25)/100
        print('\033[33m Seu novo salário é {}R$ \033[m'.format(salário))
    
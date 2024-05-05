#29) Desenvolva um programa que leia o nome de um funcionário, seu salário, 
#quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de 
#acordo com a tabela a seguir:
 #- Até 3 anos de empresa: aumento de 3%
 #- entre 3 e 10 anos: aumento de 12.5%
 #- 10 anos ou mais: aumento de 20%
 
nome = str(input('Digite o nome do funcionário: '))
sal = float(input('Digite se salário: '))
ano = int(input('Digite a quantos anos o funcionário está na empresa '))
 
print('\033[1;32m-=\033[m'*15)
print('\033[1;34mCalculando o aumento de salário\033[m')
print('\033[1;32m-=\033[m'*15)
if(ano <= 3):
    sal = sal + (sal * 3/100)
    print('Seu novo salário é {}R$'.format(sal))
elif(ano > 3) and (ano <= 10):   
    sal = sal + (sal * 12.5/100)
    print('Seu novo salário é {}R$'.format(sal))
else:
    sal = sal + (sal * 20/100)
    print('Seu novo salário é {}R$'.format(sal)) 
    
    
#15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o 
#salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 
#por hora trabalhada.

dia = int(input ('Dias trabalhados: '))

sal = dia * 8 *25 

print('o funcionário receberá um valor de {} '.format(sal))

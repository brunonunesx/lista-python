#33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra 
#de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e 
#em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que 
#ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[1;35m-=\033[m'*20)
print ('\033[1;34m           Empréstimo Bancário\033[m')
print('\033[1;35m-=\033[m'*20)

casa = float(input ('Qual o valor da casa ?'))
salário = float(input ('Quando é seu salário '))
anos = int(input('Em quantos anos voce que paga'))

prestação = casa / (anos * 12)
condição = 30 * salário /100

if prestação > condição : 
    print('emprestimo negado')
else:
    print('emprestimo aceito')
    
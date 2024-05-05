#27) Crie um programa que leia duas notas de um aluno e calcule a sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
 #- Média 7.0 ou superior: APROVADO
 
nota1 = float(input('Digite o valor da nota do aluno: '))
nota2 = float(input('Digite o valor da nota do aluno: '))
 
media = (nota1 + nota2)/2
 
if(media <= 4.9):
    print('O aluno está de reprovado ')
elif(media >=5) and (media <=6.9):
    print ('O aluno está de recuperação ')
else:
    print ('O aluno está aprovado ')
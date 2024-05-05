#26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando 
#na tela uma das mensagens abaixo:
 #- O primeiro valor é o maior
 #- O segundo valor é o maior
 #- Não existe valor maior, os dois são iguais
 
num1 = int(input ('Digite um número inteiro: '))
num2 = int(input ('Digite outro número inteiro: '))
 
if(num1 > num2):
     print('{} O primeiro número e maior'.format(num1))
elif(num2 > num1):
    print('{} o segundo número é maior'.format(num2))
else:  
    print('{} e {} são iguais'.format(num1, num2))
print ('tenha um bom dia')   
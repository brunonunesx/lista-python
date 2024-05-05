#6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu 
#sucessor.
#Ex: 
#Digite um número: 9
#O antecessor de 9 é 8
#O sucessor de 9 é 10

num = int(input('Digite um número inteiro: '))
ant = num - 1
suc = num + 1 
print('O antecessor de {} é {} \nO sucessor de {} é {}'.format(num, ant, num, suc))

#53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
#a) Quantos homens foram cadastrados
#b) Quantas mulheres foram cadastradas
#c) A média de idade do grupo
#d) A média de idade dos homens
#e) Quantas mulheres tem mais de 20 anos

mulher = 0
homem = 0 
s = 0
sh = 0
tm = 0

for c in range (0, 5):
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo [M/F]: ')).upper()
    s = s + idade 
    if (sexo == 'M'):
        homem = homem + 1
        sh = sh + idade
    else:
        mulher = mulher + 1   
        if (idade > 20):
            tm = tm + 1 
            
            
m = s / 5
mh = sh / homem  
      
print('O total de homens é {} \nO total de mulheres é {} \nA média da idade do grupo é {} \nA média da idade  dos homens é {} \nHa {} mulheres acima de 20 anos'.format(homem, mulher, m, mh, tm))
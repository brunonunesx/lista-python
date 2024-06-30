#34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no 
#peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o 
#indivíduo dentro de certas faixas.
# - abaixo de 18.5: Abaixo do peso
# - entre 18.5 e 25: Peso ideal
# - entre 25 e 30: Sobrepeso
# - entre 30 e 40: Obesidade
# - acima de 40: Obseidade mórbida
#Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado 
#da altura)

print('\033[1;35m-=\033[m'*20)
print ('\033[1;34m     calculo de IMC\033[m')
print('\033[1;35m-=\033[m'*20)

altura = float(input('qual sua altura'))
peso = float(input('Qual é seu peso'))

imc = peso / altura**2

if (imc <= 18.5):
    print('Abaixo do peso')
elif (imc > 18.5) and (imc <= 25): 
    print('peso ideal')
elif (imc > 25 ) and (imc <= 30):
    print('sobrepeso')
elif (imc > 30) and (imc <= 40):
    print:('obesidade')
else:
    print('obesidade mórbida')    
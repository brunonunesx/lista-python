#17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 
#80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba 
#o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

vel = float(input('Qual a velocidade do carro em Km/h'))
print('A velocidade do carro foi {}Km/h'.format(vel))
if (vel > 80):
    print('Foi multado')
    valor = (vel - 80) * 5
    print('O valor para da multa é {}R$'.format(valor))
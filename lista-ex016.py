#16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um 
#fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele 
#já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule 
#quantos dias de vida um fumante perderá e exiba o total em dias.

quan = int(input('Digite a quantidade de cigarro que fuma por dia: '))
ano = int(input('Digite a quando anos vc fuma: '))

rd = quan * (ano * 365) * 1/144

print('Fumando {} cigarro por dia durante {} vc perde {:.2f} dias'.format(quan, ano, rd))
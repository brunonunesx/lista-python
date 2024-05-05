#19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua 
#média e mostre na tela. No final, analise a média e mostre se o aluno teve ou 
#não um bom aproveitamento (se ficou acima da média 7.0).

nome = str(input('Digite o nome do aluno '))
not1 = float(input('Digite a primeira nota do aluno {} '.format(nome)))
not2 = float(input('Digite a segunda nota do aluno {} '.format(nome)))
media = (not1 + not2)/2
print('A media das nota do aluno {} foi {}'.format(nome, media))
if (media > 7):
    print('deve um bom aproveitamento')
else:
    print('Não deve um bom aproveitamento') 
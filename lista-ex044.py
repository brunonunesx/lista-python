#44)Crie um algoritmo que leia o valor inicial da contagem, o valor final e o 
#incremento, mostrando em seguida todos os valores no intervalo:
#Ex: Digite o primeiro Valor: 3
#Digite o último Valor: 10
#Digite o incremento: 2
#Contagem: 3 5 7 9 Acabou!

inicial = int(input ('inicial: '))
final = int(input ('final: '))
incremento = int(input ('incremento: '))

for c in range (inicial, final+incremento, incremento):
    print (c)
print ('acabou') 
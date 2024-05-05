#28)Faça um programa que leia a largura e o comprimento de um terreno 
#retangular, calculando e mostrando a sua área em m². O programa também 
#devemostrar a classificação desse terreno, de acordo com a lista abaixo:
 #- Abaixo de 100m² = TERRENO POPULAR
 #- Entre 100m² e 500m² = TERRENO MASTER
 #- Acima de 500m² = TERRENO VIP
 
lar = float(input ('Digite a largura do terreno: '))
comp = float(input ('Digite o compromimemto do terreno: '))

print('-='*15)
print('Alanisando o terreno')
print('-='*15)

área = lar * comp
print('O terreno tem uma área de {}m²'.format(área))

if(área < 100):
    print ('Terreno popular')
elif(área >=100) and (área < 500):
    print('Terreno Master')   
else:
    print('Terreno VIP')
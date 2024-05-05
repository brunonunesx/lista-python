#30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo 
#de triângulo será formado: 
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes


print ('\033[1;35m-=\033[m'*15)
print('\033[1;34mAnalisando um triângulo\033[m')
print ('\033[1;35m-=\033[m'*15)
seg1 = int(input('Digite um número para o primeiro segmento do triângulo '))
seg2 = int(input('Digite um número para o segundo segmento do triângulo '))
seg3 = int(input('Digite um número para o terceiro segmento do triângulo '))

if (seg1+seg2 > seg3) and (seg1 + seg3 > seg2) and (seg3 + seg2 > seg1):
    print('\033[0;32mOs três segmento formam um triângulo\033[m')
    if(seg1 == seg2) and (seg1 == seg3):
        print('\033[33mEsse triângulo é equilátero\033[m')
    elif(seg1 !=  seg2) and (seg2 != seg3) and (seg3 != seg1):
        print('\033[33mEsse triângulo é escaleno\033[m')  
    else:
        print('\033[33mEsse triângulo é isoceceles\033[m') 
else:
    print('\033[31mOs três segmento não formam um triângulo\033[m')
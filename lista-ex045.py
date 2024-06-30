#45) O programa acima vai ter um problema quando digitarmos o primeiro valor 
#maior que o último. Resolva esse problema com um código que funcione em qualquer 
#situação.

inicial = int(input ('inicial: '))
final = int(input ('final: '))
incremento = int(input ('incremento: '))

if (inicial < final):
    for c in range (inicial, final+incremento, incremento):
        print (c)
else:
    for c in range (inicial, final-incremento, -incremento):
        print (c)
print ('acabou') 
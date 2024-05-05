#8) Desenvolva um programa que leia uma distância em metros e mostre os valores 
#relativos em outras medidas.
#Ex: 
#Digite uma distância em metros: 185.72
#A distância de 85.7m corresponde a:
#0.18572Km
#1.8572Hm
#18.572Dam
#1857.2dm
#18572.0cm
#185720.0mm

num = float(input('Digite uma distância em  metros: '))
km = num / 1000
hm = num / 100
dam = num / 10
dm = num * 10
cm = num * 100
mm = num * 1000
print('A distância de {}m corresponde a: '.format(num))
print('{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(km, hm, dam, dm, cm, mm))
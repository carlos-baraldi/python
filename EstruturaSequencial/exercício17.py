'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''


import math #importa o módulo math, para que possa usar a função math.ceil para arredondar o número para cima

area_m = float(input('Digite o valor em metros quadrados da área a ser pintada: '))

litros = area_m / 6

latag = litros / 18

ptotal_latasg = latag * 80

latap = litros / 3.6

ptotal_latasp = latap * 25

restolatag = (litros % 18) / litros

lataginteira = int(latag)

latapinteira = float(math.ceil(restolatag))

pmisturatotal = float((lataginteira * 80) + (latapinteira *25))

print(f' **Se o usuário comprar apenas latas de 18 litros, será necessário comprar {math.ceil(latag)} e gastará um total de {math.ceil(ptotal_latasg)}')

print(f' **Se o usuário comprar apenas galões de 3,6 litros, será necessário comprar {math.ceil(latap)} e gastará um total de {math.ceil(ptotal_latasp)}')

print(f'** Se o usuário for comprar tanto latas quanto galões será necessário comprar {lataginteira} latas e {latapinteira} galões. O valor gasto pelo usuário será de {pmisturatotal}')

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

celc = float(input('Digite o valor em graus Celcius'))

#fórmula para transformar graus celcius em farenheit " F = C × 1, 8 + 32"
fare = celc * 1.8 + 32

print(f'{celc} graus celcius equivalem a {fare} graus farenheit')

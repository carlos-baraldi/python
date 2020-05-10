#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

fahre = float(input('Digite o valor da temperatura em graus farenheit: '))

#fórmula para transformar graus farenheit em celcius " C = (F − 32) ÷ 1, 8 "
Celc =  (fahre - 32) / 1.8

print (f'{fahre} graus fahrenheit equivale a {Celc} graus Celcius')

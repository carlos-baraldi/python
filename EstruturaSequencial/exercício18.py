'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). '''

tam_arquivo = float(input('Digite o tamanho do arquivo para download (em MB): '))
vel_link = float(input('Digite a velocidade do link de internet (em Mbs): '))

tempo_segundos = tam_arquivo / vel_link
tempo_minutos = tempo_segundos / 60

print(f'O tempo aproximado de download do arquivo será de {round(tempo_minutos, 2)} minutos')
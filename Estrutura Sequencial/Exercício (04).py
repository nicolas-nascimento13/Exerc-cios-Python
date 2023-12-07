# Faça um Programa que converta metros para centímetros.

print('ATENÇÃO: esse conversor só converte de METROS PARA CENTÍMETROS')

metros = input('Informe o valor em metros: ')
metros = metros.replace(',', '.')
metros = float(metros)
centimetros = metros * 100

print(f'{metros} m em centímetros é {centimetros} cm')

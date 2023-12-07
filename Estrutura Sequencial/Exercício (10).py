# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_celsius = input('Informe a temperatura em Celsius: ')
temperatura_celsius = temperatura_celsius.replace(',', '.')
temperatura_celsius = float(temperatura_celsius)

conversor_para_fahrenheit = (temperatura_celsius * 9/5) + 32
conversor_para_fahrenheit = round(conversor_para_fahrenheit, 2)

print(f'{temperatura_celsius}°C equivale a {conversor_para_fahrenheit}°F')

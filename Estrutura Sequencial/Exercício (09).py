"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
temperatura_fahrenheit = input('Informe a temperatura em graus Fahrenheit: ')
temperatura_fahrenheit = temperatura_fahrenheit.replace(',', '.')
temperatura_fahrenheit = float(temperatura_fahrenheit)

conversor_para_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)
conversor_para_celsius = round(conversor_para_celsius, 2)

print(f'{temperatura_fahrenheit}°F equivale a {conversor_para_celsius}°C')

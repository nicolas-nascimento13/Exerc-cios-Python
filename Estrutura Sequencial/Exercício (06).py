# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = input('Informe o raio do círculo em centímetros: ')
raio = raio.replace(',', '.')
raio = float(raio)
raio = raio ** 2

print(f'A área desse circulo é {raio}π cm²')

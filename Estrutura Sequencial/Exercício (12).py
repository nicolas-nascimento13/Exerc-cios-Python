"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule
seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

altura = input('Informe sua altura (em metros): ')
altura = altura.replace(',', '.')
altura = float(altura)

peso_ideal = (72.7 * altura) - 58
peso_ideal = round(peso_ideal, 2)

print(f'Considerando a altura {altura}m, o peso ideal {peso_ideal}kg')

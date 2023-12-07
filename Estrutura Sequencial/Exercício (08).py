""" Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. """

reais_por_hora = input('Informe quanto você ganha por hora: ')
horas_por_mes = input('Informe quantas horas você trabalha por mês: ')

reais_por_hora = reais_por_hora.replace(',', '.')
reais_por_hora = float(reais_por_hora)
horas_por_mes = horas_por_mes.replace(',', '.')
horas_por_mes = float(horas_por_mes)

salario_mensal = reais_por_hora * horas_por_mes

print(f'Seu salário mensal é de R${salario_mensal}')

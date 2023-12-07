"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
"""

salario_por_hora = input('Digite quanto você ganha por hora: ')
salario_por_hora = salario_por_hora.replace('R$', '')
salario_por_hora = salario_por_hora.replace(',', '.')
salario_por_hora = float(salario_por_hora)
horas_por_mes = input('Informe quantas horas você trabalha por mês: ')
horas_por_mes = float(horas_por_mes)

# a) Salário Bruto

salario_bruto = salario_por_hora * horas_por_mes
salario_bruto = round(salario_bruto, 2)

# b) quanto pagou ao INSS

inss = salario_bruto * 0.08
inss = round(inss, 2)

# c) quanto pagou ao sindicato

sindicato = salario_bruto * 0.05
sindicato = round(sindicato, 2)

# *) Nas letras "d)" e "e)" exigem o cálculo do Imposto de Renda (IR), portanto o faremos aqui

imposto_de_renda = salario_bruto * 0.11
imposto_de_renda = round(imposto_de_renda, 2)

# INSS, Imposto de Renda e Sindicato são todos descontos da folha de pagamento, portanto calcularemos o desconto total

desconto_total = inss + sindicato + imposto_de_renda
desconto_total = round(desconto_total, 2)

# d) salário líquido

salario_liquido = salario_bruto - desconto_total
salario_liquido = round(salario_liquido, 2)

""" e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$ 
"""

print(f'+ Salário Bruto: R${salario_bruto}\n'
      f'- IR (11%): R${imposto_de_renda}\n'
      f'- INSS (8%): R${inss}\n'
      f'- Sindicato (5%): R${sindicato}\n'
      f'= Salário Líquido: R${salario_liquido}')

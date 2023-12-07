"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
e o preço total.
"""

area = input('Informe o tamanho da área em metros quadrados: ')
area = area.replace(',', '.')
area = float(area)

litros_necessarios = area / 3
litros_necessarios = round(litros_necessarios, 2)
quantidade_de_latas = int(litros_necessarios / 18) + 1

preco_total = quantidade_de_latas * 80

print(f'Será necessário comprar {quantidade_de_latas} latas de tinta, custando R${preco_total}')

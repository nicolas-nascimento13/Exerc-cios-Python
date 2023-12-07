"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
"""

area = input('Informe o tamanho da área em metros quadrados: ')
area = area.replace(',', '.')
area = float(area)

litros_necessarios = area / 6
litros_necessarios = round(litros_necessarios, 2)

# a) comprar apenas latas de 18 litros

quantidade_de_latas_18 = int(litros_necessarios / 18) + 1
preco_total_18 = quantidade_de_latas_18 * 80
print(f'Se você comprar somente latas de 18 litros, terá de comprar {quantidade_de_latas_18} latas num valor total '
      f'de R$ {preco_total_18}')
# b) comprar apenas galões de 3,6 litros

quantidade_de_latas_3_6 = int(litros_necessarios / 3.6) + 1
preco_total_3_6 = quantidade_de_latas_3_6 * 25
print(f'Se você comprar somente galões de 3,6 litros, terá de comprar {quantidade_de_latas_3_6} latas num valor total'
      f'de R${preco_total_3_6}')

# c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
# arredonde os valores para cima, isto é, considere latas cheias.

litros_necessarios_folga = litros_necessarios * 1.1
qtd_latas_c = litros_necessarios_folga // 18

litros_necessarios_folga_faltando = litros_necessarios_folga - (qtd_latas_c * 18)
qtd_galoes_c = int(litros_necessarios_folga_faltando / 3.6) + 1

custo_mix = (qtd_latas_c * 80) + (qtd_galoes_c * 25)

print("Mix de latas e galões:")
print(f'O cliente precisa comprar {qtd_latas_c} latas e {qtd_galoes_c} galões, que custarão {custo_mix}')

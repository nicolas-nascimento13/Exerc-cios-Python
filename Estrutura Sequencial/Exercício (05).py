# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

bimestre1 = float(input('Digite a nota do primeiro bimestre: '))
bimestre2 = float(input('Digite a nota do segundo bimestre: '))
bimestre3 = float(input('Digite a nota do terceiro bimestre: '))
bimestre4 = float(input('Digite a nota do quarto bimestre: '))

soma_das_notas = bimestre1 + bimestre2 + bimestre3 + bimestre4
media = soma_das_notas / 4

print(f'A média final foi {media}')

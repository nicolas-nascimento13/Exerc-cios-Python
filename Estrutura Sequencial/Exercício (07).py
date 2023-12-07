# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_do_quadrado = input('Informe o lado do quadrado em centímetros: ')
lado_do_quadrado = lado_do_quadrado.replace(',', ',')
lado_do_quadrado = float(lado_do_quadrado)

area = lado_do_quadrado ** 2
dobro_da_area = area * 2

print(f'A área do quadrado é {area} cm² e o dobro da área é {dobro_da_area} cm²')

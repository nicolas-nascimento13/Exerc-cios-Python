# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

numero1 = input('Digite o primeiro número inteiro: ')
numero2 = input('Digite o segundo número inteiro: ')
numero3 = input('Digite um número real: ')

numero1 = int(numero1)
numero2 = int(numero2)
numero3 = numero3.replace(',', '.')
numero3 = float(numero3)

# a) o produto do dobro do primeiro com metade do segundo

letra_a = (2 * numero1) * (numero2 / 2)
letra_a = round(letra_a, 2)
print(f'O produto do dobro do primeiro número com a metade do segundo número é {letra_a}')

# b) a soma do triplo do primeiro com o terceiro

letra_b = (3 * numero1) + numero3
letra_b = round(letra_b, 2)
print(f'A soma do triplo do primeiro número com o terceiro número é {letra_b}')

# c) o terceiro elevado ao cubo

letra_c = numero3 ** 3
letra_c = round(letra_c, 2)
print(f'O terceiro número elevado ao cubo é {letra_c}')

"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
"""
altura = input('Informe sua altura (em metros): ')
altura = altura.replace(',', '.')
altura = float(altura)

genero = input('Se você for homem digite 1, se você for mulher digite 2: ')
genero = int(genero)

if genero == 1:
    genero = 'masculino'
    peso_ideal = (72.7 * altura) - 58
    peso_ideal = round(peso_ideal, 2)
elif genero == 2:
    genero = 'feminino'
    peso_ideal = (62.1 * altura) - 44.7
    peso_ideal = round(peso_ideal, 2)
else:
    genero = 'null'
    peso_ideal = 'null'
    print('Informe uma entrada válida')

print(f'Considerando a altura {altura} e o gênero {genero}, o peso ideal é de {peso_ideal}kg')

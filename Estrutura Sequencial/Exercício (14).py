"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""

peso = input('Informe quantos Quilogramas (Kg) de peixe você pesou: ')
peso = peso.replace(',', ' .')
peso = float(peso)

if peso > float(50):
    excesso = peso - 50
    variavel = 4 * excesso
    print(f'Você pescou {peso}kg. Esse peso é maior do que o regulamento de pesca do estado de São Paulo permite \n'
          f'O peso excedente foi de {excesso}kg, logo o a multa que terá de pagar sairá no valor de R${variavel}')

"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_do_arquivo = input('Informe quantos MB o arquivo do download tem: ')
tamanho_do_arquivo = tamanho_do_arquivo.replace(',', '.')
tamanho_do_arquivo = float(tamanho_do_arquivo)
velocidade_internet = input('Qual é a velocidade da sua internet em Mbps: ')
velocidade_internet = velocidade_internet.replace(',', '.')
velocidade_internet = float(velocidade_internet)

tempo_aproximado = tamanho_do_arquivo / velocidade_internet
minutos = tempo_aproximado / 60
minutos = round(minutos, 2)
minutos_exatos = int(minutos)
decimal_do_minuto
segundos = (((minutos - int(minutos)) * 100) * 60)
segundos = round(segundos)
tempo_exato = str(int(minutos)) + str(segundos)
print(segundos)

print(f'Tamanho do aquivo: {tamanho_do_arquivo}MB\n'
      f'Velocidade da Internet: {velocidade_internet}Mbps\n'
      f'Tempo estimado de download: {minutos} minutos, ou {minutos_exatos} minutos e {segundos} segundos')

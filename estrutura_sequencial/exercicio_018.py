'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). '''

from estrutura_decisao.cabecalho import linha
linha('-', 'Tempo de download')

tamanha_arquivo = float(input('Informe o tamanho do arquivo em MB:  '))

velocidade_link = float(input('Informe a velocidade de download em Mbps:  '))

velocidade_final = velocidade_link / 8 # Converte Mbps em MBps

tempo_em_segundos = tamanha_arquivo / velocidade_final # calcula o tempo para realizar o download

tempo_em_minutos = tempo_em_segundos / 60 # converte o tempo de segundos para minutos

print(f'Um arquivo de {tamanha_arquivo} MB  com uma velocidade de {velocidade_link}Mbps levará aproximadamente {tempo_em_minutos:.2f} minutos para concluir o download')
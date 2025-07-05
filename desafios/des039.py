# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda se alistar ao serviço militar, se é a hora de se alistar, se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

import datetime
agora = datetime.datetime.now() # Puxando a data e a hora atuais
ano_atual = agora.year # Puxando o ano atual

anonasc = int(input('Digite o ano de nascimento: '))

idade = ano_atual - anonasc

if idade == 18:
    print('Está na hora de se alistar!')
elif idade > 18:
    print('Já passou do tempo!')
elif idade < 18:
    print('Está cedo!')
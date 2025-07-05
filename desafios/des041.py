# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos MIRIM, até 14 anos INFANTIL, até 19 anos JÚNIOR, até 20 anos SÊNIOR e acima MASTER

import datetime
agora = datetime.datetime.now()
ano_atual = agora.year

anonasc = int(input('Digite o ano de nascimento do atleta: '))

idade = ano_atual - anonasc

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 15 and idade <= 20:
    print('JÚNIOR')
else:
    print('MASTER')
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

from datetime import datetime

def voto(ano_nasc):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc
    if idade < 16:
        return 'VOTO NEGADO!!'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL!!'
    else:
        return 'VOTO OBRIGATÓRIO'

ano_nasc = int(input('Digite o seu ano de nascimento: '))
print(voto(ano_nasc))
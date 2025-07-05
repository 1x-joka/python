# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores

import datetime
maior = 0
menor = 0

for c in range(1, 8):
    anonasc = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - anonasc
    if idade >= 18:
        maior += 1 # Adicionando 1 ("pessoa") cada vez que essa condição for satisfeita
    else:
        menor += 1

print(f'{maior} pessoas já completaram a maioridade!!')
print(f'{menor} pessoas NÃO completaram a maioridade!!')
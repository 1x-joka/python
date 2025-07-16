# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} marcou {gols} gol(s) no campeonato'

nome = input('Digite o nome do jogador: ')
gols = input('Digite a quantidade de gols que ele marcou: ') # Não coloca int pois pode dar erro

if nome == '':
    nome = '<desconhecido>'
if gols.isdigit(): # Verifica se a variável gols é uma string que contém só números
    gols = int(gols) # Converte essa string pra um número inteiro e guarda esse número na variável gols
else:
    gols = '<desconhecido>'

print(ficha(nome, gols))
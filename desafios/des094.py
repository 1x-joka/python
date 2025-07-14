# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: a) Quantas pessoas foram cadastradas; b) A média de idade do grupo; c) Uma lista com todas as mulheres; d) Uma lista com todas as pessoas com idade acima da média

from time import sleep

pessoas = []
soma_idade = 0

print('-='*20)
print(f'{"Programa Cálculo":^40}')
print('-='*20)

while True:
    dados = dict() # Não pode ficar antes desse while pois eu estarei sobrescrevendo cada pessoa quando der loop
    dados['nome'] = input('Digite seu nome: ').strip()
    while True:
        dados['sexo'] = input('Digite seu sexo: ').strip().upper()[0]

        if dados['sexo'] in 'MF':
            break
        print('[ERRO] Digite apenas M ou F')

    dados['idade'] = int(input('Digite sua idade: '))
    soma_idade += dados['idade'] # Somando as idades digitadas
    pessoas.append(dados.copy()) # Copiando todo o dicionário na lista

    escolha = input('Quer continuar?[S/N]: ').strip().upper()[0]
    if escolha == 'N':
        break
    elif escolha != 'S':
        print('Inválido, assumindo que SIM...')

print('-='*20)
print(f'{"Calculando...":^40}')
print('-='*20)
sleep(1)

print(f'Foram cadastradas {len(pessoas)} pessoas')
media = soma_idade / len(pessoas)
print(f'A média das idades é {media:.2f} anos')

# Lista de Mulheres:
mulheres = []
for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p['nome']) # Guardando o nome das mulheres na lista 'mulheres'
print(f'As mulheres da lista são {mulheres}')

# Pessoas acima da média:
print('Pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print(f'Nome: {p["nome"]}, Sexo: {p["sexo"]}, Idade: {p["idade"]}')

# ERROS:
# lista.append(dados['idade'][:]) --> Não faz sentido pois INT é infatiável
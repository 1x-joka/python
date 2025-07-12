# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a) Quantas pessoas foram cadastradas; b) Uma listagem com as pessoas mais pesadas; c) Uma listagem com as pessoas mais leves

pessoas = list()
qtd = 0
maior = menor = 0

while True:
    nome = input('Digite o nome da pessoa: ')
    peso = int(input('Digite o peso, em kg, da pessoa: '))
    pessoas.append([nome, peso])
    qtd += 1

    if len(pessoas) == 1: # Se só tiver 1 pessoa cadastrada...
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            
    escolha = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if escolha == 'N':
        break
    elif escolha != 'S':
        print('Inválido, assumimos que SIM...')
        
maiorpeso = []
menorpeso = []

for indice in range(len(pessoas)):
    if pessoas[indice][1] == maior: # Para cada PESO de pessoa...
        maiorpeso.append(pessoas[indice][0]) # Adiciona o NOME dela na lista maiorpeso
    elif pessoas[indice][1] == menor:
        menorpeso.append(pessoas[indice][0])

print(f'{qtd} pessoas foram cadastradas')
print(f'O maior peso foi {maior}kg. Pessoa mais pesada: {maiorpeso}')
print(f'O menor peso foi {menor}kg. Pessoa mais leve: {menorpeso}')
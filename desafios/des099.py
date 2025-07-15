# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar os valores e dizer qual deles é maior

def maior(*lista):
    print(f'Os números digitados foram: {lista}')
    print(f'Foram digitados {len(lista)} valores')
    print(f'O maior número dela foi {max(lista)}')

n = 0
lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    escolha = input('Quer continuar?[S/N]: ').strip().upper()[0]
    if escolha == 'N':
        break
    elif escolha != 'S':
        print('Inválido, assumimos que SIM...')

maior(*lista)
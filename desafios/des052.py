# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

numero = int(input('Digite um número inteiro: '))

total = 0
for c in range(1, numero + 1): # Para ser primo, só pode ser divisível por 1 e por ele mesmo, então vamos verificar todos os números entre ele
    if numero % c == 0:
        print('\033[32m', end = ' ')
        total += 1
    else:
        print('\033[31m', end = ' ')
    print(c, end = ' ')

print('\033[m', end=' ') # Resetando a cor
print(f'\nO número {numero} foi divisível {total} vezes')

if total == 2: # Se o número for divisível 2 vezes (1 e ele mesmo)
    print('É PRIMO!!')
else:
    print('NÃO É PRIMO!!')
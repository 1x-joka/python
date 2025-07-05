# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termos são: ')

for c in range(1, 11):
    cadatermo = primeirotermo + (c - 1)*razao # c-1 pois o primeiro termo da PA é ele mesmo (posição 0)
    print(cadatermo, end=' ')
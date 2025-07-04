# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO

nome = input('Digite o nome de uma cidade: ')

dividido = nome.split()

print(dividido[0].upper() == 'SANTO')
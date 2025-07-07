# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando uma estrutura while

primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeirotermo
contador = 1

while contador <= 10:
    print(f'{termo}', end=' ')
    termo += razao # Atualiza o termo adicionando a razão a ele
    contador += 1 # Para bater no 10 depois
print('\nFIM')
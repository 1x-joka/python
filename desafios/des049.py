# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora usando um laço for

numero = int(input('Digite o número que você deseja realizar a tabuada: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(numero, c, numero*c))
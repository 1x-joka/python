# Aprimore o desafio anterior (matriz), mostrando no final: a) A soma de todos os valores pares digitados; b) A soma dos valores da terceira coluna; c) O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = 0
maior = 0
scoluna = 0

# FOR de alimentação:
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor na posição [{linha}, {coluna}]: '))

# FOR visual:
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0: # Após mostrar, o programa vai verificar cada elemento par
            spar += matriz[linha][coluna] # Somando eles
    print()

print('-='*30)
print(f'A soma dos valores pares é {spar}')

for linha in range(0, 3): # Faremos apenas um for para a linha, pois é ela quem varia, a terceira coluna é fixa
    scoluna += matriz[linha][2] # Somamos todos os valores da terceira coluna (que é a coluna 2)
print(f'A soma dos valores da terceira coluna é {scoluna}')

for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maior: # Se o programa estivar na primeira coluna, ele já é o maior OU se ele estiver na segunda linha e for maior do que o maior atualmente (que seria o elemento da primeira coluna), ele atribui esse valor na variável maior
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')
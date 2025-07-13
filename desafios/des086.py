# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores do teclado. No final, mostre a matriz na tela, com a formatação correta

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# FOR de alimentação
for linha in range(0, 3):
    for coluna in range(0, 3): # Para cada linha, haverá 3 colunas
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: ')) # Adicionando um valor para cada linha e coluna
print('-='*30)

# FOR visual
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='') # Mostra um do lado do outro (5 espaços centralizados)
    print() # Toda vez que ele terminar a coluna, ele quebra a linha

# EXEMPLO:
# for linha in range(0, 3):
#    for coluna in range(0, 6):
# Explicação: para cada linha (que serão 3) haverá 6 colunas
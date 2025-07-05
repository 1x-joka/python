# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end = ' ') # Usamos o end para não quebrar a linha, e sim somente dar um espaço
print('ACABOU!')
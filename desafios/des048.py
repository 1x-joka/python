# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

s = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0: # Condição
        s += c
print('A soma é {}'.format(s))
print('ACABOU!!!')
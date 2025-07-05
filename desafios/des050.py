# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitador for ímpar, desconsidere-o

s = 0
for c in range(1, 7):
    numero = int(input('Digite o {}° número inteiro: '.format(c)))
    if numero % 2 == 0:
        s += numero
print('A soma de todos os números pares digitados é {}'.format(s))
print('ACABOU!!')
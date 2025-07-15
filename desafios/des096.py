# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno

l = float(input('Digite a largura do terreno(em metros): '))
c = float(input('Digite o comprimento do terreno(em metros): '))

def area(a, b):
    s = a * b
    print(f'A área do terreno é de {s}m²')

area(l, c)
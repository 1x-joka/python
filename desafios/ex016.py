# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc as parteinteira

n1 = float(input('Digite um número: '))

print('A sua porção inteira é: {}'.format(parteinteira(n1)))
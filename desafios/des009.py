# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n1 = int(input('Digite um número inteiro: '))

print('='*10, 'TABUADA DO {}'.format(n1), '='*10)

print('{} x 1 = {} \n{} x 2 = {} \n{} x 3 = {} \n{} x 4 = {} \n{} x 5 = {} \n{} x 6 = {} \n{} x 7 = {} \n{} x 8 = {} \n{} x 9 = {} \n{} x 10 = {}'.format(n1, n1, n1, n1*2, n1, n1*3, n1, n1*4, n1, n1*5, n1, n1*6, n1, n1*7, n1, n1*8, n1, n1*9, n1, n1*10))
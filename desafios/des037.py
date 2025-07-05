# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão: 1 para binário, 2 para octal e 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
comp = int(input('Escolha uma base de conversão: \n[ 1 ]-Binário \n[ 2 ]-Octal \n[ 3 ]-Hexadecimal \nSua opção:'))

if comp == 1:
    print('O número {} em binário é {}'.format(num, bin(num)))
elif comp == 2:
    print('O número {} em octal é {}'.format(num, oct(num)))
elif comp == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)))
else:
    print('[ERRO] Digite um valor válido!')
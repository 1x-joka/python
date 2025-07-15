# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior

from random import randint
from time import sleep

numeros = []

def sorteia():
    print('Sorteando 5 números..')
    for cont in range(5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('\nSorteados!')

def somaPar():
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Os valores pares somados fica {soma}')

# Programa Principal
sorteia()
somaPar()
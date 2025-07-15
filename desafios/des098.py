# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: a) De 1 até 10, de 1 em 1; b) De 10 até 0, de 2 em 2; c) Uma contagem personalizada

from time import sleep

def contador(i, f, p):
    print(f'\nContando de {i} até {f} de {p} em {p}: ')

    if i < f: # Caso esteja de frente para trás...
        cont = i
        while cont <= f:
            print(cont, end=' ')
            sleep(0.3)
            cont += p
    else: # Caso esteja de trás para frente...
        cont = i
        while cont >= f:
            print(cont, end=' ')
            sleep(0.3)
            cont -= p

contador(1, 10, 1) # Contagem de 1 até 10 de 1 em 1
contador(10, 0, 2) # Contagem de 10 até 0 de 2 em 2

# Contagem personalizada
print('\nAgora é a vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
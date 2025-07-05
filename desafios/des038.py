# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é maior, o segundo valor é maior, não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))

if n1 > n2:
    print('O primeiro valor é maior!')
elif n1 < n2:
    print('O segundo valor é maior!')
else:
    print('Os dois valores são iguais!')
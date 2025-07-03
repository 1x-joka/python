# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input('Digite um valor(m): '))

cm = n * 100
mm = n * 1000

print('O valor {}m equivale a {}cm e {}mm'.format(n, cm, mm))
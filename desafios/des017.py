# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))


h = (co)**2 + (ca)**2

print('A hipotenusa do triângulo retângulo é {}'.format(sqrt(h)))
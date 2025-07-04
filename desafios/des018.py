# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

a = float(input('Digite um ângulo, em graus: '))

a1 = math.radians(a)

print('O ângulo de {} tem SENO = {:.2f}'.format(a, math.sin(a1)))
print('O ângulo de {} tem COSSENO = {:.2f}'.format(a, math.cos(a1)))
print('O ângulo de {} tem TANGENTE = {:.2f}'.format(a, math.tan(a1)))
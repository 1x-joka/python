import math # Importando toda a biblioteca de Matemática
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é, arredondado para cima, {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é, arredondado para baixo, {}'.format(num, math.floor(raiz)))

from math import sqrt as raizquadrada # Importando nomeando
print('A raiz de {} é igual a {}'.format(num, raizquadrada(num))) # Outra forma de se fazer

from math import sqrt, floor, pow, ceil # Importando um por um e NÃO nomeando

import random # Importando toda a biblioteca random (utilizada para criar números aleatórios)
num = random.random() # Gerando um número aleatório entre 0 e 1
num2 = random.randint(1, 10) # Gerando um número inteiro de 1 a 10

print(num)
print(num2)

# Para explorar todas as bibliotecas e funcionalidades dentro delas é só ir para python.org na aba PyPI e Docs

import emoji
print(emoji.emojize("Olá Mundo :smiling_face_with_horns:")) # Adicionando emoji
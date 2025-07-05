# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero todos os lados iguais, Isósceles dois lados iguais e Escaleno todos os lados diferentes

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Fecha um triângulo!')
else:
    print('NÃO fecha um triângulo!')

if r1 == r2 == r3:
    print('EQUILÁTERO')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('ISÓSCELES')
else:
    print('ESCALENO')
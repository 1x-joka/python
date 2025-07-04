# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se pode ou não formar um triângulo

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # Cada lado de um triângulo é menor que a soma dos outros dois
    print('Fecha um triângulo!')
else:
    print('NÃO fecha um triângulo!')
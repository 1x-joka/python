# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = float(input('Digite um número: '))

print('O número digitado foi {}. Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n, n*2, n*3, n**(1/2)))
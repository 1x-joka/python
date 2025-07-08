# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando for solicitado um número negativo

print('='*20, 'Programa Tabuada', '='*20)

while True:
    num= int(input('Digite outro número inteiro: '))
    if num < 0:
        break
    cont = 1
    while cont < 10:
        cont += 1
        print(f'{num} x {cont} = {num*cont}')
print('~'*30)
print('[ERRO] Número Negativo!')
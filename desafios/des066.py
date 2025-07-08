# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

print('='*20, 'Programa 999', '='*20)
num = int(input('Digite um número inteiro: '))
soma = num
qtd = 1

while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    soma += num
    qtd += 1
print('~'*30)
print(f'Foram digitado {qtd} números e a soma entre eles é {soma}')
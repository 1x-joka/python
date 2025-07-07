# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

numero = int(input('Digite um número inteiro: '))
qtd = 0
soma = numero

while numero != 999:
    soma += numero
    qtd += 1
    numero = int(input('Digite um número inteiro: ')) # Colocamos no final para o programa poder conferir se o valor digitado NÃO foi o 999
print(f'Foram digitados {qtd} números e a soma entre eles é {soma}')
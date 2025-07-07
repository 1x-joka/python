# Crie um programa que leia vários números inteiros pelo teclado. No final, da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

numero = int(input('Digite um valor inteiro: '))
opcao = input('Quer continuar? [S/N]: ').strip().upper()[0]
maior = menor = numero
soma = numero
qtd = 1

while opcao == 'S':
    numero = int(input('Digite um valor inteiro: '))
    opcao = input('Quer continuar? [S/N]: ').strip().upper()[0]
    soma += numero
    qtd += 1

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    
media = soma / qtd

print(f'A média dos números digitados é {media}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
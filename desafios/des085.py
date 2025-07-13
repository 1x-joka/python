# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

valores = [[], []] # Valores[0] = pares e Valores[1] = ímpares

for cont in range(1, 8):
    num = int(input(f'Digite o {cont} valor: '))

    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
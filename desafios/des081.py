# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: a) Quantos números foram digitados; b) A lista de valores, ordenada de forma decrescente; c) Se o valor 5 foi digitado e está ou não na lista

lista = []

while True:
    n = int(input('Digite um valor na lista: '))
    lista.append(n)

    if n == 5:
        print('Você digitou o número 5!')

    opcao = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao != 'S':
        print('Resposta inválida, assumindo que quer continuar...')

print(f'Os valores digitados foram: {lista}')
print(f'Foram digitados {len(lista)} números na lista')
lista.sort(reverse=True)
print(f'A lista, em ordem decrescente, fica: {lista}')

if 5 in lista:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 não foi digitado e não está na lista')
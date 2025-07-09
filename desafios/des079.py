# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

lista = []

print('='*30)
print('Programa Quantidade')
print('='*30)

while True:
    n = int(input('Digite um número: '))

    if n not in lista:
        lista.append(n)
    else:
        print('Valor ja adicionado, tente novamente!')
    
    opcao = input('Quer continuar? [S/n]: ').strip().upper()[0]

    if opcao == 'N':
        break

print('~'*50)
lista.sort() # Precisa colocar em ordem crescente antes
print(f'Os valores adicionados, em ordem crescente, foram: {lista}')
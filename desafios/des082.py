# Crie um programa que vai ler vários números e colocar na lista. Depois disso, crie duas listas extras que vão contem apenas os valores pares e valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

lista = []
listapar = [] # Não pode criar dentro do if ou else pois elas serão zeradas a cada loop
listaimpar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    
    opcao = input('Quer continuar?[S/N]: ').strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao != 'S':
        print('Resposta inválida, assumindo que quer continuar...')

print(f'Os valores da lista par foram: {listapar}')
print(f'Os valores da lista ímpar foram: {listaimpar}')
print(f'Os valores da lista normal foram: {lista}')
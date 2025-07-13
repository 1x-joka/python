# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

boletim = list()

while True:
    nome = input('Digite o nome do aluno: ')
    n1 = int(input('Digite a primeira nota dele: '))
    n2 = int(input('Digite a segunda nota dele: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    escolha = input('Quer continuar?[S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
    elif escolha != 'S':
        print('Inválido, assumimos que sim...')

for indice, aluno in enumerate(boletim):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}') # Imprime o número/posição do aluno (indice), o nome dele (aluno[0]) e a média dele (aluno[2])

# Mostrando as notas individualmente
while True:
    opcao = int(input('\nDeseja mostrar as notas de qual aluno? (999 para interromper): '))
    if opcao == 999:
        break
    if 0 <= opcao < len(boletim): # Só pode digitar um número entre 0 e o comprimento da lista (se tiver só dois elementos, 1)
        print(f'As notas de {boletim[opcao][0]} são: {boletim[opcao][1]}') # boletim[opcao][0] = Nome; boletim[opcao][1] = notas; boletim[opcao][2] = média
    else:
        print('Número Inválido')
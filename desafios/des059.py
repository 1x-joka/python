# Crie um programa que leia dois valores e mostre um um menu na tela: [ 1 ] - Somar; [ 2 ] - Multiplicar; [ 3 ] - Maior; [ 4 ] - Novos Números; [ 5 ] - Sair do Programa. Seu programa deverá realizar a operação solicitada em cada caso

print('='*15 + 'PROGRAMA INTERATIVO' + '='*15)
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

resposta = 0

while resposta != 5:
    print('''
    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Sair do Programa
    ''')
    resposta = int(input('Sua Opção: '))

    if resposta == 1:
        soma = n1 + n2
        print(f'\033[32mA soma dos números digitados é {soma}\033[m')
    elif resposta == 2:
        mult = n1 * n2
        print(f'\033[32mO produto dos números digitados é {mult}\033[m')
    elif resposta == 3:
        if n1 > n2:
            print(f'\033[32m{n1} é maior do que {n2}\033[m')
        else:
            print(f'\033[32m{n2} é maior do que {n1}\033[m')
    elif resposta == 4:
        n1 = float(input('Digite um novo valor: '))
        n2 = float(input('Digite um outro novo valor: '))
    elif resposta == 5:
        print('\033[31mPROGRAMA ENCERRADO!\033[m') # Não colocamos exit() pois o while ja encerrado quando for 5
    else:
        print('\033[31m[ERRO] Digite respostas válidas\033[m')
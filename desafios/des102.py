# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(n=1, show=False):
    fat = 1
    for cont in range(n, 0, -1):
        if show == True:
            print(cont, end=' ')
            if cont > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        fat *= cont
    return fat

n = int(input('Digite um número: '))
mostrar = input('Deseja mostrar o processo:[S/N]: ').strip().upper()[0]

if mostrar == 'S':
    print(fatorial(n, show=True))
else:
    print(f'O fatorial de {n} é {fatorial(n)}')
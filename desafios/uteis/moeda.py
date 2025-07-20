def aumentar(n = 0, formato=False):
    res = n + 1
    return res if formato is False else moeda(res)

def diminuir(n = 0, formato=False):
    res = n - 1
    return res if formato is False else moeda(res)

def dobro(n = 0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)

def metade(n = 0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)

def moeda(n = 0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')

def resumo(n = 0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: {n}')
    print(f'Dobro do preço: {dobro(n, True)}')
    print(f'Metade do preço: {metade(n, True)}')
    print(f'Aumento de: {aumentar(n, True)}')
    print(f'Diminuição de: {diminuir(n, True)}')
    print('-'*30)
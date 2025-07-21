def leiaInt(n):
    while True:
        try:
            n = int(input(n))
        except (TypeError, ValueError):
            print('[ERRO] Por favor, digite um número inteiro válido!')
        except KeyboardInterrupt:
            print('[ERRO] Digite alguma coisa no teclado!')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
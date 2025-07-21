# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade na digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

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
    
def leiaFloat(n):
    while True:
        try:
            n = float(input(n))
        except (TypeError, ValueError):
            print('[ERRO] Por favor, digite um número inteiro válido!')
        except KeyboardInterrupt:
            print('[ERRO] Digite alguma coisa no teclado!')
            return 0
        else:
            return n
n = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n}')
print(f'O número real digitado foi {n2}')
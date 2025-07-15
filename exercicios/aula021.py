# help(print) --> INTERACTIVE HELP
# print(input.__doc__) --> INTERACTIVE HELP

def contador(i, f, p):
    """ # Criando a DOCSTRING
    --> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal Curso em Vídeo
    """
    c = i
    while c <= f:
        print(c, end='')
        c += p
    print('\nFIM')
help(contador)

print('*'*50)

def somar(a=0, b=0, c=0): # PARÂMETROS OPCIONAIS
    """
    --> Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :type a: float (real)
    :param b: o segundo valor
    :type b: float (real)
    :param c: o terceiro valor
    :type c: float (real)
    """
    s = a + b + c
    print(f'A soma entre {a}, {b} e {c} é {s}')

somar(3.4, 2, 5)
somar(3, 2)
somar()
somar(b=4, c=2)
somar(c=3, a=2)

print('*'*50)

def teste():
    x = 8 # Variável Local (pega somente aqui dentro)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa Principal
n = 2 # Variável Global (pega no programa todo)
print(f'No programa principal, n vale {n}')
teste()
# print(f'No programa principal, x vale {x}') --> ERRO, pois a variável x foi criada dentro da função --> Escopo Local

print('*'*50)

def funcao():
    n1 = 4
    print(f'n1 dentro(local) vale {n1}')

n1 = 2
print(f'n1 fora(global) vale {n1}')
funcao()

print('*'*50)

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)

print(f'Meus cálculos foram: {r1}, {r2} e {r3}')

print('*'*50)

def fatorial(num=1):
    f = 1
    for cont in range(num, 0, -1): # Começa no número, vai até 0 e volta de 1 em 1
        f *= cont
    return f

n = int(input('Digite um número: '))
print(fatorial(n))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2} e {f3}')

print('*'*50)

def parOuImpar(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

num2 = int(input('Digite um número: '))
print(parOuImpar(num2))

if parOuImpar(num2): # Se num2 for par...
    print('É par!')
else:
    print('É ímpar!')
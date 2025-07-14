def lin():
    print('-'*30)

# Programa Principal
lin()
print('       CURSO EM VÍDEO      ')
lin()
lin()
print('       APRENDA PYTHON      ')
lin()
lin()
print('       GUSTAVO GUANABARA       ')
lin()

print('**'*40)

def título(txt):
    print('-'*30)
    print(txt) # Imprime o texto la em cima
    print('-'*30)

# Programa Principal
título('       CURSO EM VÍDEO      ') # Joga essa mensagem dentro do 'txt' la em cima e aplica a função
título('       PYTHON É MUITO BOM      ')
título('            Oi          ')

print('**'*40)

a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

print('**'*40)

def soma(a, b): # 'soma' vai receber 'a' e 'b' (parâmetros)
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

soma(a=4, b=5)
soma(b=4, a=5)

print('**'*40)

def contador(* num):
    print(f'Recebi os valores {num} e são ao todo {len(num)} números')
    for valor in num:
        print(valor, end=' ')
    print('\nFIM')

# Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print('**'*40)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2 # Dobrando cada valor da lista 'valores'
        pos += 1

# Programa Principal
valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores) # Ele vai criar uma lista valores e jogar la pra cima (lista)
print(f'A lista com os elementos dobrados fica: \n{valores}')

print('**'*40)

def soma2(* valores2):
    s2 = 0
    for num in valores2: # Para cada número em 'valores2' (que no caso é soma2)
        s2 += num # Irei somar os números
    print(f'Somando os valores {valores2} temos {s2}')

# Programa Principal
soma2(5, 2)
soma2(2, 9, 4)
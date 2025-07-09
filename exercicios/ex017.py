num = (2, 5, 9, 1) # Tupla
print(num)

num = [2, 5, 9, 1]
num[2] = 3 # Manipulando a lista, LISTAS SÃO MUTÁVEIS
num.append(7) # Adicionando 7 no final da lista
num.sort() # Colocando em ordem crescente
num.sort(reverse=True) # Colocando em ordem decrescente
num.insert(2, 2) # Quero inserir o 2 na posição 2 (arrasta os demais para a direita e encaixa ele)
num.remove(2) # Deleta o PRIMEIRO elemento 2

if 4 in num:
    num.remove(4) # Se o 4 estiver na lista, ele é removido
else:
    print('Não achei o número 4')

num.pop() # Deletando o último elemento da lista
num.pop(2) # Deletando o número na posição 2
print(f'Essa lista tem {len(num)} elementos')

print('='*30)

valores = [] # ou: list()
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores: # Para cada elemento da minha lista...
    print(f'O valor {valor}...')

print('='*30)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: '))) # Guarda o valor digitado já dentro da lista

for chave,valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}')
print('Cheguei ao final da lista')

print('='*30)

a = [2, 3, 4, 7]
b = a # Cria uma ligação, e não uma cópia
b = a[:] # Cria uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
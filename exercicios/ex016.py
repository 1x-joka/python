# Criando a Tupla
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') # Podemos criar tupla com ou sem parênteses
# lanche[1] = 'Refrigerante' --> ERRO, tuplas são IMUTÁVEIS
print(lanche)

# Fatiamentos
print(lanche[1])
print(lanche[0])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])

for cont in range(0, len(lanche)): # Contando quantos itens tem na tupla, terminando no comprimento dela (5) mas ignora o último
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') # Fala o nome do lanche que está na posição "cont"

print('='*30)

for comida in lanche: # Usando "for" como "itens" e não como "range"
    print(f'Eu vou comer {comida}')
print('Comi para caramba!')

print('='*30)

for pos, comida in enumerate(lanche): # enumerate me da tanto o dado quanto a posição (por conta disso, tem que colocar o pos na variável)
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi para caramba!')

print('='*30)

print(sorted(lanche)) # Coloca em ordem alfabética

print('='*30)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c) # Cria uma nova tupla (cola a tupla a na tupla b)
print(c.count(5)) # Quantas vezes está aparecendo o número 5 dentro de c?
print(c.index(8)) # Mostra em que posição está o 8
print(c.index(2)) # Mostra a PRIMEIRA ocorrência do 2
print(c.index(5, 1)) # Mostra a PRIMEIRA ocorrência do 5 A PARTIR da posição 1

print('='*30)

pessoa = ('Gustavo', 39, 'Masculino', 99.88) # Em linguagens como Java por exemplo, isso não é possível, todos os dados têm que ser do mesmo tipo, no Python isso não se aplica
del(pessoa) # Deletando a variável toda
del(pessoa[0]) # Não é possível, pois uma tupla é imutável
print(pessoa)
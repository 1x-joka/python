# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma listagem de preços, organizando os dados de forma tabular

nomesprecos = (
    'Lápis', 1.50, # Observação! O nome do produto sempre está em uma posição par e o preço sempre em uma ímpar
    'Caneta', 2.00,
    'Caderno', 15.90,
    'Mochila', 120.00,
    'Borracha', 0.75,
    'Apontador', 1.25,
    'Estojo', 10.00,
    'Livro', 45.90
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for item in range(0, len(nomesprecos)): # Usamos for para analisar cada elemento da tupla e saber a posição de cada um / len para parar apenas quando der a quantidade de itens da tupla
    if item % 2 == 0:
        print(f'{nomesprecos[item]:.<30}', end='') # Alinhando o texto à esquerda e completando o espaço com "."
    else:
        print(f'R${nomesprecos[item]:>5.2f}') # .2f para mosrar 2 casas decimais
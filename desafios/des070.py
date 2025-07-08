# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: a) Qual é o total gasto na compra; b) Quantos produtos custam mais de R$1000; c) Qual é o nome do produto mais barato

print('='*20, 'Programa Produtos', '='*20)
total = qtdmil = menorpreco = 0
nomeprodbarato = ''

while True:
    nomeprod = input('Escreva o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    if preco > 1000:
        qtdmil += 1
    if total == preco or preco < menorpreco: # O preço atual é menor que o menor preço digitado? 
        menorpreco = preco # Ele passa a ser o menor preço
        nomeprodbarato = nomeprod # E atualiza o nome
    escolha = input('Quer continuar? [S/N]').strip().upper()[0]
    if escolha == 'N':
        break
print(f'O total gasto foi de R${total}')
print(f'No carrinho, {qtdmil} produtos custam mais de R$1000,00')
print(f'O produto mais barato é o {nomeprodbarato}')
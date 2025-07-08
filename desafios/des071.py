# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1

print('='*30)
print('{:^30}'.format('Banco CEV'))
print('='*30)

valor = int(input('Digite o valor (inteiro) a ser sacado: R$'))
total = valor # Montante
ced = 50 # Começando com a cédula de maior valor
totalcedulas = 0 # Total de cédulas que eu tenho que dar

while True:
    if total >= ced: # Se eu puder tirar 50...
        total -= ced # Tira 50
        totalcedulas += 1 # Quantas notas de 50 foram tiradas
    else: # Caso o total seja menor que 50...
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} cédulas de R${ced}')
        if ced == 50: # Se a cédula atual for 50 (não consigo tirar mais)
            ced = 20 # A próxima será 20, e fará a conta do primeiro if novamente
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalcedulas = 0 # Já houve todas as conversões
        if total == 0: # Se o dinheiro acabar...
            break

print('='*30)
print('Volte sempre ao Banco CEV, tenha um bom dia!')
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: À vista dinheiro/cheque 10% DE DESCONTO, À vista no cartão 5% DE DESCONTO, Em até 2x no cartão PREÇO NORMAL e 3x ou mais no cartão 20% DE JUROS

preco_atual = float(input('Digite o valor da compra: R$'))

print("""
Escolha a forma de pagamento...
[ 1 ] - À vista no dinheiro/cheque (10% de desconto)
[ 2 ] - À vista no cartão (5% de desconto)
[ 3 ] - Até 2x no cartão
[ 4 ] - 3x ou mais no cartão (20% de juros) """)

condicoes = int(input('Selecione: '))

if condicoes == 1:
    preco_atual *= 0.90
    print('O preço do produto fica em R${:.2f}'.format(preco_atual))
elif condicoes == 2:
    preco_atual *= 0.95
    print('O preço do produto fica em R${:.2f}'.format(preco_atual))
elif condicoes == 3:
    parcela = preco_atual / 2
    print('O preço do produto, dividido em 2x, fica em R${:.2f} SEM JUROS'.format(parcela))
elif condicoes == 4:
    total = preco_atual + ((preco_atual * 20) / 100)
    totalparcelas = int(input('Quantas parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparcelas, parcela))
else:
    print('[ERRO] INSIRA UM VALOR VÁLIDO!')
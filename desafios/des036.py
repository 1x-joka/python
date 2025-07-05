# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valorcasa = float(input('Digite o valor avaliado da casa: R$'))
salariocomp = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite em quantos anos ele vai pagar: '))

prestacao = valorcasa / (anos * 12)
salariocompnovo = (salariocomp * 30) / 100

if prestacao > salariocompnovo:
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO CONCEDIDO!')
print('Para comprar uma casa de R${:.2f} em {:.2f} anos, a prestação mensal será de R${:.2f}'.format(valorcasa, anos, prestacao))
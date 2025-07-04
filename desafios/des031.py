# Desenvolva um programa que pergunte a distância de uma viagem em km, calcule o preço da passagem do ônibus cobrando R$0.50 por km para viagens de até 200km e R$0.45 por km para viagens mais longas

d = float(input('Digite a distância da viagem, em km: '))

if d <= 200:
    c1 = d * 0.50
    print('Terá que pagar R${}'.format(c1))
else:
    c2 = d * 0.45
    print('Terá que pagar R${}'.format(c2))
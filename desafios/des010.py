# Crie um programa que leia quanto dinheiro ela tem na carteira e mostre quantos dólares ela pode comprar

r = float(input('Digite a quantia(R$) da sua carteira: '))
 
d = 5.43

c = r / d

input('{}R$ são {:.2f}US$'.format(r, c))
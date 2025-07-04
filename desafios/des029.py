# Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite

vel = float(input('Digite a velocidade do carro, em km/h: '))

if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Vai ter que pagar R${:.2f}'.format(multa))
else:
    print('Está normal')
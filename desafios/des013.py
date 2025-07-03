# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

santigo = float(input('Digite o salário atual do funcionário: '))

satual = santigo * 1.15 # ou satual = ((santigo * 15) / 100) + santigo

print('O salário atual do funcionário COM AUMENTO DE 15% é R${:.2f}'.format(satual))
# Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para salários inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    a1 = salario * 1.1
    print('O salário com aumento de 10% é R${}'.format(a1))
else:
    a2 = salario * 1.5
    print('O salário com aumento de 15% é R${}'.format(a2))
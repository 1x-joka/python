# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: Abaixo de 18.5 ABAIXO DO PESO, Entre 18.5 e 25 PESO IDEAL, 25 até 30 SOBREPESO, 30 até 40 OBESIDADE e Acima de 40 OBESIDADE MÓRBIDA

p = float(input('Digite o peso, em kg: '))
h = float(input('Digite a altura, em metros: '))

imc = p / (h**2)

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
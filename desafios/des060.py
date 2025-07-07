# Faça um programa que leia um número qualquer e mostre seu fatorial

numero = int(input('Digite um número: '))
resposta = 1
contador = numero # número vai ser o número digitado, e contador no começo será igual a ele, mas depois vai diminuindo, por isso criamos duas iguais

while contador > 0:
    resposta *= contador # Multiplica
    contador -= 1 # Tira um e volta no loop
print(f'O fatorial de {numero} é {resposta}')
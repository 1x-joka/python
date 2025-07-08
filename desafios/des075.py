# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: a) Quantas vezes apareceu o valor 9; b) Em que posição foi digitado o primeiro valor 3; c) Quais foram os números pares

n = ( # Criando a tupla 
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')

if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1} posição')
else:
    print('O valor 3 não foi digitado!')

print(f'Os valores pares digitados foram ', end='')

for numero in n: # Verifica cada número digitado
    if numero % 2 == 0:
        print(numero)
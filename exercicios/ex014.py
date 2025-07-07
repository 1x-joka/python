''' for c in range(1, 10):
    print(c)
print('FIM!')'''

c = 1
while c < 10:
    print(c)
    c += 1 # Quando o loop volta, eu somo +1 no c
print('FIM!')

print('='*30)

''' for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM!')'''

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM!')

print('='*30)

resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um valor: '))
    resposta = input('Quer continuar? [S/N] ').upper()
print('FIM!')

print('='*30)

n = 1
pares = 0
impares = 0

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0: # Colocamos isso pois 0 é um número NUlO, não par
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'Você digitou {pares} números pares e {impares} números ímpares')
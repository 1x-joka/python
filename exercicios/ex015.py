contador = 1
while contador <= 10: # Enquanto isso for verdade...
    print(contador, '--> ', end='')
    contador += 1
print('Acabou')

print('='*30)

while True: # Loop Infinito
    print(contador, '--> ', end='')
    contador += 1
    break # Quebra o loop infinito
print('Acabou')

print('='*30)

n = int(input('Digite um número inteiro: '))
contador = 0

while contador < 5: # Lê 5 números
    n = int(input('Digite um número inteiro: '))
    contador += 1

print('='*30)

n = int(input('Digite um número inteiro: '))
s = 0
while n != 999: # 999 é o meu "flag"
    n = int(input('Digite um número inteiro: '))
    s += n
s -= 999 # Desconsidera o 999 (NÃO FAÇA ISSO, É GAMBIARRRA!!)
print(f'A soma vale {s}')

print('='*30)

n = int(input('Digite um número inteiro: '))
s = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break # Interrompe o while, ou seja, não soma o 999 aos digitados anteriormente, uma vez que a soma vem depois de analisar o número
    s += n

print('='*30)

nome = 'José'
idade = 33
salário = 987.35
print(f'O {nome} tem {idade} anos') # Python 3.6+
print('O {} tem {} anos'.format(nome, idade)) # Python 3
print('O %s tem %d anos' % (nome, idade)) # Python 2
print(f'O {nome:-<^20} tem {idade} anos e ganha R${salário:.2f}')
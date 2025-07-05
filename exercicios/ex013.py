for c in range(1, 10): # Não considera o último número, então terá 'Oi' 9 vezes
    print('Oi')
    print(c)
print('FIM')

print('='*30)

for c in range(6, 0, -1): # -1 = Iteração, faz a contagem de trás para frente
    print(c)

print('='*30)

for c in range(0, 7, 2): # Conta de 0 a 7 pulando de 2 em 2
    print(c)

print('='*30)

n = int(input('Digite um número: '))
for c in range(0, n+1): # Utiliza o n como limite/intervalo para o for
    print(c)

print('='*30)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): # Utiliza o n como limite/intervalo para o for
    print(c)

print('='*30)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor inteiro: '))
    s += n # Vai somando cada valor em cada loop
print('O somatório dos valores digitados foi {}'.format(s))
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} --> {t2}', end='')
cont = 3 # Começa em 3 pois já mostrei o primeiro e o segundo termo

while cont <= n:
    t3 = t1 + t2 # Somando o 1 com o 0, pois são subsequentes
    print(f' --> {t3}', end='')
    t1 = t2 # "Andando pro lado"
    t2 = t3 # "Andando pro lado"
    cont += 1 # Fazendo bater até o número de termos selecionados
print(' --> FIM')
print('~'*30)
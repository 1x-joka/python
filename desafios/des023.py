# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex.: Digite um número: 1834 (unidade: 4 dezena: 3 centena: 8 e milhar: 1)

num = int(input('Digite um número: '))
u = (num // 1) % 10 # Pego esse número, divido por 10 e pego o resto da divisão (unidade)
d = (num // 10) % 10 # (num // 10) --> Pega os três primeiros dígitos; (num // 10) % 10 Pega o resto dos três primeiros dígitos
c = (num // 100) % 10
m = (num // 1000) % 10

print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u, d, c, m))
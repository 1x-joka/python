# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desenconsiderando os espaços

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split() # Separando a frase em uma lista
tudojunto = ''.join(palavras) # Substitui os espaços por '' (vazio)
inverso = ''

for letra in range(len(tudojunto) - 1, -1, -1): # len(junto) - 1 = Pegando o número de letras e tiramos 1 (pois o elemento inicial é 0); -1 = vai até antes da primeira (uma vez que a primeira é 0); -1 = vai voltando uma letra
    inverso += tudojunto[letra] # Pegando a letra da posição atual e adicionando no final de "inverso"
print(f'O inverso de {tudojunto} é {inverso}')

if inverso == tudojunto:
    print('É UM PALÍNDROMO!')
else:
    print('A frase digitado NÃO é um palíndromo!')
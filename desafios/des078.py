# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições nas listas

valores = list()

print('='*30)
print('Programa Lista Clássica')
print('='*30)

for cont in range(1, 6):
    valores.append(int(input(f'Digite o {cont}° número: ')))

maior = menor = valores[0] # Tem que estar aqui, não pode estar no começo, pois isso tem que ser definido após o usuário completar a lista

for num in valores:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print('~'*50)
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')

for i, v in enumerate(valores): # Percorre a lista inteira, pegando o i (índice) e v (valor) ao mesmo tempo
    if v == maior: # Se tal valor for maior que o maior da lista...
        print(i + 1, end=' ') # Mostra todas as posições onde aparece o maior valor

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')

for i, v in enumerate(valores):
    if v == menor:
        print(i + 1, end=' ')

# Não pode usar index pois o index retorna a primeira posição em que o valor aparece, ou seja, se tiver repetido da um problema
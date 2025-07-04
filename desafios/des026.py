# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

frase = input('Escreva uma frase: ').strip()

print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" apareceu pela primeira vez na posição {}'.format(frase.find('A')+1)) # Soma 1 pois se a primeira letra for "A" vai aparecer que ele está na posição 0
print('A letra "A" apareceu pela última vez na posição {}'.format(frase.rfind('A')+1)) # rfind = procure a partir da direita (final)
# Faça um programa que leia a largura e altura de uma parede, em metros, e calcule a sua área e a quantidade tinta para limpá-la, sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input('Digite a largura(m) da sua parede: '))
h = float(input('Digite a altura(m) da sua parede: '))

a = l * h

q = a / 2

input('A quantidade necessária de tinta para pintar {}m² da sua parede são {}L'.format(a, q))
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

n = input('Digite algo: ')

print('O tipo primitivo é {}'.format(type(n))) # Mostra o tipo primitivo
print('Só tem espaços? {}'.format(n.isspace())) # Mostra se tem espaço na frase/palavra
print('É um número? {}'.format(n.isnumeric())) # Mostra se é um número
print('É alfabético? {}'.format(n.isalpha())) # Mostra se é alfabético
print('É alfanumérico? {}'.format(n.isalnum())) # Mostra se é alfanumérico
print('Está em maiúsculas? {}'.format(n.isupper())) # Mostra se está em maiúsculas
print('Está em minúsculas? {}'.format(n.islower())) # Mostra se está em minúsculas
print('Está capitalizada? {}'.format(n.istitle())) # Mostra se está capitalizada
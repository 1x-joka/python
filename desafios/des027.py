# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente. Ex.: Ana Maria de Souza (primeiro nome: Ana e último nome: Souza)

nome = input('Escreva seu nome completo: ').strip()

dividido = nome.split()

print('Primeiro nome: {} \nÚltimo Nome: {}'.format(dividido[0], dividido[-1])) # -1 para pegar o último elemento da lista
# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, O nome com todas as letras minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')

print('O nome com todas as maiúsculas fica: {}'.format(nome.upper()))
print('O nome com todas as minúsculas fica: {}'.format(nome.lower()))
print('O nome tem {} letras ao todo'.format(len(nome.strip())-nome.count(' '))) # Retirando os espaços do meio

dividido = nome.split()

print('O primeiro nome tem {} letras'.format(len(dividido[0])))
# Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = input('Digite seu nome completo: ').strip()

print('Seu nome tem Silva: {}'.format('SILVA' in nome.upper().split())) # Usa-se split() para separar o nome em palavras individuais, e assim garantir que estamos procurando pela palavra exata "SILVA", e não apenas por ela estar dentro de outra palavra, como "SILVANDRO"
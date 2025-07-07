# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo  =  input('Digite o seu sexo [M/F]: ').strip().upper()[0] # Usamod [0] para pegar somente a primeira letra do que a pessoa digitou

while sexo not in 'MF':
    sexo = input('[ERRO] Dados Inválidos, digite um novo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
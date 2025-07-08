# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: a) Quantas pessoas tem mais de 18 anos; b) Quantos homens foram cadastrados; c) Quantas mulheres tem menos de 20 anos

qtdidade = qtdfem = qtdmasc = 0

print('='*20, 'Programa Quantidade', '='*20)

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0]
    if idade > 18:
        qtdidade += 1
    if sexo == 'M': # Não pode usar elif pois o elif só se realiza se a anterior estiver errada
        qtdmasc += 1
    if sexo == 'F' and idade < 20:
        qtdfem += 1

    escolha = input('Quer continuar? [S/N]: ').strip().upper()[0] # Colocamos aqui porque temos que fazer a contagem primeiro, depois perguntar
    if escolha == 'N':
        break
print(f'{qtdidade} pessoas têm mais de 18 anos')
print(f'{qtdmasc} homens foram cadastrados no total')
print(f'{qtdfem} mulheres têm menos de 20 anos')
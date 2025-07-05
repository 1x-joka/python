# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

maioridade = 0
menoridade = 0
homemmaisvelhoidade = 0
homemmaisvelhonome = ''
mulhercom20 = 0
somaidade = 0

for c in range(1 ,5):
    nome = input(f'Digite o nome da {c}° pessoa: ')
    idade = int(input(f'Digite a idade da {c}° pessoa: '))
    sexo = input(f'Digite o sexo (M ou F) da {c}° pessoa: ')

    somaidade += idade # A cada idade digitada, irá somar

    if sexo == 'M':
        if idade > homemmaisvelhoidade: # Verifica se o homem atual é mais velho do que o que já foi registrado antes
            homemmaisvelhoidade = idade # Caso seja verdade, atribui a idade ao homem digitado agora
            homemmaisvelhonome = nome
    elif sexo == 'F' and idade < 20:
        mulhercom20 += 1

media = somaidade / 4

print(f'A média das idades digitadas é {media}')
print(f'O {homemmaisvelhonome} é o mais velho e tem {homemmaisvelhoidade} anos')
print(f'{mulhercom20} mulheres têm menos de 20 anos')
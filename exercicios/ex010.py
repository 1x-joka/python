nome = input('Qual é seu nome: ')

if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Que nome feio você tem')

print('Bom Dia, {}!'.format(nome))

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print('A sua média foi {:.1f}'.format(media))

if media >= 6.0:
    print('APROVADO!')
else:
    print('REPROVADO!')

print('APROVADO!' if media >=6 else 'REPROVADO!') # Condição Simplificada 
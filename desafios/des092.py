# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime
ano_atual = datetime.now().year

dados = dict()

dados['nome'] = input('Digite o nome: ')
dados['anonasc'] = int(input('Digite o ano de nascimento: '))
dados['idade'] = ano_atual - dados['anonasc']
dados['carteira'] = int(input('Digite a carteira de trabalho(0 se não tiver): '))
    
if dados['carteira'] != 0:
    dados['ano_contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['ano_contratacao'] + 35) - dados['anonasc']

print('\nDados Cadastrados:')
for k, v in dados.items():
    print(f'{k.capitalize()}: {v}')
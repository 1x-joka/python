# Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

dados = dict()
boletim = list()
nome = ''
media = 0

while True:
    dados['nome'] = input('Digite o nome do aluno: ').strip()
    dados['media'] = float(input('Digite a média do aluno: '))

    if dados['media'] >= 7:
        dados['situacao'] = 'Aprovado!!'
    elif 5 <= dados['media'] < 7:
        dados['situacao'] = 'Recuperação!!'
    else:
        dados['situacao'] = 'Reprovado!!'

    boletim.append(dados.copy())
    dados.clear() # Limpa o dicionário dados para o próximo aluno

    escolha = input('Quer continuar?[S/N]: ').strip().upper()[0]
    if escolha == 'N':
        break
    elif escolha != 'S':
        print('Inválido, assumimos que sim...')
print('\nBoletim do Aluno:')

for aluno in boletim:
    print(f'O aluno {aluno["nome"]}, tem média {aluno["media"]} e situação {aluno["situacao"]}')
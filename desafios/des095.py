# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

jogadores = []

while True:
    dados = dict()
    gols = []
    dados['nome'] = input('Digite o nome do jogador: ').strip()
    totalpartidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))

    for indice in range(totalpartidas):
        gol = int(input(f'Quantos gols ele fez na {indice + 1}° partida: '))
        gols.append(gol) # Adicionando cada gol na lista

    dados['gols'] = gols # Passando a lista para o dicionário
    dados['total'] = sum(gols) # Somando os gols feitos

    jogadores.append(dados.copy())

    escolha = input('Quer continuar?[S/N]: ').strip().upper()[0]
    if escolha == 'N':
        break
    elif escolha != 'S':
        print('Inválido, assumimos que SIM...')

# Tabela com Resumo
print('\n' + '-' * 40)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":<5}') # Imprime um cabeçalho formatado para a tabela de jogadores, alinhando os títulos das colunas de forma organizada
print('-' * 40)

for indice,jogador in enumerate(jogadores):
    print(f'{indice:<4}{jogador["nome"]:<15}{str(jogador["gols"]):<15}{jogador["total"]:<5}') # Imprimindo uma linha formatada com 4 colunas
print('-'*40)

# Tabela de visualização individual
while True:
    opcao = int(input('Quer mostrar os dados de qual jogador?(999 para interromper): '))
    if opcao == 999:
        break
    if 0 <= opcao < (len(jogadores)): # Verifica se a opção condiz com a lista jogadores
        print(f'Detalhes do jogador {jogadores[opcao]["nome"]}: ') # Acessando o nome do jogador na estrutura de dados criado
        for indice, gol in enumerate(jogadores[opcao]['gols']):
            print(f'No jogo {indice + 1} fez {gol} gols')
    else:
        print('[ERRO] Código Inválido. Tente novamente')
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

dados = dict()

dados['nome'] = input('Digite o nome do jogador: ').strip()
totalpartidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
dados['partidas'] = totalpartidas

gols = list()

for indice in range(totalpartidas):
    gol = int(input(f'Quantos gols ele fez na {indice + 1}° partida: '))
    gols.append(gol) # Adicionando cada gol na lista

dados['gols'] = gols # Passando a lista para o dicionário
dados['total'] = sum(gols) # Somando os gols feitos

print('\nResumo do jogador:')
print(f'Nome: {dados["nome"]}')
print(f'Número de partidas: {dados["partidas"]}')
print(f'Gols por partida: {dados["gols"]}')
print(f'Total de gols no campeonato: {dados["total"]}')
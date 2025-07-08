# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Apenas os 5 primeiros colocados; b) Os últimos 4 colocados da tabela; c) Uma lista com os times em ordem alfabética; d) Em que posição na tabela está o time da Chapecoense

brasileirao = (
    'Flamengo', 'Botafogo', 'Palmeiras', 'Grêmio', 'Athletico-PR',
    'Bragantino', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'Cuiabá',
    'Corinthians', 'Internacional', 'Cruzeiro', 'Bahia', 'Santos',
    'Goiás', 'Vasco', 'América-MG', 'Coritiba', 'Chapecoense'
)

print(f'Os 5 primeiros colocados na tabela são: {brasileirao[:5]}')
print(f'Os 4 últimos colocados na tabela são: {brasileirao[-4:]}')
print(f'Em ordem alfabética fica: {sorted(brasileirao)}')
print(f'O time "CHAPECOENSE" está na posição {brasileirao.index("Chapecoense")+1}') # Adicionamos 1 pois a contagem começa no 0
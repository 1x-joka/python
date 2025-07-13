pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # ASPAS DUPLA
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Leandro' # Substituindo um nome por outro
pessoas['peso'] = 98.5 # Adicionando uma chave com elemento
del pessoas['sexo'] # Deletando a chave 'sexo'

print('='*30)

for k in pessoas.keys():
    print(k)

print('='*30)

for k, v in pessoas.items(): # pessoas.items() substitui o enumerate
    print(f'{k} = {v}')

print('='*30)

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil) # Lista com dicionários
print(brasil[0]) # Mostrando tudo do Rio de Janeiro
print(brasil[1]) # Mostrando tudo de São Paulo
print(brasil[0]['uf']) # Mostrando apenas "Rio de Janeiro"
print(brasil[1]['sigla']) # Mostrando apenas "SP"

print('='*30)

estado3 = dict()
brasil2 = list()

for cont in range(1, 4):
    estado3['uf'] = input('Digite a Unidade Federativa: ')
    estado3['sigla'] = input('Digite a sigla do estado: ')
    brasil2.append(estado3.copy()) # Copiando o conteúdo (fatiamento em listas e tuplas)
print(brasil2)

for e in brasil2:
    for v in e.values():
        print(v, end=' ')
    print() # Para quebrar linha
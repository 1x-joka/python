from lib.interface import *
import os

def caminho_do_arquivo(nome):
    # Caminho absoluto da pasta onde está o script
    pasta = os.path.dirname(os.path.abspath(__file__)) # os.path.dirname(...) = Remove o nome do arquivo e pega só a pasta / os.path.abspath(__file__) = Pega o caminho absoluto completo do seu arquivo .py
    return os.path.join(pasta, nome) # Junta a pasta com o nome do arquivo (cursoemvideo.txt) de forma segura

def arquivoExiste(nome):
    return os.path.isfile(nome) # Verifica se existe um arquivo com aquele nome e se ele é realmente um arquivo(pois pode ser uma pasta)
    
def criarArquivo(nome):
    try:
        with open(nome, 'wt+') as arq: # with open(...) as arq = Garante que o arquivo seja automaticamente fechado depois que você terminar de usar e evita erros, tipo esquecer de usar arquivo.close() ; wt+ = escreve dentro do arquivo txt criando-o
            print(f'Arquivo "{nome}" criado com sucesso!')
    except Exception as erro:
        print(f'Houve um erro ao criar o arquivo: {erro}')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a: # Para cada linha dentro do arquivo...
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome = '<desconhecido>', idade = 0):
    try:
        a = open(arq, 'at') # at = append arquivo de texto
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
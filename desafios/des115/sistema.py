# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema vai ter 2 opções: cadastrar uma nova pessoa na lista e listar todas as pessoas cadastradas

from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = caminho_do_arquivo('cursoemvideo.txt')
if not arquivoExiste(arq): # Se não existir...
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar um conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31m[ERRO] Digite uma opção válida!\033[m')
    sleep(1)
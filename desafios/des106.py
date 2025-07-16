# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs.: Use cores

from time import sleep

c = ('\033[m', # 0 - Sem cores
     '\033[0;30;41m', # 1 - Vermelho
     '\033[0;30;42m', # 2 - Verde
     '\033[0;30;43m', # 3 - Amarelo
     '\033[0;30;44m', # 4 - Azul
     '\033[0;30;45m', # 5 - Roxo
     '\033[7;30m', # 6 - Branco
     )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4) # Dentro de uma função eu posso chamar outra função
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1.5)

def título(msg, cor=0): # O 'ATÉ LOGO' será encaminho no lugar de msg
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end='') # Limpa as cores
    sleep(1)

# Programa Principal
comando = ''
while True:
    título('Sistema de Ajuda PyHelp', 2)
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM': # Colocamos o upper aqui, pois caso ele escreva print, sairá PRINT (e não é a mesma coisa)
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)
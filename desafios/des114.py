# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado

import urllib
import urllib.error
import urllib.request # Importando um módulo interno dentro de urllib

try:
    site = urllib.request.urlopen('http://www.pudim.com.br') # Tentando abrir uma url
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento!')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read()) # Me da o código do site todo
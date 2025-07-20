# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 108, 108 e 109 para o primeiro pacote e matenha tudo funcionando

from utilidadesCeV import moeda, dado

n = float(input('Digite um número qualquer: '))
moeda.resumo(n)
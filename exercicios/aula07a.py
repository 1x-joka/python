pow(4,3) # Mesma coisa que 4³

print('='*50)

nome = str(input('Digite seu nome: '))
print('Prazer em te conhecer {:20}!'.format(nome)) # {:20} Aparece em 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome)) # {:>20} Alinha o nome à direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # {:<20} Alinha o nome à esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # {:^20} Alinha o nome ao centro
print('Prazer em te conhecer {:=^20}!'.format(nome)) # {:=^>20} Escreve o nome em 20 espaços, centralizado e colocando "=" em volta

print('='*50)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, \n o produto é {}, a divisão é {}, '.format(s, m, d), end='') # end='' Mostra que no final da linha NÃO terá quebra / \n QUEBRA a linha

print('a divisão inteira é {:.3f} e a exponenciação é {}'.format(di, e))# {:.3f} Mostra somente 3 casas decimais flutuantes (reais)
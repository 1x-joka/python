n = bool(input('Digite um número: '))

print(n) # Caso tenha um valor dentro da variável = true

n2 = input('Digite algo: ')
print(n2.isnumeric()) # Verifica se é possível converter o valor "n2" em um número do tipo primitivo int
print(n2.isalpha()) # Verifica se o valor "n2" é uma letra
print(n2.isalnum()) # Verifica se é alfanumérico (tem letra e número)
print(n2.isupper()) # Verifica se todas as letras são maiúsculas
print(n2.islower()) # Verifica se todas as letras são minúsculas
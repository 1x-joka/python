n1 = int(input('Digite um valor: '))
print(type(n1)) # Aparece como string porque ela tem que ser especificada

n2 = int(input('Digite outro número: '))
s = n1 + n2

print('A soma vale {}'.format(s)) # Caso você não especifique o tipo da variável, ela irá concatenar na hora da soma
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
print('A soma entre', n1, 'e', n2, 'vale', s) # Modo antigo, NÃO USAR
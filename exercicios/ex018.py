teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria' # Após fazer isso, os dois ficaram com 'Maria', pois o append sem o [:] faz uma ligação entre as estruturas, então se eu mudar uma eu mudo a outra
teste[1] = 22
galera.append(teste[:]) # Fazendo uma cópia (com [:])
print(galera)

print('='*30)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] # Estrutura composta
print(galera2)
print(galera2[0])
print(galera2[0][0])
print(galera2[2][1])

print('='*30)

galera3 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for pessoa in galera3:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade') # Pessoa[1] pega o primeiro elemento (idade) de cada lista

print('='*30)

galera4 = list()
dado = list() # Será usada para pegar temporariamente os dados da galera4
totalmaior = totalmenor = 0

for cont in range(0, 3):
    dado.append(input('Digite o nome: ')) # Jogando cada nome para dentro da lista dado
    dado.append(int(input('Digite a idade: ')))
    galera4.append(dado[:]) # Depois passando para galera4 criando uma cópia
    dado.clear() # Excluindo DADO, não galera4

print(galera4)

for pessoa in galera4:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade!')
        totalmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        totalmenor += 1

print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade!')
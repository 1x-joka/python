# Crie um programa que tenha a função leiaInt() do Python, só que fazendo a validação para aceitar apenas um valor númerico. Ex.: n = leiaInt('Digite um n')

def leiaInt(n):
    ok = False # Se não tiver nada ok (No começo, ainda não temos um valor válido)
    valor = 0
    while True:
        n = input(n) # Mostra a mensagem passada para a função (repete a mensagem da variável global)
        if n.isnumeric(): # Se eu digitei um número...
            valor = int(n) # A parte inteira dele vai para a variável local
            ok = True # É um número
        else:
            print('\033[0;31m[ERRO] Digite um número inteiro válido!!\033[m')
        if ok: # se a entrada for válida (True = um número)...
            break
    return valor # Retorna o valor numérico digitado pelo usuário (convertido pra int)

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
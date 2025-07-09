# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expr = str(input('Digite a expressão: '))
pilha = []

for simbolo in expr:
    if simbolo == '(':
        pilha.append('(') # Cada parênteses que o usuário abre, eu jogo na pilha
    elif simbolo == ')':
        if len(pilha) > 0: # Ou seja, não está vazio
            pilha.pop() # Removendo o último elemento dela
        else:
            print(pilha.append(')')) # Se a pilha estiver vazia, eu adiciono o ')', ou seja, teve mais parênteses fechando do que abrindo
            break

if len(pilha) == 0: # Cada parênteses que abriu, teve seu par (o fechando)
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
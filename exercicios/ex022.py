try: # Tente...
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # Caso der um erro... / Exception as erro = Criando uma variável erro
    print(f'Problema encontrado foi {erro.__class__}')
else: # Caso der certo (opcional)...
    print(f'O resultado é {r:.1f}')
finally: # Independente de der certo ou errado (opcional)...
    print('Volte sempre! Muito obrigado!')

print('*'*50)

try: # Tente...
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): # Caso dê erro de valor ou de tipo...
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: # Caso der certo (opcional)...
    print(f'O resultado é {r:.1f}')
finally: # Independente de der certo ou errado (opcional)...
    print('Volte sempre! Muito obrigado!')
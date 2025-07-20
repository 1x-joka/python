def leiaDnheiro(n = 0):
    válido = False # É letra
    while not válido:
        entrada = str(input(n)).replace(',', '.').strip() # replace(',', '.') = substituindo todas as vírgulas por pontos
        if entrada.isalpha() or entrada == '': # Se ele for alpha numérico (letra) ou tiver cheia de espaço...
            print(f'\033[0;31m[ERRO] \"{entrada}\" Preço Inválido!\033[m')
        else:
            válido = True # É número
            return float(entrada) # Retorna ele normal, como digitado
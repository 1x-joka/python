# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

palavras = (
    'Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro'
)

for p in palavras: # Para analisar cada palavra da tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # Para analisar cada letra na palavra "p"
        if letra.lower() in 'aeiou': # Se tiver letras com a e i o u...
            print(letra, end=' ')
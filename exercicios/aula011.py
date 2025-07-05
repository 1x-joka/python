print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;35mOlá, Mundo!\033[m')
print('\033[0;33;44mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Guanabara'
cores = {'limpa':'\033[m', 
        'Azul':'\033[34m', 
        'Amarelo':'\033[33m', 
        'Preto e Branco':'\033[7;30m'}

print('Olá! Muito prazer te conhecer {}{}{}!'.format('\033[4;34m', nome, '\033[m')) # Abrindo, variável, fechando
print('Olá! Muito prazer te conhecer {}{}{}!'.format(cores['Preto e Branco'], nome, cores['limpa']))
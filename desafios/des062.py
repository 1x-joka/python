# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeirotermo
contador = 1 # quantos termos da PA já foram mostrados
total = 0 # Guarda a quantidade total de termos que já foram mostrados até agora
mais = 10 # Número de termos que o usuário quer mostrar a mais na próxima rodada (começa com 10)

while mais != 0:
    total += mais # Quero mostrar mais "mais" termos, então atualizo o total para refletir isso
    while contador <= total:
        print(f'{termo} --> ', end=' ')
        termo += razao # Atualiza o termo adicionando a razão a ele
        contador += 1 # Somando 1 até bater no total depois
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar: '))
print('\nFIM')
print(f'Progressão finalizada com {total} termos!')
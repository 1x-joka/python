frase = 'Curso em Vídeo Python'

print(frase)
print(frase[3]) # Letra s
print(frase[3:13]) # so em Víde
print(frase[:13]) # Curso em Víde
print(frase[13:]) # o Python
print(frase[1:15]) # urso em Vídeo
print(frase[1:15:2]) # us mVdo
print(frase[1::2]) # us mVdoPto
print(frase[::2]) # Croe íe yhn
print(frase.count('o')) # Conta quantos 'o' (minúsculos) tem
print(frase.count('O')) # Conta quantos 'O' (maiúsculos) tem
print(frase.upper().count('O')) # Transforma em maiúsculo e conta quantos 'O' (maiúsculos) tem
print(len(frase)) # Quantas letras têm
print(len(frase.strip())) # Remove os espaços antes e depois e conta quantas letras têm
print(frase.replace('Python', 'Android')) # Trocando 'Python' por 'Android'
print('Curso' in frase) # Verifica se a palavra 'Curso' está dentro da frase
print(frase.fin('Curso')) # Mostra a posição da palavra 'Curso' na frase
print(frase.lower().find('vídeo')) # Deixa a frase tudo minúscula e mostra em qual posição a palavra 'vídeo' está
print(frase.split()) # Cria uma lista com separador de espaço

dividido = frase.split()
print(dividido[0]) # Mostrando o primeiro item da lista
print(dividido[2][3]) # Mostrando qual é a terceira letra do primeiro item da lista

print('Oi')

print("""Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.""") # Aspas triplas
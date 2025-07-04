# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame # Utilizado para criar jogos, e jogos contém musicas, imagens, etc.
pygame.init() # Inicializando
pygame.mixer.music.load('paiva.mp3') # Carregando/Puxando o arquivo
pygame.mixer.music.play() # Começando
input()
pygame.event.wait() # Encerrando
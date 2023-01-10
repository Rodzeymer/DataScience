# Neste algoritmo tentamos fazer o Python tocar um arquivo de mp3, não sei se funciona, mas
# segui os passos do Guanabara

print('*' *30)
print(f"{'Python Mundo 1 - Desafio 21':^30}")
print('*' *30)

import pygame

pygame.init()
pygame.mixer.music.load("/src/musica.mp3")
pygame.mixer.music.play()
pygame.event.wait()

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)
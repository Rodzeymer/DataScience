import pygame

pygame.init()

pygame.mixer.music.load("/src/musica.mp3")
pygame.mixer.music.play()
pygame.event.wait()
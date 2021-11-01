import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

rect(screen, 'grey', (0, 0, 1280, 720)) #Заливка

circle(screen, 'yellow', (300, 300), 100) #Голова
circle(screen, 0, (300, 300), 100, 1) #Голова_обводка

circle(screen, 'red', (260, 270), 20) #Левый глаз
circle(screen, 0, (260, 270), 20, 1) #Левый глаз_обводка
circle(screen, 0, (260, 270), 9) #Левый глаз_зрачок
line(screen, 0, (200, 220), (280, 260), 10) #Левый глаз_бровь

circle(screen, 'red', (345, 270), 15) #Правый глаз
circle(screen, 0, (345, 270), 15, 1) #Правый глаз_обводка
circle(screen, 0, (345, 270), 8) #Правый глаз_зрачок
line(screen, 0, (330, 260), (400, 225), 10) #Правый глаз_бровь

rect(screen, 0, (250, 340, 100, 20)) #Рот

pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((2000, 1500))

rect(screen, (254, 213, 162), (0, 0, 2000, 300)) #Заливка1
rect(screen, (254, 213, 196), (0, 300, 2000, 300)) #Заливка2

circle(screen, 'yellow', (1000, 300), 120) #Солнце

polygon(screen, (252, 152, 49), [[0, 540], [400, 280], [500, 305], [540, 370], [810, 560], [950, 535], #Гора1
                                 [1020, 595], [1150, 490], [1260, 530], [1320, 470], [1600, 250],
                                 [1680, 400], [1770, 360], [1900, 450], [1950, 430],
                                 [2000, 540], [2000, 600], [0, 600]])
ellipse(screen, (252, 152, 49), (1500, 250, 200, 800))
ellipse(screen, (254, 213, 196), (10, 60, 400, 350))
polygon(screen, (254, 213, 162), [[0, 300], [394, 300], [400, 280], [500, 280], [400, 0], [0, 0]])

rect(screen, (254, 213, 148), (0, 600, 2000, 300)) #Заливка3

polygon(screen, (172, 67, 52), [[320, 900], [440, 690], [640, 790], [710, 630], [930, 670], [1050, 760], #Гора2
                                [1200, 730], [1410, 570], [1620, 750], [1720, 670], [1830, 730],
                                [1890, 640], [1950, 680], [2000, 510], [2000, 900]])
ellipse(screen, (172, 67, 52), (25, 520, 350, 900))
ellipse(screen, (172, 67, 52), (1200, 560, 350, 900))

rect(screen, (179, 134, 148), (0, 900, 2000, 600)) #Заливка4

pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

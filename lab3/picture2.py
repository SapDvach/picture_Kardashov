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

polygon(screen, (48, 16, 38), [[0, 670], [270, 710], [530, 1100], [1000, 1450], [1400, 1200], #Гора3
                               [1670, 1300], [2000, 850], [2000, 1500], [0, 1500]])
ellipse(screen, (179, 134, 148), (1420, 910, 380, 400))
ellipse(screen, (48, 16, 38), (1800, 815, 380, 660))

surf = pygame.Surface((100, 100), pygame.SRCALPHA) #Птица
ellipse(surf, (66, 33, 11), (15, 35, 20, 110))
ellipse(surf, (66, 33, 11), (10, 84, 80, 60))

screen.blit(pygame.transform.rotozoom(surf, 45, 1.8), (1480, 850)) #Распределение птиц
screen.blit(pygame.transform.rotozoom(surf, 45, 1), (1400, 800))
screen.blit(pygame.transform.rotozoom(surf, 45, 1.3), (1300, 870))
screen.blit(pygame.transform.rotozoom(surf, 45, 0.8), (1250, 840))

screen.blit(pygame.transform.rotozoom(surf, 45, 1), (900, 400))
screen.blit(pygame.transform.rotozoom(surf, 45, 1.15), (850, 500))
screen.blit(pygame.transform.rotozoom(surf, 45, 0.9), (750, 450))

pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

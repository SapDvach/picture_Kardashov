import pygame
from pygame.draw import *
import sys

name = str(input('Your name: '))

width, length = 1200, 900   # Размер экрана

pygame.init()
pygame.display.set_caption('OSU')   # Название игры
screen = pygame.display.set_mode((width, length))
clock = pygame.time.Clock()

FPS = 60

x1, x2, x3 = width / 2, width / 2, width / 2      # X координаты шаров
y1, y2, y3 = length / 2, length / 2, length / 2   # Y координаты шаров
x1_move, x2_move, x3_move = 5, 8, 5   # X смещения шаров
y1_move, y2_move, y3_move = 8, 5, 3   # Y смещения шаров
r = 50   # Радиус шаров

x4, y4 = width / 2 - 10, length / 2 - 10   # Координаты квадрата
x4_move = 10   # X смещение квадрата

n = 0   # Счётчик

while True:
    clock.tick(FPS)

    x1 += x1_move   # Смещения шаров
    y1 += y1_move
    x2 -= x2_move
    y2 -= y2_move
    x3 += x3_move
    y3 -= y3_move

    x4 += x4_move   # Смещение квадрата

    screen.fill((0, 0, 0))

    ball1 = circle(screen, (255, 0, 0), (x1, y1), r)   # Инициализация шаров
    ball2 = circle(screen, (0, 255, 0), (x2, y2), r)
    ball3 = circle(screen, (0, 0, 255), (x3, y3), r)

    sqrt = rect(screen, (255, 255, 255), (int(x4), int(y4), 20, 20))   # Инициализация квадрата

    if ball1.topleft[0] <= 0 or ball1.bottomright[0] >= width:   # Отскоки шаров от стен
        x1_move = -x1_move
    if ball1.topleft[1] <= 0 or ball1.bottomright[1] >= length:
        y1_move = -y1_move
    if ball2.topleft[0] <= 0 or ball2.bottomright[0] >= width:
        x2_move = -x2_move
    if ball2.topleft[1] <= 0 or ball2.bottomright[1] >= length:
        y2_move = -y2_move
    if ball3.topleft[0] <= 0 or ball3.bottomright[0] >= width:
        x3_move = -x3_move
    if ball3.topleft[1] <= 0 or ball3.bottomright[1] >= length:
        y3_move = -y3_move

    if sqrt.topleft[0] <= 0 or sqrt.bottomright[0] >= 1200:   # Отскоки квадрата от стен
        x4_move = -x4_move

    for event in pygame.event.get():   # Проверка на выход
        if event.type == pygame.QUIT:
            print('Score:', n)
            if n > 20:   # Запись в файл
                out = str(name) + ': ' + str(n)
                f = open('Top.txt', 'a')
                f.write('\n')
                f.write(out)
                f.close()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:   # Проверка на попадание
            A = pygame.mouse.get_pos()
            x_A = A[0]
            y_A = A[1]

            if ((x_A - x1)**2 + (y_A - y1)**2 <= r**2)\
                    or ((x_A - x2)**2 + (y_A - y2)**2 <= r**2)\
                    or ((x_A - x3)**2 + (y_A - y3)**2 <= r**2):   # Проверка на попадание шаров
                print('+1')
                n += 1

            elif (x_A - x4)**2 + (y_A - y4)**2 <= r**2:   # Проверка на попадание квадрата
                print('+5')
                n += 5
            else:
                print('Miss')

    pygame.display.update()

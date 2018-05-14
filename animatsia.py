# Пак Дмитрий ИУ7-22Б

import pygame as py
from math import sin, cos, pi


# Грузовик
def track(trackcoords, color):
    py.draw.rect(screen, color["orange"],
                 ((trackcoords[0], trackcoords[1]), (180, 90)))
    py.draw.rect(screen, color["darkblue"],
                 ((trackcoords[0] + 25, trackcoords[1] + 10), (130, 40)))


# Колеса
def wheels(wheelcoords_left, wheelcoords_right, color):
    x1 = -14.8 * cos(t1)
    fx1 = 14.8 * sin(t1)
    x2 = -14.8 * cos(t2)
    fx2 = 14.8 * sin(t2)
    y_fix_wheel = 430

    py.draw.circle(screen, (0, 0, 0), (wheelcoords_left[0], y_fix_wheel), 20)
    py.draw.circle(screen, (0, 0, 0), (wheelcoords_right[0], y_fix_wheel), 20)
    py.draw.circle(screen, (color["gray"]), (wheelcoords_left[0], y_fix_wheel),
                   16, 3)
    py.draw.circle(screen, (color["gray"]),
                   (wheelcoords_right[0], y_fix_wheel), 16, 3)
    py.draw.line(screen, (color["gray"]),
                 (wheelcoords_left[0] + x1, y_fix_wheel - fx1),
                 (wheelcoords_left[0] - x1, y_fix_wheel + fx1), 3)
    py.draw.line(screen, (color["gray"]),
                 (wheelcoords_left[0] + x2, y_fix_wheel - fx2),
                 (wheelcoords_left[0] - x2, y_fix_wheel + fx2), 3)
    py.draw.line(screen, (color["gray"]),
                 (wheelcoords_right[0] + x1, y_fix_wheel - fx1),
                 (wheelcoords_right[0] - x1, y_fix_wheel + fx1), 3)
    py.draw.line(screen, (color["gray"]),
                 (wheelcoords_right[0] + x2, y_fix_wheel - fx2),
                 (wheelcoords_right[0] - x2, y_fix_wheel + fx2), 3)


# Человек
def man(headcoords):
    py.draw.arc(screen, color["desert"], (paracoords, (150, 50)), 0,
                pi, 25)
    py.draw.circle(screen, (0, 0, 0),
                   headcoords, 9, 9)
    py.draw.line(screen, (0, 0, 0),
                 headcoords,
                 (headcoords[0], headcoords[1] + 25), 3)
    py.draw.line(screen, (0, 0, 0),
                 (headcoords[0], headcoords[1] + 25),
                 (headcoords[0] + 10, headcoords[1] + 35), 3)
    py.draw.line(screen, (0, 0, 0),
                 (headcoords[0], headcoords[1] + 25),
                 (headcoords[0] - 10, headcoords[1] + 35), 3)
    py.draw.line(screen, (0, 0, 0),
                 (headcoords[0] - 15, headcoords[1] + 13),
                 (headcoords[0] + 15, headcoords[1] + 13), 3)
    py.draw.line(screen, (0, 0, 0),
                 (headcoords[0] + 15, headcoords[1] + 13),
                 (headcoords[0] + 70, headcoords[1] - 25), 1)
    py.draw.line(screen, (0, 0, 0),
                 (headcoords[0] - 15, headcoords[1] + 13),
                 (headcoords[0] - 80, headcoords[1] - 25), 1)


# Фон
def bg():
    py.draw.rect(screen, color["green"], ((0, 450), (800, 150)))  # зелень
    py.draw.rect(screen, (129, 128, 128), ((0, 450), (800, 50)))  # асфальт
    # облака
    py.draw.ellipse(screen, (255, 255, 255), ((150, 80), (120, 40)))
    py.draw.ellipse(screen, (255, 255, 255), ((170, 70), (120, 40)))
    py.draw.ellipse(screen, (255, 255, 255), ((190, 80), (120, 40)))
    py.draw.ellipse(screen, (255, 255, 255), ((550, 80), (120, 40)))
    py.draw.ellipse(screen, (255, 255, 255), ((570, 70), (120, 40)))
    py.draw.ellipse(screen, (255, 255, 255), ((590, 80), (120, 40)))
    py.draw.ellipse(screen, (255, 255, 255), ((590, 80), (120, 40)))


if __name__ == "__main__":
    py.init()
    size = [800, 600]
    screen = py.display.set_mode(size)
    clock = py.time.Clock()
    # цвета
    color = {"gray": [76, 76, 76], "blue": [54, 144, 234],
             "green": [114, 232, 149], "desert": [232, 249, 38],
             "brown": [99, 82, 68], "red": [218, 97, 86],
             "orange": [237, 154, 64], "darkblue": [0, 36, 244]}
    # координаты объектов
    trackcoords = [300, 340]
    wheelcoords_left = [345, 430]
    wheelcoords_right = [435, 430]
    textcoords = [350, 390]
    paracoords = [300, 50]
    headcoords = [380, 100]

    t1 = 0
    t2 = 1.57
    # текст
    font = py.font.Font(None, 25)
    text = font.render("Петрович", True, color["red"])

    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        screen.fill((1, 150, 250))

        man(headcoords)

        bg()

        track(trackcoords, color)

        wheels(wheelcoords_left, wheelcoords_right, color)

        screen.blit(text, textcoords)

        py.display.flip()
        clock.tick(15)

        trackcoords[0] += 10
        textcoords[0] += 10
        wheelcoords_left[0] += 10
        wheelcoords_right[0] += 10
        paracoords[1] += 3
        headcoords[1] += 3
        if trackcoords[0] > 800:
            trackcoords[0] = -200
            textcoords[0] = -150
            wheelcoords_left[0] = -155
            wheelcoords_right[0] = -65

        t1 += 0.3
        t2 += 0.3

        if paracoords[1] > 450:
            paracoords[1] = -100
            headcoords[1] = -50

    py.quit()

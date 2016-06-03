__author__ = 'jubin'
import pygame
from pygame.locals import *
from sys import exit

one_pos = (320, 120)  # first rotor
two_pos = (160, 240)  # second rotor
three_pos = (480, 240)  # third rotor
four_pos = (320, 360)  # fourth rotor


def return_colour(colour):
    if colour == 'BLACK':
        return 0, 0, 0
    elif colour == 'GREEN':
        return 0, 255, 64
    elif colour == 'RED':
        return 255, 0, 0


def _2drawcircle(color, i):
    pygame.draw.circle(screen, color, one_pos, i, 1)


def _4drawcircle(color, i):
    pygame.draw.circle(screen, color, two_pos, i, 1)


def _6drawcircle(color, i):
    pygame.draw.circle(screen, color, three_pos, i, 1)


def _8drawcircle(color, i):
    pygame.draw.circle(screen, color, four_pos, i, 1)


_2rpm = 0
_4rpm = 0
_6rpm = 0
_8rpm = 0

temp_2 = 0
temp_4 = 0
temp_6 = 0
temp_8 = 0
qflag = 0
wflag = 0

_2flag = 0
_4flag = 0
_6flag = 0
_8flag = 0

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Quadcopter Simulator")

myfont = pygame.font.SysFont("TimesNewRoman", 15)
label1 = myfont.render("hold ' q ' to increase rotor rpm", 1, return_colour('GREEN'))
label2 = myfont.render("hold ' w ' to decrease rotor rpm ", 1, return_colour('GREEN'))
label3 = myfont.render("' 2 ' to move forward", 1, return_colour('GREEN'))
label4 = myfont.render("' 8 ' to move backword", 1, return_colour('GREEN'))
label5 = myfont.render("' 4 ' to move left", 1, return_colour('GREEN'))
label6 = myfont.render("' 6 ' to move right", 1, return_colour('GREEN'))
label7 = myfont.render("' 5 ' to stablize the rotors", 1, return_colour('GREEN'))

screen.blit(label1, (10, 0))
screen.blit(label2, (10, 15))
screen.blit(label3, (10, 30))
screen.blit(label4, (10, 45))
screen.blit(label5, (10, 60))
screen.blit(label6, (10, 75))
screen.blit(label7, (10, 90))
pygame.display.update()
# ' q ' to increase the engine power ==  k_q
# ' w ' to decrease engine power     ==  k_w
# ' 2 ' to move forward              ==  k_KP2
# ' 4 ' to move left                 ==  k_KP4
# ' 6 ' to move right                ==  k_KP6
# ' 8 ' to move backward             ==  k_KP8


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    if event.type == KEYDOWN:
        if event.key == K_q and _2rpm <= 800 and _4rpm <= 800 and _6rpm <= 800 and _8rpm <= 800:
            _2rpm += 1
            _4rpm += 1
            _6rpm += 1
            _8rpm += 1
            qflag = 1
            wflag = 0

        elif event.key == K_w and _2rpm > 0 and _4rpm > 0 and _6rpm > 0 and _8rpm > 0:
            _2rpm -= 1
            _4rpm -= 1
            _6rpm -= 1
            _8rpm -= 1
            qflag = 0
            wflag = 1

        elif event.key == K_2 or event.key == K_KP2:
            _2flag = 1
            temp_2 = _2rpm - 20
            temp_8 = _8rpm + 20

        elif event.key == K_4 or event.key == K_KP4:
            _4flag = 1
            temp_4 = _2rpm - 20
            temp_6 = _8rpm + 20

        elif event.key == K_6 or event.key == K_KP6:
            _6flag = 1
            temp_6 = _2rpm - 20
            temp_4 = _8rpm + 20

        elif event.key == K_8 or event.key == K_KP8:
            _8flag = 1
            temp_8 = _2rpm - 20
            temp_2 = _8rpm + 20

        elif event.key == K_5 or event.key == K_KP5:
            for i in range(1, 80):
                if _2rpm >= i and _4rpm >= i and _6rpm >= i and _8rpm >= i:
                    _2drawcircle(return_colour('GREEN'), i)
                    _4drawcircle(return_colour('GREEN'), i)
                    _6drawcircle(return_colour('GREEN'), i)
                    _8drawcircle(return_colour('GREEN'), i)
                    pygame.display.update()

            for i in range(100, 1, -1):
                if _2rpm <= i and _4rpm <= i and _6rpm <= i and _8rpm <= i:
                    _2drawcircle(return_colour('BLACK'), i)
                    _4drawcircle(return_colour('BLACK'), i)
                    _6drawcircle(return_colour('BLACK'), i)
                    _8drawcircle(return_colour('BLACK'), i)
                    pygame.display.update()

        if qflag == 1:
            for i in range(1, 80):
                if _2rpm >= i and _4rpm >= i and _6rpm >= i and _8rpm >= i:
                    _2drawcircle(return_colour('GREEN'), i)
                    _4drawcircle(return_colour('GREEN'), i)
                    _6drawcircle(return_colour('GREEN'), i)
                    _8drawcircle(return_colour('GREEN'), i)
                    pygame.display.update()
            qflag = 0
        elif wflag == 1:
            for i in range(100, 1, -1):
                if _2rpm <= i and _4rpm <= i and _6rpm <= i and _8rpm <= i:
                    _2drawcircle(return_colour('BLACK'), i)
                    _4drawcircle(return_colour('BLACK'), i)
                    _6drawcircle(return_colour('BLACK'), i)
                    _8drawcircle(return_colour('BLACK'), i)
                    pygame.display.update()
            wflag = 0

        elif _2flag == 1:
            for i in range(100, 1, -1):
                if temp_2 <= i:
                    _2drawcircle(return_colour('BLACK'), i)
                    pygame.display.update()
            for i in range(1, 100):
                if temp_8 >= i:
                    _8drawcircle(return_colour('GREEN'), i)
                    pygame.display.update()
            _2flag = 0

        elif _4flag == 1:
            for i in range(100, 1, -1):
                if temp_4 <= i:
                    _4drawcircle(return_colour('BLACK'), i)
                    pygame.display.update()
            for i in range(1, 100):
                if temp_6 >= i:
                    _6drawcircle(return_colour('GREEN'), i)
                    pygame.display.update()
            _4flag = 0
        elif _6flag == 1:
            for i in range(100, 1, -1):
                if temp_6 <= i:
                    _6drawcircle(return_colour('BLACK'), i)
                    pygame.display.update()
            for i in range(1, 100):
                if temp_4 >= i:
                    _4drawcircle(return_colour('GREEN'), i)
                    pygame.display.update()
            _6flag = 0

        elif _8flag == 1:
            for i in range(100, 1, -1):
                if temp_8 <= i:
                    _8drawcircle(return_colour('BLACK'), i)
                    pygame.display.update()
            for i in range(1, 100):
                if temp_2 >= i:
                    _2drawcircle(return_colour('GREEN'), i)
                    pygame.display.update()
            _8flag = 0

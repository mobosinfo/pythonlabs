from pygame import *
import pygame as py
from math import sin, cos
import os

py.init()
size = [800, 600]
screen = py.display.set_mode(size)
clock = py.time.Clock()

color = {"gray":[76,76,76], "blue":[54,144,234], "green":[114,232,149], "desert":[232,249,38], "brown":[99,82,68]}
treecoords = [[120,10],[100,50],[250,10],[230,50],[380,10],[360,50],\
[510,10],[490,50],[640,10],[620,50],[750,10],[730,50]]
suncoords = [400,40]
t1 = 0
t2 = 1.57


def track():
    py.draw.rect(screen, color["desert"],((450, 475), (45, 45))) #корпус
    py.draw.rect(screen, color["brown"],((300, 400), (140, 85))) #крыша
    py.draw.rect(screen, color["desert"], ((440, 430), (55, 50)))  # кабина
    py.draw.rect(screen, color["desert"], ((300, 475), (180, 45)))

    py.draw.circle(screen, (0,0,0), (345,520),20)
    py.draw.circle(screen, (0,0,0), (435,520),20)
    py.draw.circle(screen, (128,128,128), (345,520),16,3)
    py.draw.circle(screen, (128,128,128), (435,520),16,3)

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill((1, 150, 250))
    py.draw.circle(screen,(247,255,0),(suncoords[0],suncoords[1]),20)
    py.draw.line(screen,(247,255,0),\
    (suncoords[0]-15,suncoords[1]),(suncoords[0]-40,suncoords[1]),4)
    py.draw.line(screen,(247,255,0),\
    (suncoords[0]+15,suncoords[1]),(suncoords[0]+40,suncoords[1]),4)
    py.draw.line(screen,(247,255,0),\
    (suncoords[0]-10,suncoords[1]-10),(suncoords[0]-35,suncoords[1]-25),5)
    py.draw.line(screen,(247,255,0),\
    (suncoords[0]+10,suncoords[1]-10),(suncoords[0]+35,suncoords[1]-25),5)
    py.draw.line(screen,(247,255,0),\
    (suncoords[0]-10,suncoords[1]+10),(suncoords[0]-35,suncoords[1]+25),5)
    py.draw.line(screen,(247,255,0),\
    (suncoords[0]+10,suncoords[1]+10),(suncoords[0]+35,suncoords[1]+25),5)
    py.draw.line(screen,(247,255,0),\
    (suncoords[0],suncoords[1]+35),(suncoords[0],suncoords[1]-35),4)
    py.draw.rect(screen, color["green"], ((0, 350), (800, 500))) #зелень
    py.draw.rect(screen, (129,128,128), ((0, 450), (800, 100))) #асфальт
    py.draw.rect(screen, (255,255,255), ((0, 495), (800, 8))) #полоса
    track()
    py.draw.rect(screen,(139,69,19),\
    ((treecoords[0][0],330),(treecoords[0][1],40)))
    py.draw.ellipse(screen,(0,80,0),\
    ((treecoords[1][0],290,),(treecoords[1][1],60)))
    py.draw.rect(screen,(139,69,19),\
    ((treecoords[2][0],370),(treecoords[2][1],40)))
    py.draw.ellipse(screen,(0,80,0),\
    ((treecoords[3][0],330,),(treecoords[3][1],60)))
    py.draw.rect(screen,(139,69,19),\
    ((treecoords[4][0],330),(treecoords[4][1],40)))
    py.draw.ellipse(screen,(0,80,0),\
    ((treecoords[5][0],290,),(treecoords[5][1],60)))
    py.draw.rect(screen,(139,69,19),\
    ((treecoords[6][0],370),(treecoords[6][1],40)))
    py.draw.ellipse(screen,(0,80,0),\
    ((treecoords[7][0],330,),(treecoords[7][1],60)))
    py.draw.rect(screen,(139,69,19),\
    ((treecoords[8][0],330),(treecoords[8][1],40)))
    py.draw.ellipse(screen,(0,80,0),\
    ((treecoords[9][0],290,),(treecoords[9][1],60)))
    py.draw.rect(screen,(139,69,19),\
    ((treecoords[10][0],370),(treecoords[10][1],40)))
    py.draw.ellipse(screen,(0,80,0),\
    ((treecoords[11][0],330,),(treecoords[11][1],60)))

    x1 = -14.8*cos(t1)
    fx1 = 14.8*sin(t1)
    x2 = -14.8*cos(t2)
    fx2 = 14.8*sin(t2)

    
    py.draw.line(screen,(128,128,128),(345+x1,520-fx1),(345-x1,520+fx1),3)
    py.draw.line(screen,(128,128,128),(345+x2,520-fx2),(345-x2,520+fx2),3)
    py.draw.line(screen,(128,128,128),(435+x1,520-fx1),(435-x1,520+fx1),3)
    py.draw.line(screen,(128,128,128),(435+x2,520-fx2),(435-x2,520+fx2),3)

    c = 0
    for i in range(50,800,300):
        if c%2 == 0:
            y = 50
        else:
            y = 80
        py.draw.ellipse(screen,(255,255,255),((i,y),(120,40)))
        py.draw.ellipse(screen,(255,255,255),((i+20,y-10),(80,60)))
        c += 1
    py.display.flip()
    clock.tick(15)
    
    for i in range(len(treecoords)):
        treecoords[i][0] -= 10
        if treecoords[i][0] + treecoords[i][1]/2 < 0:
            treecoords[i][0] = 800 - treecoords[i][1]/2

    suncoords[1] += 10
    if suncoords[1] - 50 > 350:
        suncoords[1] = 40
    
    t1 += 0.3
    t2 += 0.3


py.quit()

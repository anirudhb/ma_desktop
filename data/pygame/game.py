#!/usr/bin/env python

# Housekeeping stuff
import pygame, sys, random
from pygame.locals import *
pygame.init()
random.seed()

sHeight = random.randint(640, 1000)
sWidth = random.randint(480, 700)

# Screen & title
screen = pygame.display.set_mode((sHeight, sWidth), 0, 32)
pygame.display.set_caption("Eat The Apples")

# Colors
RED = pygame.Color("red")
YELLOW = pygame.Color("yellow")
GREEN = pygame.Color("green")
LGREEN = pygame.Color("lightgreen")
LYELLOW = pygame.Color("lightyellow")
LLYELLOW = (200, 200, 200)
BLUE = pygame.Color("blue")
WHITE = pygame.Color("white")
BLACK = pygame.Color("black")


# clock = pygame.time.Clock()


x = 0
y = 0

score = 0
maxScore = 10
size = 40
width = size
height = 40
applex = random.randint(0, screen.get_width()-size)
appley = random.randint(0, screen.get_height()-size)
appleColor = RED
move = size
font = pygame.font.SysFont("cursive", 50, True)
win = font.render("You win!", True, GREEN)

times = 0

def drawRect(surface, color, rect, width=0):
    rect = pygame.draw.rect(surface, color, rect, width)
    return rect, color

def newApple():
    global applex, appley, appleColor
    applex = random.randint(size, screen.get_width()-size)
    appley = random.randint(size, screen.get_height()-size)
    appleColor = random.choice([RED, YELLOW, LGREEN])

def resetGame():
    global applex, appley, appleColor, width, score, times, maxScore
    applex = random.randint(size, screen.get_width()-size)
    appley = random.randint(size, screen.get_height()-size)
    appleColor = random.choice([RED, YELLOW, LGREEN])
    width = size
    score = 0
    times = 0
    maxScore += maxScore

def changeSize():
    global sHeight, sWidth, screen
    sHeight = random.randint(640, 1000)
    sWidth = random.randint(480, 700)
    screen = pygame.display.set_mode((sHeight, sWidth), 64)

def renderScore():
    font = pygame.font.SysFont("Courier New", size, True)
    text = font.render(str(score), True, BLACK)
    return text


def showMouse():
    pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, LLYELLOW, pos, size*2, 2)

# Mainloop

while 1:
    # No mouse for games
    pygame.mouse.set_visible(False)
    if x > screen.get_width():
        x = 0
    if x < 0:
        x = 0
    if y > screen.get_height():
        y = 0
    if y < 0:
        y = 0

    screen.fill(WHITE)

    showMouse()
    greenr = pygame.draw.rect(screen, GREEN, Rect(x, y, width, size))
    apple = drawRect(screen, appleColor, Rect(applex, appley, size, size))

    # Scorekeeper
    screen.blit(renderScore(), (0, 0))

    if greenr.colliderect(apple[0]):
        if apple[1] == RED:
            score += 1
        if apple[1] == YELLOW:
            score += 5
            width += size
        if apple[1] == LGREEN:
            score += -5
            width = size
        changeSize()
        newApple()



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                x += move
            if event.key == K_LEFT:
                x -= move
            if event.key == K_UP:
                y -= move
            if event.key == K_DOWN:
                y += move
            if event.key == K_h:
                # They want to know how to play
                font = pygame.font.SysFont("Courier New", 12, True)
                for i in range(2000):
                    t = 'You play by eating apples. You move with arrow keys. Green apples make you lose 5 points.'
                    text = font.render(t, True, BLACK)
                    screen.fill(WHITE)
                    screen.blit(text, (0, screen.get_height()/2-80))
                    pygame.display.update()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if apple[0].collidepoint(pygame.mouse.get_pos()):
                newApple()


    if score > maxScore:
        # They won
        screen.fill(WHITE)
        screen.blit(win, (screen.get_width()/2-85, screen.get_height()/2))
        times += 1
    if times == 240:
        resetGame()
        renderScore()


    pygame.display.update()

    # clock.tick(120)

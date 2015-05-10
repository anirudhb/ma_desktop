#!/usr/bin/env python
import pygame, sys, time
from pygame.locals import *
pygame.init()

cat = 'cat.png'

screen = pygame.display.set_mode((400, 400), 0, 32)

cimg = pygame.image.load(cat).convert()
white = (255, 255, 255)
pygame.display.set_caption('Pygame GUI For Siddhi')
f = pygame.font.SysFont('Arial', 48, True)
t = f.render('This is green text', True, (0, 255, 0))
tr = f.render('This is red', True, (255, 0, 0))

s = pygame.mixer.Sound('beep.wav')




while True:
        s.play()
        time.sleep(1)
        s.stop()
        screen.fill(white)
        screen.blit(cimg, screen.get_rect().center)
        screen.blit(t, screen.get_rect())
        screen.blit(tr, (50, 50))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                                s.stop()
                                time.sleep(10)
                        if event.key == K_F10:
                                import tkMessageBox
                                tkMessageBox.showerror('KeyError', "Cannot find key 'F10' on keyboard or in character map")
                        if event.key == K_p:
                                import tkMessageBox
                                tkMessageBox.showinfo('Peace', 'You get peace for as long as you keep this window open!')
                                



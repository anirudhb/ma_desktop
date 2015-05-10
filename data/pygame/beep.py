import pygame
pygame.init()

beep = pygame.mixer.Sound("printer.wav")

while True:
    beep.play()

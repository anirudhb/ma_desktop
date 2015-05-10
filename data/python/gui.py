from pygame.locals import *
import os
class Window:
	def __init__(self, title, size=(400, 400)):
		import pygame
		pygame.init()
		self.screen = pygame.display.set_mode(size, 0, 32)
		pygame.display.set_caption(title)

	def mainloop(self):
		import pygame
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					os._exit(0)

win = Window(title='Example Implementation Of GUIs In Python')
win.mainloop()


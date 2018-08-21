import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface
W, H = 1920, 1080
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Template")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

# main loop
while True:
	events()

	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)

# code.Pylet - Rectangle Based Collisions Detection
# watch the video here - https://youtu.be/0xYzcS_b0ng
# Any questions? Just ask!

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
pygame.display.set_caption("code.Pylet - Rectangle Based Collisions")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)

WHITE_STAR = pygame.image.load("whitestar-100x100.png").convert_alpha()
GREEN_STAR = pygame.image.load("greenstar-100x100.png").convert_alpha()
RED_STAR = pygame.image.load("redstar-100x100.png").convert_alpha()

class rectangle:
	def __init__(self, x, y, id):
		w = h = 100 # cheating
		
		self.x1 = x
		self.y1 = y
		self.x2 = x + w
		self.y2 = y + h
		
		self.w = w
		self.h = h
		
		self.xMargin = int(w * 0.125)
		self.yMargin = int(h * 0.125)
		
		self.starColor = WHITE_STAR

		self.stained = False
		self.id = id
		
	def setXY(self, xy):
		self.x1, self.y1 = xy
		self.x2 = xy[0] + self.w
		self.y2 = xy[1] + self.h
	
	def getXY(self):
		return (self.x1, self.y1)
	
	def rect(self):
		return self.getXY() + (self.w, self.h)
		
	def coords(self):
		return self.getXY() + (self.x2, self.y2)
		
	def hasCollided(self, target):
		tx1, ty1, tx2, ty2 = target.coords()
		if tx1 + target.xMargin > self.x2 - self.xMargin \
		or tx2 - target.xMargin < self.x1 + self.xMargin \
		or ty1 + target.yMargin > self.y2 - self.yMargin \
		or ty2 - target.yMargin < self.y1 + self.yMargin : return False
		return True
	
	def draw(self, surface = None):
		if not surface: surface = pygame.display.get_surface()
		surface.blit(self.starColor, self.getXY())
		
rectangles = list([rectangle(random.randint(0, W), random.randint(0, H), i) for i in range(0, 10)])
rectangles[0].starColor = GREEN_STAR
		
# main loop
while True:
	events()

	mb = pygame.mouse.get_pressed()
	rectangles[0].setXY(pygame.mouse.get_pos())
	
	for r in rectangles:
		if r.id == 0: continue
		r .draw()
		
		result = r.hasCollided(rectangles[0])
		if result:
			r.starColor = RED_STAR
			if mb[0]: r.stained = True
		else:
			if not r.stained: r.starColor = WHITE_STAR
	
	rectangles[0].draw()
	
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)
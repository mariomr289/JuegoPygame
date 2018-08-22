# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *

from mapa import *

# Clases
# ---------------------------------------------------------------------

class Chara(pygame.sprite.Sprite):
	def __init__(self, fil, col, filename):
		pygame.sprite.Sprite.__init__(self)
		
		self.images, self.rects = cortar_sprite(filename, fil, col)
		
		self.fil = fil
		self.col = col
		
		self.w = self.images[0][0].get_width()
		self.h = self.images[0][0].get_height()
			
		self.image = self.images[0][0]
		self.rect = self.rects[0][0]
		
		

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

def cortar_sprite(ruta, fil, col):
	image = load_image(ruta, True)
	rect = image.get_rect()
	w = rect.w / col
	h = rect.h / fil
	sprite = range(fil)
	rects = range(fil)
	
	for i in range(fil):
		sprite[i] = range(col)
		rects[i] = range(col)
		
	for f in range(fil):
		for c in range(col):
			sprite[f][c] = image.subsurface((rect.left, rect.top, w, h))
			rects[f][c] = sprite[f][c].get_rect()
			rect.left += w
		rect.top += h
		rect.left = 0
		
	return sprite, rects

# ---------------------------------------------------------------------

def main():
	
	return 0

if __name__ == '__main__':
	main()

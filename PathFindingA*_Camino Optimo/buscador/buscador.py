#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *

from mapa import *
from actor import *

# Constantes
WIDTH = 640
HEIGHT = 480

# Clases
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

# ---------------------------------------------------------------------

def main():
	mapa = Mapa()
	screen = pygame.display.set_mode((mapa.col*32, mapa.fil*32))
	pygame.display.set_caption("Buscador A*")
	
	mapa.convertir()
	chara = Chara(4, 4, "images/chara.png")
	clock = pygame.time.Clock()
	
	while True:
		time = clock.tick(60)
		keys = pygame.key.get_pressed()
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
			if keys[K_ESCAPE]:
				sys.exit(0)
		
		mapa.eventos(screen)
		mapa.mover_chara(chara)
		mapa.actualizar(chara)
		mapa.dibujar(screen)
		pygame.display.flip()
		pygame.time.wait(80)
	return 0

if __name__ == '__main__':
	pygame.init()
	main()

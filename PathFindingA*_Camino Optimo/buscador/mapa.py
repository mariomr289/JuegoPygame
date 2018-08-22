#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
# Módulos
import sys, pygame
from pygame.locals import *
from aestrella import *

# Clases
# ---------------------------------------------------------------------

class Mapa(pygame.sprite.Sprite):
	def __init__(self, archivo="mapa.txt"):
		
		self.mapa = leerMapa(archivo)
		self.fil = len(self.mapa)
		self.col = len(self.mapa[0])
		
		self.chara_pos = buscarPos(2, self.mapa)
		self.camino = 0
		
	def convertir(self):
		pygame.sprite.Sprite.__init__(self)
		self.cesped = load_image("images/cesped.png")
		self.cesped_rect = self.cesped.get_rect()
		
		self.tronco = load_image("images/tronco.png", 1)
		self.tronco_rect = self.tronco.get_rect()
		
				
	def __str__(self):
		salida = ""
		for f in range(self.fil):
			for c in range(self.col):
				if self.mapa[f][c] == 0:
					salida += "  "
				if self.mapa[f][c] == 1:
					salida += "# "
				if self.mapa[f][c] == 2:
					salida += "T "
				if self.mapa[f][c] == 3:
					salida += "S "
			salida += "\n"
		return salida
	
	def eventos(self, screen):
		raton = pygame.mouse.get_pressed()
		if raton[0]:
			pos_raton = pygame.mouse.get_pos()
			x = pos_raton[0] / 32
			y = pos_raton[1] / 32
			if self.mapa[y][x] == 0:
				self.mapa[y][x] = 1
			elif self.mapa[y][x] == 1:
				self.mapa[y][x] = 0
		if raton[2]:
			pos_raton = pygame.mouse.get_pos()
			x = pos_raton[0] / 32
			y = pos_raton[1] / 32
			if self.mapa[y][x] == 0:
				self.mapa[y][x] = 3
				A = AEstrella(self.mapa)
				self.mapa[y][x] = 0
				if A.camino == -1:
					tex, tex_rec = texto("Imposible", (self.col*32)/2, (self.fil*32)/2)
					screen.blit(tex, tex_rec)
					pygame.display.flip()
					pygame.time.wait(160)
				else:
					self.camino = A.camino
	
	def actualizar(self, chara):
		self.salida = []
		for f in range(self.fil):
			for c in range(self.col):
				if self.mapa[f][c] == 1:
					self.salida.append([self.tronco, (self.tronco_rect.w*c, self.tronco_rect.h*f)])
				if self.mapa[f][c] == 2:
					self.salida.append([chara.image, (chara.rect.w*c, 32*f-16)])
					
	def mover_chara(self, chara):
		if self.camino:
			if self.chara_pos[0] < self.camino[0][0]:
				self.mapa[self.chara_pos[0]][self.chara_pos[1]] = 0
				self.mapa[self.chara_pos[0]+1][self.chara_pos[1]] = 2
				self.chara_pos[0] += 1
				chara.image = chara.images[0][0]
				del self.camino[0]
				return self.camino
			if self.chara_pos[0] > self.camino[0][0]:
				self.mapa[self.chara_pos[0]][self.chara_pos[1]] = 0
				self.mapa[self.chara_pos[0]-1][self.chara_pos[1]] = 2
				self.chara_pos[0] -= 1
				del self.camino[0]
				chara.image = chara.images[3][0]
				return self.camino
			if self.chara_pos[1] < self.camino[0][1]:
				self.mapa[self.chara_pos[0]][self.chara_pos[1]] = 0
				self.mapa[self.chara_pos[0]][self.chara_pos[1]+1] = 2
				self.chara_pos[1] += 1
				chara.image = chara.images[2][0]
				del self.camino[0]
				return self.camino
			if self.chara_pos[1] > self.camino[0][1]:
				self.mapa[self.chara_pos[0]][self.chara_pos[1]] = 0
				self.mapa[self.chara_pos[0]][self.chara_pos[1]-1] = 2
				chara.image = chara.images[1][0]
				self.chara_pos[1] -= 1
				del self.camino[0]
				return self.camino
		
	def dibujar(self, screen):
		for f in range(self.fil):
			for c in range(self.col):
				screen.blit(self.cesped, (self.cesped_rect.w*c, self.cesped_rect.h*f))
		for i in range(len(self.salida)):
			screen.blit(self.salida[i][0], self.salida[i][1])

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

def texto(texto, posx, posy, color=(255, 255, 255)):
	fuente = pygame.font.Font("images/DroidSans.ttf", 25)
	salida = pygame.font.Font.render(fuente, texto, 1, color)
	salida_rect = salida.get_rect()
	salida_rect.centerx = posx
	salida_rect.centery = posy
	return salida, salida_rect

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

# Quita el ultimo caracter de una lista.
def quitarUltimo(lista):
	for i in range(len(lista)):
		lista[i] = lista[i][:-1]
	return lista

# Covierte una cadena en una lista.	
def listarCadena(cadena):
	lista = []
	for i in range(len(cadena)):
		if cadena[i] == ".":
			lista.append(0)
		if cadena[i] == "#":
			lista.append(1)
		if cadena[i] == "T":
			lista.append(2)
		if cadena[i] == "S":
			lista.append(3)
	return lista

# Lee un archivo de texto y lo convierte en una lista.
def leerMapa(archivo):
	mapa = open(archivo, "r")
	mapa = mapa.readlines()
	mapa = quitarUltimo(mapa)
	for i in range(len(mapa)):
		mapa[i] = listarCadena(mapa[i])
	return mapa

# ---------------------------------------------------------------------

def main():
	mapa = Mapa()
	print mapa
	return 0

if __name__ == '__main__':
	main()

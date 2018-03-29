import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Tutorial Nueve")

Mi_imagen = pygame.image.load("imagenes/Military-Tank-38.png")
posX = 200
posY = 100

velocidad = 5
Blanco = (255,255,255)
derecha = True

while True:
    ventana.fill(Blanco)
    ventana.blit(Mi_imagen,(posX,posY))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == K_LEFT:
                posX -= velocidad
            elif evento.key == K_RIGHT:
                posX += velocidad
        elif evento.type == pygame.KEYUP:
            if evento.key == K_LEFT:
                print "Tecla Izquierda Liberada"
            elif evento.key == K_RIGHT:
                print "Tecla Derecha Liberada"

    pygame.display.update()

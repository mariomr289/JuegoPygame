#Rojo, Verde y Azul

import pygame,sys
from pygame.locals import *

Color = (0,140,60)
ColorDos = pygame.Color(255,120,9)

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola Mundo")

while True:
    ventana.fill(ColorDos)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

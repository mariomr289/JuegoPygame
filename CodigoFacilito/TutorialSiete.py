import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((700,600))
pygame.display.set_caption("Tutorial Siete")

Mi_imagen = pygame.image.load("imagenes/Military-Tank-38.png")
posX = randint(10,400)
posY = randint(10,300)

ventana.blit(Mi_imagen,(posX,posY))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

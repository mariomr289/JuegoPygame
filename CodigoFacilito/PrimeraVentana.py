import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola Mundo")

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

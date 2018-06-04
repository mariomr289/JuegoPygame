import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((700,600))
pygame.display.set_caption("Tutorial Seis")

Mi_imagen = pygame.image.load("imagenes/Military-Tank-38.png")
posX,posY = 130,70

# Inicializar posiciones
#posX=130
#posY=70

ventana.blit(Mi_imagen,(posX,posY))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

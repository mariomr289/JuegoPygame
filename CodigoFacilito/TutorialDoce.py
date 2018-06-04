import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Doce")

miFuente = pygame.font.Font(None,30)
miTexto = miFuente.render("Prueba Fuente",0,(200,60,80))

miFuenteSistema = pygame.font.SysFont("Arial",50)
miTextoSistema = miFuente.render("Prueba Fuente Sistema",0,(200,60,80))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ventana.blit(miTextoSistema,(0,0))
    ventana.blit(miTexto,(100,100))
    pygame.display.update()

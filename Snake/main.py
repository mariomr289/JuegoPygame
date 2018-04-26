import pygame
from pygame.locals import *
import sys

pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake: By Mario")

# Ciclo del juego
while True:
    #Cuerpo de eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    pass

print "Todo Funcionando"

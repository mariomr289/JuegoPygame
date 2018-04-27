import pygame
from pygame.locals import *
import sys
import grafitero

pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake: By Mario")
g = grafitero.grafica()

# Variables
fase = 0
seleccionmenu = 0

# Ciclo del juego
while True:
    g.Fondo()
    g.Titulo(seleccionmenu)
    #Cuerpo de eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            pass
        elif evento.type == KEYDOWN:
            if fase == 0:
                if evento.key == pygame.K_DOWN:
                    if seleccionmenu < 1:
                        seleccionmenu += 1
                    else:
                        seleccionmenu = 0
                elif evento.key == pygame.K_UP:
                    if seleccionmenu > 0:
                        seleccionmenu -= 1
                    else:
                        seleccionmenu = 1
        elif evento.type == KEYUP:
            pass

    pygame.display.update()
    pass

print "Todo Funcionando"

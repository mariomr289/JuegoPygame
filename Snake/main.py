import pygame
from pygame.locals import *
import sys
import grafitero
import time

pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake: By Mario")
g = grafitero.grafica()

# Variables
fase = 0
seleccionmenu = 0

# Ciclo del juego
while True:
    if fase == 0:
        g.Fondo()
        g.Titulo(seleccionmenu)
    elif fase == 1:
        g.Fondo()
        g.DibujarSnake()
        pass
    elif fase == 2:
        g.Fondo()
        g.Creditos()
        pass
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
                elif evento.key == pygame.K_z:
                    if seleccionmenu == 0:
                        fase = 1
                    elif seleccionmenu == 1:
                        fase =2
            elif fase == 2:
                if evento.key == pygame.K_x:
                    fase = 0
        elif evento.type == KEYUP:
            pass

    pygame.display.update()
    time.sleep(0.03)
    pass

print "Todo Funcionando"

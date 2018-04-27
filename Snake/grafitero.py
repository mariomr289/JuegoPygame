import pygame
from pygame.locals import *
pygame.init()

ventana = pygame.display.set_mode((800,600))
VerdeFondo = (80,120,80)
VerdeObjeto = (30,40,30)

# Fuentes
Fuente_Titulo = pygame.font.Font("Font/PressStart2P-Regular.ttf",50)

# Renders
Titulo = Fuente_Titulo.render("Classic Snake", True, VerdeObjeto)

class grafica(object):
    def __init__(self):
        print "Nuevas graficas creadas"
        pass
    def Fondo(slef):
        ventana.fill(VerdeFondo)

    def Titulo(self):
        ventana.blit(Titulo,(80,50))
        pass

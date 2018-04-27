import pygame
from pygame.locals import *
pygame.init()

ventana = pygame.display.set_mode((800,600))
VerdeFondo = (80,120,80)
VerdeObjeto = (30,40,30)
VerdeObjetoClaro = (50,60,50)

# Fuentes
Fuente_Titulo = pygame.font.Font("Font/PressStart2P-Regular.ttf",50)
Fuente_Menu = pygame.font.Font("Font/PressStart2P-Regular.ttf",25)
Fuente_Texto = pygame.font.Font("Font/PressStart2P-Regular.ttf",15)

# Renders
Titulo = Fuente_Titulo.render("Classic Snake", True, VerdeObjeto)
UnJugador = Fuente_Menu.render("Un Jugador", True, VerdeObjeto)
Creditos = Fuente_Menu.render("Creditos", True, VerdeObjeto)
InstruccionMenu = Fuente_Texto.render("Presione Z para entrar a la opcion",True, VerdeObjeto)

class grafica(object):
    def __init__(self):
        print "Nuevas graficas creadas"
        pass
    def Fondo(slef):
        ventana.fill(VerdeFondo)

    def Titulo(self, seleccion):
        if seleccion == 0:
            pygame.draw.rect(ventana,VerdeObjetoClaro,(110,200,300,30))
        elif seleccion == 1:
            pygame.draw.rect(ventana,VerdeObjetoClaro,(110,230,300,30))
        ventana.blit(Titulo,(80,50))
        ventana.blit(UnJugador,(120,200))
        ventana.blit(Creditos,(120,230))
        ventana.blit(InstruccionMenu,(10,550))
        pass

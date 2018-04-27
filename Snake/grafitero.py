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
InstruccionMenu = Fuente_Texto.render("Presione Z para entrar a la opcion",True, VerdeObjetoClaro)
InstruccionMenu2 = Fuente_Texto.render("Presione X para volver al menu",True, VerdeObjetoClaro)
Creditos1 = Fuente_Texto.render("Este juego fue desarrollado por",True,VerdeObjetoClaro)
Creditos2 = Fuente_Texto.render("Mario Merlo, sin fines de lucro",True,VerdeObjetoClaro)
Creditos3 = Fuente_Texto.render("Crear. Solor para disfrutar...",True,VerdeObjetoClaro)

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
    def Creditos(self):
        ventana.blit(Creditos, (120,230))
        ventana.blit(Creditos1, (120,260))
        ventana.blit(Creditos2, (120,280))
        ventana.blit(Creditos3, (120,300))
        ventana.blit(InstruccionMenu2,(10,550))

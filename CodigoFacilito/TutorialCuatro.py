import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Tutorial Cuatro")

Color = pygame.Color(70,80,150)
pygame.draw.line(ventana,Color,(60,80),(160,100),8)

print Color.r
print Color.g
print Color.b

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

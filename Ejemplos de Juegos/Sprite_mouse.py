import pygame
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((800,600),0,32)
imagen = pygame.image.load("mario.png")

x = 10
y = 10

sprite1 = pygame.sprite.Sprite()
sprite1.image = imagen

reloj = pygame.time.Clock()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()

    reloj.tick(25)
    pantalla.fill((0,0,0))
    pantalla.blit(sprite1.image,(x,y))
    x,y = pygame.mouse.get_pos()
    pygame.display.update()

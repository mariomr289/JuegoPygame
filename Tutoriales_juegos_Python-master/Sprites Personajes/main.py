# -*- coding: utf-8 -*-

import pygame
import player

pygame.init()

# Definimos algunas variables que usaremos en nuestro código

ancho_ventana = 954
alto_ventana = 710
screen = pygame.display.set_mode((ancho_ventana, alto_ventana), pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF)
pygame.display.set_caption("Tutorial sprites Piensa 3D")
clock = pygame.time.Clock()
player = player.Kate((ancho_ventana/2, alto_ventana/2))
game_over = False

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    player.handle_event(event)
    screen.fill(pygame.Color('gray'))
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(20)

pygame.quit ()

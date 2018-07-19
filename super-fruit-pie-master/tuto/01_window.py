#!/usr/bin/python
# -*- coding: utf-8 -*-

# David Art <david.madbox@gmail.com>
# Program Arcade Games With Python And Pygame - Build a Platformer
# http://programarcadegames.com

import pygame

pygame.init()

size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RaspJam")
color = (0,0,0) # black
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            done = True

    screen.fill(color)
    pygame.display.flip()
    clock.tick(60)

pygame.quit ()


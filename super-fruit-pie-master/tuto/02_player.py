#!/usr/bin/python
# -*- coding: utf-8 -*-

# David Art <david.madbox@gmail.com>
# Program Arcade Games With Python And Pygame - Build a Platformer
# http://programarcadegames.com

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):

    def __init__(self, width=32, height=32):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([width, height])
       self.image.fill(YELLOW)
       self.rect = self.image.get_rect()

# Initialize the window
pygame.init()

# Set the height and width of the screen
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RaspJam")

player = Player()
player.rect.x = 200
player.rect.y = 200

allsprites = pygame.sprite.RenderPlain((player))
#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= 8
            if event.key == pygame.K_RIGHT:
                player.rect.x += 8
            if event.key == pygame.K_UP:
                player.rect.y -= 8
            if event.key == pygame.K_DOWN:
                player.rect.y += 8

    screen.fill(BLACK)
    allsprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit ()

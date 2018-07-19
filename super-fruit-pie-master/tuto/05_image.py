#!/usr/bin/python
# -*- coding: utf-8 -*-

# RaspJam : basic 2D game
# David Art <david.madbox@gmail.com>
# Program Arcade Games With Python And Pygame - Build a Platformer
# http://programarcadegames.com

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
WIDTH, HEIGHT = 640, 480


class Platform (pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/block.png')
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0
    jump_ok = True
    frame_since_collision = 0

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,blocks):

        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, blocks, False)

        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, blocks, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.jump_ok = True

            # Keep track of the last time we hit something
            self.frame_since_collision = 0

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

        # If we haven't hit anything in a while, allow us jump
        if self.frame_since_collision > 2:
            self.jump_ok = False

        # Increment frame counter
        self.frame_since_collision += 1

    # Calculate effect of gravity.
    def calc_grav(self):
        self.change_y += .4

        # See if we are on the ground.
        if self.rect.y >= HEIGHT-30 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT-30
            self.frame_since_collision = 0
            self.jump_ok = True

    # Called when user hits 'jump' button
    def jump(self,blocks):

        # If it is ok to jump, set our speed upwards
        if self.jump_ok:
            self.change_y = -9.81

# Create platforms
def create_level1(block_list,all_sprites_list):


    block = Platform(WHITE, 128, 16)
    block.rect.x = 160
    block.rect.y = 128
    block_list.add(block)
    all_sprites_list.add(block)

    block = Platform(WHITE, 128, 16)
    block.rect.x = 352
    block.rect.y = 128
    block_list.add(block)
    all_sprites_list.add(block)


    block = Platform(WHITE, 128, 16)
    block.rect.x = 0
    block.rect.y = 432
    block_list.add(block)
    all_sprites_list.add(block)

    block = Platform(WHITE, 128, 16)
    block.rect.x = WIDTH - 128
    block.rect.y = 432
    block_list.add(block)
    all_sprites_list.add(block)


    block = Platform(WHITE, 128, 16)
    block.rect.x = 0
    block.rect.y = 240
    block_list.add(block)
    all_sprites_list.add(block)

    block = Platform(WHITE, 128, 16)
    block.rect.x = WIDTH - 128
    block.rect.y = 240
    block_list.add(block)
    all_sprites_list.add(block)


    block = Platform(WHITE, 128, 16)
    block.rect.x = 160
    block.rect.y = 336
    block_list.add(block)
    all_sprites_list.add(block)

    block = Platform(WHITE, 128, 16)
    block.rect.x = 352
    block.rect.y = 336
    block_list.add(block)
    all_sprites_list.add(block)

# Initialize the window
pygame.init()
# Set the height and width of the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("RaspJam")
background = pygame.image.load('images/bg.png')
# Main program, create the blocks
block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

create_level1(block_list,all_sprites_list)

player = Player(20, 15)

player.rect.x = 240
player.rect.y = 0

all_sprites_list.add(player)

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:

    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x = -6
            if event.key == pygame.K_RIGHT:
                player.change_x = 6
            if event.key == pygame.K_SPACE:
                player.jump(block_list)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_x = 0
            if event.key == pygame.K_RIGHT:
                player.change_x = 0

    # --- Game Logic
    # Wrap player around the screen
    if player.rect.x >= WIDTH:
        player.rect.x = -15

    if player.rect.x <= -16:
        player.rect.x = WIDTH

    player.calc_grav()
    player.update(block_list)
    block_list.update()

    # --- Draw Frame
    #~ screen.fill(BLACK)
    screen.blit(background, (0, 0))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit ()

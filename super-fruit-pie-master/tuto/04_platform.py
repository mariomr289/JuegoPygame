#!/usr/bin/python
# -*- coding: utf-8 -*-

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

# This class represents the platform we jump on
class Platform (pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # Set to true if it is ok to jump
    jump_ok = True

    # Count of frames since the player
    # collided against something. Used to prevent jumping
    # when we haven't hit anything.
    frame_since_collision = 0

    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image = pygame.Surface([16, 16])
        self.image.fill(YELLOW)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Find a new position for the player
    def update(self,blocks):

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, blocks, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, blocks, False)
        for block in block_hit_list:

            # We hit something below us. Set the boolean to flag that we can jump
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
        if self.frame_since_collision > 3:
            self.jump_ok = False

        # Increment frame counter
        self.frame_since_collision += 1

    # Calculate effect of gravity.
    def calc_grav(self):
        self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= HEIGHT-16 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT-16
            self.frame_since_collision = 0
            self.jump_ok = True

    # Called when user hits 'jump' button
    def jump(self,blocks):

        # If it is ok to jump, set our speed upwards
        if self.jump_ok:
            self.change_y = -8

# Create platforms
def create_level1(block_list,all_sprites_list):

    # 7 blocks
    for i in range(4):
        block = Platform(WHITE, 128, 16)
        # Set x and y based on block number
        block.rect.x = 64 + 128 * i
        block.rect.y = 160 + 80 * i

        block_list.add(block)
        all_sprites_list.add(block)

# Initialize the window
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption("RaspJam")

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
    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit ()

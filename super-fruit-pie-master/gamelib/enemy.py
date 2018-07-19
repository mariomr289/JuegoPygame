import pygame
import random

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 310
        self.rect.y = 30
        self.direction = random.choice([True, False])
        self.dy = 0
        self.dx = 100
        self.resting = False
        self.is_dead = False

    def update(self, dt, game):
        last = self.rect.copy()

        if self.direction:
            self.rect.x -= self.dx * dt
        else:
            self.rect.x += self.dx * dt

        self.dy = min(400, self.dy + 30)
        self.rect.y += self.dy * dt

        new = self.rect
        self.resting = False
        for cell in pygame.sprite.spritecollide(self, game.block_list, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
                self.direction = not self.direction
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
                self.direction = not self.direction
            if last.bottom <= cell.top and new.bottom > cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.dy = 0

        if self.rect.x >= game.width:
            self.rect.x = -15

        if self.rect.x <= -16:
            self.rect.x = game.width

        if self.rect.y >= game.height:
            self.is_dead = True

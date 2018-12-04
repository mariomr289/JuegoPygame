import pygame
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((800,600),0,32)
imagen = pygame.image.load("mario.png")

x = 10
y = 10

sprite1 = pygame.sprite.Sprite()
sprite1.image = imagen
sprite1.rect = imagen.get_rect()

sprite1.rect.top = y
sprite1.rect.left = x

rectangulo = pygame.Rect(300, 0, 10, 400)

reloj = pygame.time.Clock()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pulsada = pygame.key.get_pressed()
    if pulsada[K_UP]:
        sprite1.rect.top -= 5
    if pulsada[K_DOWN]:
        sprite1.rect.top += 5
    if pulsada[K_LEFT]:
        sprite1.rect.left -= 5
    if pulsada[K_RIGHT]:
        sprite1.rect.left += 5
    if rectangulo.colliderect(sprite1):
        sprite1.rect.left = oldx
        sprite1.rect.top = oldy

    oldx = sprite1.rect.left
    oldy = sprite1.rect.top
    reloj.tick(25)
    pantalla.fill((0,0,0))
    pantalla.blit(sprite1.image, sprite1.rect)
    pygame.draw.rect(pantalla, (255, 255, 255), rectangulo )
    pygame.display.update()

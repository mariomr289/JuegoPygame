#!/usr/bin/python
# -*- encoding: utf-8 -*-
import pygame

#Constantes del juego Colores, Ancho y Alto de la pantalla
ANCHO = 640
ALTO = 480

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

class Protagonista(pygame.sprite.Sprite):

    def __init__(self):
        self.image = pygame.image.load("hombre.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.speed = [0.5, -0.5]

    def mover_derecha(self, pixeles):
        self.rect.x = self.rect.x + pixeles

    def mover_izquierda(self, pixeles):
        self.rect.x = self.rect.x - pixeles

    def mover_arriba(self, pixeles):
        self.rect.y = self.rect.y - pixeles

    def mover_abajo(self, pixeles):
        self.rect.y = self.rect.y + pixeles


pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura] y establecemos el titulo
dimensiones = (ANCHO, ALTO)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Primer juego en PyGame")

#Cargamos la imagen de fondo del juego (escenario)
background_image = pygame.image.load("fondo.png")

# El bucle del juego se ejecuta hasta que el usuario hace click sobre el botón de cierre.
hecho = False

# Se usa para establecer cuan rapido se actualiza la pantalla
reloj = pygame.time.Clock()




hombresito = Protagonista()

# Game loop
while not hecho:
    # Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # --- LA LOGICA DEL JUEGO DEBERIA IR AQUI

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        hombresito.mover_izquierda(3)
    if pressed[pygame.K_RIGHT]:
        hombresito.mover_derecha(3)
    if pressed[pygame.K_UP]:
        hombresito.mover_arriba(3)
    if pressed[pygame.K_DOWN]:
        hombresito.mover_abajo(3)

    # --- EL CODIGO DE DIBUJO DEBERIA IR AQUI

    pantalla.blit(background_image, (0, 0))
    pantalla.blit(hombresito.image, hombresito.rect)

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)

# Cerramos la ventana y salimos.
pygame.quit()

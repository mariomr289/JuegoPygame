# -*- coding: utf-8 -*-

import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME

# Definimos el tamaño de la ventana

windowWidth = 600
windowHeight = 650

# Inicializamos el juego y la ventana
pygame.init()
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pruebas sonoras PyGame')

# Definimos la variable donde guardaremos los diferentes botones
buttons = []
stopButton = { "image" : pygame.image.load("assets/images/stop.png"), "position" : (275, 585)}

# Definimos una variable para guardar la posicion del raton y el volumen
mousePosition = None
volume = 1.0

pygame.mixer.init()
pygame.mixer.music.load('assets/sounds/OGG/farm.ogg')
pygame.mixer.music.play(-1)

# Definimos las funciones que usaremos en nuestro codigo

def drawButtons():
# Funcion para dibujar los botones dentro de la ventana que hemos definido

  for button in buttons:
    surface.blit(button["image"], button["position"])

  surface.blit(stopButton["image"], stopButton['position'])

def drawVolume():
# Funcion para dibujar la barra de volumen y el selector

  pygame.draw.rect(surface, (229, 229, 229), (450, 610, 100, 5))

  volumePosition = (100 / 100) * (volume * 100)

  pygame.draw.rect(surface, (204, 204, 204), (450 + volumePosition, 600, 10, 25))

def handleClick():
# Funcion para poder conocer la posición del cursor sobre la ventana

  global mousePosition, volume

# Primero miramos la posicion de todos los botones que hemos colocado y luego comprobamos que tenemos el cursor encima
  for button in buttons:

    buttonSize = button['image'].get_rect().size
    buttonPosition = button['position']

    if mousePosition[0] > buttonPosition[0] and mousePosition[0] < buttonPosition[0] + buttonSize[0]:

      if mousePosition[1] > buttonPosition[1] and mousePosition[1] < buttonPosition[1] + buttonSize[1]:
        button['sound'].set_volume(volume)
        button['sound'].play()

    if mousePosition[0] > stopButton['position'][0] and mousePosition[0] < stopButton['position'][0] + stopButton['image'].get_rect().size[0]:
      if mousePosition[1] > stopButton['position'][1] and mousePosition[1] < stopButton['position'][1] + stopButton['image'].get_rect().size[1]:
        pygame.mixer.stop()

def checkVolume():
# Funcion para poder realizar los cambios en el volumen

  global mousePosition, volume

  if pygame.mouse.get_pressed()[0] == True:

    if mousePosition[1] > 600 and mousePosition[1] < 625:
      if mousePosition[0] > 450 and mousePosition[0] < 550:
        volume = float((mousePosition[0] - 450)) / 100

def quitGame():
  pygame.quit()
  sys.exit()

# Creamos todos los botones dentro de la ventana
buttons.append({ "image" : pygame.image.load("assets/images/sheep.png"), "position" : (25, 25), "sound" : pygame.mixer.Sound('assets/sounds/OGG/sheep.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/rooster.png"), "position" : (225, 25), "sound" : pygame.mixer.Sound('assets/sounds/OGG/rooster.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/pig.png"), "position" : (425, 25), "sound" : pygame.mixer.Sound('assets/sounds/OGG/pig.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/mouse.png"), "position" : (25, 225), "sound" : pygame.mixer.Sound('assets/sounds/OGG/mouse.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/horse.png"), "position" : (225, 225), "sound" : pygame.mixer.Sound('assets/sounds/OGG/horse.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/dog.png"), "position" : (425, 225), "sound" : pygame.mixer.Sound('assets/sounds/OGG/dog.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/cow.png"), "position" : (25, 425), "sound" : pygame.mixer.Sound('assets/sounds/OGG/cow.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/chicken.png"), "position" : (225, 425), "sound" : pygame.mixer.Sound('assets/sounds/OGG/chicken.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/cat.png"), "position" : (425, 425), "sound" : pygame.mixer.Sound('assets/sounds/OGG/cat.ogg')})

# Codigo principal de nuestro juego
while True:

  surface.fill((255,255,255))

  mousePosition = pygame.mouse.get_pos()

  for event in GAME_EVENTS.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_ESCAPE:
        quitGame()

    if event.type == GAME_GLOBALS.QUIT:
      quitGame()

    if event.type == pygame.MOUSEBUTTONUP:
      handleClick()

  drawButtons()
  checkVolume()
  drawVolume()

  pygame.display.update()

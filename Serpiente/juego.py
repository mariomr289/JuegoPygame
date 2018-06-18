#!/usr/bin/python
# -*- coding: utf-8 -*-
# Ejemplo de juego hecho solo con funciones
# Modulos a importar
# -----------------------------------------
import pygame, time, random
from pygame.locals import *
# -----------------------------------------
# Variables Constantes no cambian su valor
# -----------------------------------------
# documentos de los Creditos
# -----------------------------------------
archivo = open("creditos.txt","r")
contenido = archivo.read()
# -----------------------------------------
# pantalla
# -----------------------------------------
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla,alto_pantalla))
pygame.display.set_caption('Snake')
reloj = pygame.time.Clock()
# -----------------------------------------
# colores
# -----------------------------------------
blanco = 255,255,255
negro = 0,0,0
rojo = 255,0,0
azul = 0,0,255
verde = 0,255,0
amarillo = 255,255,0
plomo = 232,224,224
cyan = 147,206,222
# -----------------------------------------
# Variables auxiliares
suma = 0
direccion = "izquierda"
pausado = False
fin = False
# imagenes del Juego
# -----------------------------------------
img1 = pygame.image.load('imagenes/cabeza-bocaA.png')
img2 = pygame.image.load('imagenes/cabeza-bocaB.png')
BocaAbierta = pygame.transform.scale(img1,(32,32))
BocaCerrada = pygame.transform.scale(img2,(32,32))
imgMan = pygame.image.load('imagenes/manzana.png')
ImagenManz = pygame.transform.scale(imgMan,(25,25))
# -----------------------------------------
# manzana
# -----------------------------------------
bloqueManzana = 30
#ladoXManzana = 250
#ladoYManzana = 250
# -----------------------------------------
# Inicializacion del constructor del juego
# -----------------------------------------
pygame.init()
# Fuentes
pequenafuente = pygame.font.SysFont("comicsansms",15)
medianafuente = pygame.font.SysFont("comicsansms",30)
grandefuente = pygame.font.SysFont("comicsansms",80)
# -----------------------------------------
# Datos de boton
# -----------------------------------------
Boton1 = [300,290]
TamBoton = [200,45]
ColorBoton1 = [plomo,amarillo]
# -----------------------------------------
Boton2 = [300,340]
ColorBoton2 = [plomo,azul]
# -----------------------------------------
Boton3 = [300,390]
ColorBoton3 = [plomo,verde]
# -----------------------------------------
Boton4 = [300,440]
ColorBoton4 = [plomo,rojo]
# -----------------------------------------
BotonPausa = [550,50]
BotonPtam = [35,35]
ColorBotonP = [plomo,cyan]
# -----------------------------------------
# Funciones a usar dentro del juego
# -----------------------------------------
def creditos():
    entrada = True
    while entrada:
        pantalla.fill(blanco)
        mensaje("Creditos",azul,-200,tamano="grande")
        mensaje(contenido,verde,tamano="pequeno")
        pygame.display.update()
        for action in pygame.event.get():
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_x:
                    quit()
# -----------------------------------------
def TextoBoton(msg,color,BotonX,BotonY,Ancho,Alto,tamano="pequeno"):
    textoSuperficie, textoRect = objetotexto(msg,color,tamano)
    textoRect.center = (BotonX+(Ancho/2),BotonY+(Alto/2))
    pantalla.blit(textoSuperficie,textoRect)
# -----------------------------------------
def botones(texto,superficie,estado,Posicionamiento,tam,identidad = None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global  pausado
    global fin

    if Posicionamiento[0] + tam[0] > cursor[0] > tam[0] and Posicionamiento[1] + tam[1] > cursor[1] > tam[1] and Posicionamiento[1] + tam[1] < cursor[1] + tam[1]:
        #print (click)
        if click[0] == 1:
            if identidad == "comienzo":
                gameloop()
            elif identidad == "configuracion":
                opciones()
            elif identidad == "detalles":
                creditos()
            elif identidad == "salir":
                quit()
            elif identidad == "pausado":
                pausa()
            elif identidad == "resumir":
                pausado = True
            elif identidad == "guardar":
                pass
            elif identidad == "control":
                pass
            elif identidad == "retorno":
                pausado = True
                introduccion()
            elif identidad == "reinicio":
                fin = True
                gameloop()
            elif identidad == "menu":
                fin = True
                introduccion()

        boton = pygame.draw.rect(superficie,estado[1],(Posicionamiento[0],Posicionamiento[1],tam[0],tam[1]))
    else:
        boton = pygame.draw.rect(superficie,estado[0],(Posicionamiento[0],Posicionamiento[1],tam[0],tam[1]))

    TextoBoton(texto,negro,Posicionamiento[0],Posicionamiento[1],tam[0],tam[1])
    return boton
# -----------------------------------------
def dibujado(img,pos1,pos2):
    if direccion == "derecha":
        img = pygame.transform.flip(img,True,False)
    if direccion == "izquierda":
        img = img
    if direccion == "arriba":
        img = pygame.transform.rotate(img,90)
    if direccion == "abajo":
        img = pygame.transform.rotate(img,270)
    imagen = pantalla.blit(img,(pos1,pos2))
    return imagen
# -----------------------------------------
def pausa():
    global pausado
    while not pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pausado = false
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_c:
            #        pausado = False
            #    if event.key == pygame.K_r:
            #        pausado = False
            #        introduccion()

        pantalla.fill(blanco)
        mensaje("Juego en Pausa",verde,-100,tamano="grande")
        botones("Continuar",pantalla,ColorBoton1,Boton1,TamBoton,identidad="resumir")
        botones("Guardado",pantalla,ColorBoton2,Boton2,TamBoton,identidad="guardar")
        botones("Controles",pantalla,ColorBoton3,Boton3,TamBoton,identidad="control")
        botones("Retornar",pantalla,ColorBoton4,Boton4,TamBoton,identidad="retorno")
        #mensaje("presiona C para omitir, o presiona R para retornar",azul, tamano="pequeno")
        pygame.display.update()
        reloj.tick(15)
# -----------------------------------------
def puntos(marcador):
    mensaje = medianafuente.render("Puntos: " + str(marcador), True, verde)
    botones("pausa",pantalla,ColorBotonP,BotonPausa,BotonPtam,identidad="pausado")
    #mensaje2 = pequenafuente.render("Pausar Juego (p)", True, negro )
    pantalla.blit(mensaje,(0,0))
    #pantalla.blit(mensaje2,(650,0))
# -----------------------------------------
def fin_juego():
    global fin
    while not fin:
        pantalla.fill(blanco)
        mensaje("Has perdido",azul,-200,tamano="grande")
        mensaje("Quieres Continuar ?",verde,-100,tamano="mediano")
        #mensaje("Presiona C para Continuar o X para salir",negro,-30,tamano="mediano")
        mensaje("Tu puntuacion Obtenida fue: " + str(suma),rojo,tamano="pequeno")
        botones("Reintentar",pantalla,ColorBoton2,Boton2,TamBoton,identidad="reinicio")
        botones("Menu Principal",pantalla,ColorBoton3,Boton3,TamBoton,identidad="menu")
        botones("Salir",pantalla,ColorBoton4,Boton4,TamBoton,identidad="salir")
        pygame.display.update()
        for action in pygame.event.get():
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_c:
                    introduccion()
                    fin = False
                if action.key == pygame.K_x:
                    quit()
# -----------------------------------------
def serpiente(bloque,cuerpo):
    for dim in cuerpo[:-1]:
        dibujado(BocaCerrada,(cuerpo[-1][0]-5),(cuerpo[-1][1]-5))
        pygame.draw.rect(pantalla,verde,(dim[0],dim[1],bloque,bloque))
# -----------------------------------------
def dirManzana():
    dirXManz = round(random.randrange(0,ancho_pantalla - bloqueManzana))
    dirYManz = round(random.randrange(0,alto_pantalla - bloqueManzana))
    return dirXManz, dirYManz
# -----------------------------------------
def objetotexto(texto,color,tamano):
    if tamano == "pequeno":
        textoSuperficie = pequenafuente.render(texto,True,color)
    if tamano == "mediano":
        textoSuperficie = medianafuente.render(texto,True,color)
    if tamano == "grande":
        textoSuperficie = grandefuente.render(texto,True,color)
    return textoSuperficie, textoSuperficie.get_rect()
# -----------------------------------------
def mensaje(msg,color,desplazamientoY=0,tamano="pequeno"):
    textoSuperficie, textoRect = objetotexto(msg,color,tamano)
    textoRect.center = (ancho_pantalla/2),(alto_pantalla/2)+desplazamientoY
    pantalla.blit(textoSuperficie,textoRect)
# -----------------------------------------
def introduccion():
    """
        esta es la introduccion de nuestro juego
    """
    introJuego = True

    while introJuego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                introJuego = False
                quit()
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_s:
            #        gameloop()
            #        introJuego = False
            #    if event.key == pygame.K_p:
            #        opciones()
            #        introJuego = False
            #    if event.key == pygame.K_x:
            #        introJuego = False
            #        quit()

        pantalla.fill(blanco)
        mensaje("Bienvenido a Snake",verde,-100,tamano="grande")
        botones("Iniciar",pantalla,ColorBoton1,Boton1,TamBoton,identidad="comienzo")
        botones("Opciones",pantalla,ColorBoton2,Boton2,TamBoton,identidad="configuracion")
        botones("Creditos",pantalla,ColorBoton3,Boton3,TamBoton,identidad="detalles")
        botones("Salida",pantalla,ColorBoton4,Boton4,TamBoton,identidad="salir")
        #TextoBoton("Iniciar",negro,Boton1[0],Boton1[1],TamBoton[0],TamBoton[1])
        #TextoBoton("Opciones",negro,Boton2[0],Boton2[1],TamBoton[0],TamBoton[1])
        #TextoBoton("Creditos",negro,Boton3[0],Boton3[1],TamBoton[0],TamBoton[1])
        #TextoBoton("Salida",negro,Boton4[0],Boton4[1],TamBoton[0],TamBoton[1])
        #mensaje("presiona S para iniciar, o presiona P para opciones, X para salir",azul, tamano="pequeno")
        pygame.display.update()
        reloj.tick(15)
# -----------------------------------------
def opciones():
    """
        estas son las futuras opciones del juego
    """
    retroceso = True

    while retroceso:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                retroceso = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    introduccion()
                    retroceso = False
        pantalla.fill(blanco)
        mensaje("opciones del juego",verde,-100,tamano="grande")
        pygame.display.update()
        reloj.tick(15)
# -----------------------------------------
def gameloop():
    """
        este es el cuerpo de nuestro juego
    """
    salir = False
    global suma
    global direccion
    # serpiente
    # -----------------------------------------
    bloque = 20
    ladoX = ancho_pantalla/2
    ladoY = alto_pantalla/2
    velX = 0
    velY = 0
    longitud = 1
    cuerpo = []
    # -----------------------------------------

    dirXManz, dirYManz = dirManzana()

    while not salir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direccion = "derecha"
                    velX = -4
                    velY = 0
                if event.key == pygame.K_RIGHT:
                    direccion = "izquierda"
                    velX = 4
                    velY = 0
                if event.key == pygame.K_UP:
                    direccion = "arriba"
                    velY = -4
                    velX = 0
                if event.key == pygame.K_DOWN:
                    direccion = "abajo"
                    velY = 4
                    velX = 0
                if event.key == pygame.K_p:
                    pausa()
        # verificamos que la serpiente sale del rom
        if ladoX > ancho_pantalla or ladoX < 0 or ladoY > alto_pantalla or ladoY < 0:
            fin_juego()

        ladoX += velX
        ladoY += velY
        pantalla.fill(blanco)
        # funcion de crecimiento de la serpiente
        cabeza = []
        cabeza.append(ladoX)
        cabeza.append(ladoY)
        cuerpo.append(cabeza)
        serpiente(bloque,cuerpo)
        # verificacion del crecimiento de la serpiente
        if len(cuerpo) > longitud:
            del cuerpo[0]
        #mostranos la puntuacion del fin_juego
        puntos(longitud-1)

        pantalla.blit(ImagenManz,(dirXManz,dirYManz))
        #manzana = pygame.draw.rect(pantalla,rojo,(dirXManz,dirYManz,bloqueManzana,bloqueManzana))

        # verificacion de la serpiente mordiendose
        for segmento in cuerpo[:-1]:
            if segmento == cabeza:
                fin_juego()

        #Colision entre la serpiente y la manzana

        if ladoX == bloqueManzana and ladoX <= dirXManz + bloqueManzana or ladoX + bloque >= dirXManz and ladoX + bloque <= dirXManz + bloqueManzana :
            if ladoY >= dirYManz and ladoY <= dirYManz + bloqueManzana:
                dirXManz, dirYManz = dirManzana()
                longitud += 1
                suma = suma + 1
                dibujado(BocaAbierta,cuerpo[-1][0],cuerpo[-1][1])

        pygame.display.update()
        reloj.tick(60)
# -----------------------------------------
introduccion()
quit()
# -----------------------------------------
gameloop()

# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
import time
import mapa



pygame.mixer.pre_init(44100,16,2,1024)
pygame.init()



BLANCO = (255,255,255)
AMARILLO = (255,255,0)

tipoLetra = pygame.font.Font('Grandezza.ttf', 30)
tipoLetra2 = pygame.font.Font('Grandezza.ttf', 35)

imagenDeFondo = 'Noticia_TomJerry.jpg'



imagenGatoContento = 'gato.png'

imagenRatonContento = 'raton1.png'

imagenQueso = 'q.png'



visor = pygame.display.set_mode((800, 600))


def pausa():
   # Esta función hace que se espera hasta que se pulse una tecla
   esperar = True
   while esperar:
      for evento in pygame.event.get():
          if evento.type == KEYDOWN:
              esperar = False
  

def mostrarIntro():
   # Muestra la pantalla de inicio y espera
   fondo = pygame.image.load(imagenDeFondo).convert()
   visor.blit(fondo, (0,0))
   mensaje = 'Pulsa una tecla para comenzar'
   texto = tipoLetra.render(mensaje, True, AMARILLO)
  
   visor.blit(texto, (60,550,350,30))
   pygame.display.update()
   pausa()


pygame.mouse.set_visible(False)
mostrarIntro()
time.sleep(0.75)


# La clase Jugador implementa el sprite del jugador. En este ejemplo es algo
# muy sencillo, simplemente un gato que se mueve a izquierda, derecha,
# arriba y abajo con las teclas o, p, q y a.



class imagenRatonContento( pygame.sprite.Sprite ):

    def __init__( self, posX, posY ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load('raton1.png').convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
              
        # Aprovechando el constructor de la clase, situamos la posición inicial
        # del sprite en las coordenadas posX y posY        
        
        
        self.rect.topleft = (posX, posY)
               
        
         # dy y dx son las velocidades verticales del sprite. Inicialmente son 0.       
        
        self.dy = 0
        self.dx = 0
                
    def update(self):
                
        # Cuando se mueve el sprite se usa esta función. Pero ahora hay que ir con
        # cuidado. Si se mueve el spritey hay colisión con la pared, en realidad
        # no se debería poder mover. Así que necesitamos una manera de deshacer
        # el movimiento y que no se muestre realmente en pantalla. ¿Cómo hacerlo?
        # Lo que hacemos es almacenar en la variable pos la posición del sprite
        # antes de que se mueva, así para deshacer el movimiento sólo hay que
        # volver a colocar el sprite en donde indica pos.        
        
        
        
        
        self.pos = self.rect.topleft
       
        # Una vez hecho eso, ya podemos hacer la tentativa de mover el sprite.        
        
        
        self.rect.move_ip(self.dx,self.dy)
        
    def deshacer(self):
 
        # Ésta es la función en la que deshacemos el movimiento, si hace falta.
        # Como hemos dicho, ponemos el srpite donde estaba antes, en pos.        
        
        
        self.rect.topleft = self.pos



class imagenGatoContento( pygame.sprite.Sprite ):

    def __init__( self, posX, posY ):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load('gato.png').convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
              
        self.rect.topleft = (posX, posY)
               
        self.dy = 0
        self.dx = 0
                
    def update(self):
                
        self.pos = self.rect.topleft
       
        self.rect.move_ip(self.dx,self.dy)
        
    def deshacer(self):
 
        self.rect.topleft = self.pos



# Empezamos el programa de manera efectiva, por fin. Primero definimos la
# ventana de 800x600 en la que se va a desarrollar.


visor = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Ejemplo de Mapa')

# Ahora creamos el sprite del jugador en la posición (50,200)...


imagenRatonContento = imagenRatonContento(50,200)
imagenGatoContento = imagenGatoContento(50,500)

grupoimagenRatonContento = pygame.sprite.RenderUpdates( imagenRatonContento )
grupoimagenGatoContento = pygame.sprite.RenderUpdates( imagenGatoContento )

nivel = mapa.Mapa('mapa.txt')

# Como es habitual, creamos el reloj que controlará la velocidad de la animación.   

reloj = pygame.time.Clock()


# Empezamos el bucle de la animación del juego. Recuerda que cada ciclo de este
# bucle representa un fotograma de la animación del juego.




while True:
    
     # Ponemos el reloj a 60 fotogramas por segundo.   
    
    reloj.tick(60)
    
    # Miramos en la lista de eventos si se cierra la ventana o se pulsa la tecla
    # escape, en cuyo caso hay que terminar el programa.
    
    for evento in pygame.event.get():
        if evento.type == QUIT or (evento.type == KEYDOWN and evento.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    # En el plano del nivel hemos dejado una salida que deja salir de la pantalla.
    # Supuestamente esa sería la forma de cambiar de nivel. En el ejemplo que
    # estamos escribiendo, simplemente también se acaba el juego. Si se quisiera
    # hacer otra cosa, éste sería el lugar.
    
    if imagenGatoContento.rect.right > 800:
        pygame.quit()
        sys.exit()
    
    # Ha llegado el momento de mover el sprite. Para eso, primero miramos
    # la lista de teclas que se han pulsado...
    
    teclasPulsadas = pygame.key.get_pressed()
    
    # ... y según cuales sean éstas, hacemos el desplazamiento correspondiente
    # en la dirección adecuada modificando su velocidad.
    
    if teclasPulsadas[K_a]:
        imagenGatoContento.dx = -2
    elif teclasPulsadas[K_d]:
        imagenGatoContento.dx = 2
    else:
        imagenGatoContento.dx = 0
        
    if teclasPulsadas[K_w]:
        imagenGatoContento.dy = -2
    elif teclasPulsadas[K_x]:
        imagenGatoContento.dy = 2
    else:
        imagenGatoContento.dy = 0
    
    
    
    # Modificada su velocidad, ya se puede llamar a la función que cambia su
    # posición de acuerdo con ello...    
    
    
    
    
    if imagenRatonContento.rect.right > 800:
        pygame.quit()
        sys.exit()
    
 
    
    teclasPulsadas = pygame.key.get_pressed()
    

    
    if teclasPulsadas[K_LEFT]:
        imagenRatonContento.dx = -2
    elif teclasPulsadas[K_RIGHT]:
        imagenRatonContento.dx = 2
    else:
        imagenRatonContento.dx = 0
        
    if teclasPulsadas[K_UP]:
        imagenRatonContento.dy = -2
    elif teclasPulsadas[K_DOWN]:
        imagenRatonContento.dy = 2
    else:
        imagenRatonContento.dy = 0
    

    
    grupoimagenRatonContento.update()
    grupoimagenGatoContento.update()
  
    # ... pero ¡recuerda!: Si en la posición nueva tenemos colisión con la pared
    # el movimiento no es posible, así que hay que deshacer el movimiento...
    # Si utilizamos cualquier función de colisión normal de pygame, la colisión
    # se produce si coincide la imagen del jugador con la de la pieza de la pared.
    # Pero esto no nos vale; de los dibujos al borde de las imagenes que los
    # contienen hay un margen y entonces no nos podríamos acercar del todo a las
    # paredes como en la realidad. Esto no queda bien, claro.
    # Podemos solucionarlo de dos formas; haciendo que las imágenes llenen por
    # completo su tamaño, de forma que no queden márgenes (algo que no siempre
    # es posible) o usando la función spritecollide junto con la función
    # collide_mask. Si lees la documentación de Pygame verás que lo que se consigue
    # con esto es que sólo se usen las partes reales del dibujo del sprite para
    # detectar la colisión. ¡Justo lo que queremos!
    # En el ejemplo que estamos escribiendo nos basta con esto. Pero debes saber
    # que estas funciones son incluso más potentes; permiten usar máscaras
    # específicas para indicar qué partes del sprite cuentan para colisionar y qué
    # partes no. ¿Te imaginas un sprite de un pirata con un cuchillo en el que
    # éste reaccione sólo cuando se choque a la altura del cuchillo?     
    
    if pygame.sprite.spritecollide(imagenRatonContento, nivel.grupo, 0, pygame.sprite.collide_mask):		
		imagenRatonContento.deshacer()
		
    if pygame.sprite.spritecollide(imagenGatoContento, nivel.grupo, 0, pygame.sprite.collide_mask):
		imagenGatoContento.deshacer()    
        # Lo dicho. Como hay colisión, hay que deshacer el movimiento.
    
    
    for pum in pygame.sprite.groupcollide(grupoimagenRatonContento, nivel.quesos, 0, 1):
        pass   
  
    for pum in pygame.sprite.groupcollide(grupoimagenRatonContento, grupoimagenGatoContento, 1, 0):
		pass     

    # Ya todo está en orden. Simplemente hay que dibujar cada elemento en sus
    # nuevas posiciones. En primer lugar el nivel del juego (en este programa
    # no cambia, pero en general podríamos tener elementos móviles):    
    
    nivel.actualizar(visor)
    
    # Y luego el sprite del jugador.    
    
    grupoimagenRatonContento.draw(visor)
    grupoimagenGatoContento.draw(visor)
    
    # ¡Se acabó! Lo volcamos en pantalla y ya está el fotograma completado.    
    
    pygame.display.update()
   
        
  

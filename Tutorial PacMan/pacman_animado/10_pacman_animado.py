#----------------------------------------------
#  
#  Autor: Santiago Galvan Sanchez
#  e-mail: galvangalvan@gmail.com
#
#----------------------------------------------

import pygame
import sys, copy, random, os

#--- Inicio MiSprite -----------------------------------------------            
 
class MiSprite ( pygame.sprite.Sprite ):
    '''Todos los objetos que se representan en pantalla son sprites'''
    def __init__(self, fichero_imagen = None, pos_inicial = [0,0]):
        pygame.sprite.Sprite.__init__(self) 
        
        #Un sprite debe tener definida las propiedades "image" y "rect"
        #    Image representa la imagen a visualizar. Es de tipo "surface".
        #    Rect es un rectangulo que representa la zona de la pantalla que ocupara la imagen
        if not fichero_imagen is None:
            self.image = cargar_imagen(fichero_imagen)
            self.rect = self.image.get_rect()
            self.rect.topleft = pos_inicial
        
    def update (self):
        pygame.sprite.Sprite.update ( self )
        
#--- Fin MiSprite -----------------------------------------------            
           
#--- Inicio SpriteMovil --------------------------------------------  

class SpriteMovil ( MiSprite ):
    def __init__(self, fichero_imagen, pos_inicial, velocidad):
        MiSprite.__init__(self, fichero_imagen, pos_inicial) 
        self.rect.topleft = pos_inicial
        self.velocidad = velocidad
        
    def update (self):       
        #la funcion "copy" crea una copia del rectangulo  
        copia_rect = copy.copy(self.rect)
       
        self.rect.move_ip ( self.velocidad[0], self.velocidad[1]) 
       
        colisiones = pygame.sprite.spritecollide(self, sprites, False)
        for colision in colisiones:
            if colision != self:
                if hasattr ( colision, "infranqueable" ):
                    if colision.infranqueable:
                        self.velocidad[0]=0
                        self.velocidad[1]=0
                        self.rect = copia_rect
                        return     
            
        screen = pygame.display.get_surface () 
            
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocidad[1] = 0
        elif self.rect.bottom > screen.get_height():
            self.rect.bottom = screen.get_height()
            self.velocidad[1] = 0
            
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocidad[0] = 0
        elif self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
            self.velocidad[0] = 0
          
#--- Fin SpriteMovil -----------------------------------------------            

         
#--- Inicio Pacman -----------------------------------------------            
 
class Pacman ( SpriteMovil ):
    NUMERO_FOTOGRAMAS = 8
    
    def __init__(self, fichero_imagen, pos_inicial):
        SpriteMovil.__init__(self, fichero_imagen, pos_inicial, [0,0]) 
        self.vidas = 3
        self.puntos = 0
        
        self.__imagenArriba = {}
        self.__imagenAbajo = {}
        self.__imagenDerecha = {}
        self.__imagenIzquierda = {}
        
        for i in range(0, self.NUMERO_FOTOGRAMAS, 1):
            self.__imagenIzquierda[i] = cargar_imagen("pacman-izquierda" + str(i+1) + ".gif")
            self.__imagenDerecha[i] = cargar_imagen("pacman-derecha" + str(i+1) + ".gif")
            self.__imagenArriba[i] = cargar_imagen("pacman-arriba" + str(i+1) + ".gif")
            self.__imagenAbajo[i] = cargar_imagen("pacman-abajo" + str(i+1) + ".gif")
        
        self.__fotogramasActuales = self.__imagenDerecha
        self.__fotogramaActual = 1
        self.__tiempoCambioFotograma = pygame.time.get_ticks()

    def update (self):
        global eventos # explicitamente declaramos que "eventos" es una variable global
        v = 1
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.velocidad[0] = -v
                    self.velocidad[1] = 0
                elif event.key == pygame.K_RIGHT:
                    self.velocidad[0] = v
                    self.velocidad[1] = 0
                elif event.key == pygame.K_UP:
                    self.velocidad[1] = -v
                    self.velocidad[0] = 0
                elif event.key == pygame.K_DOWN:
                    self.velocidad[1] = v
                    self.velocidad[0] = 0
                elif event.key == pygame.K_SPACE:
                    pass #por ahora no hacemos nada

        SpriteMovil.update(self)
        
        #se cambia la imagen de pacman segun la direccion
        if self.velocidad[0] > 0:
            self.__fotogramasActuales = self.__imagenDerecha
        elif self.velocidad[0] < 0:
            self.__fotogramasActuales = self.__imagenIzquierda
        elif self.velocidad[1] > 0:
            self.__fotogramasActuales = self.__imagenAbajo
        elif self.velocidad[1] < 0:
            self.__fotogramasActuales = self.__imagenArriba        
       
        if pygame.time.get_ticks() - self.__tiempoCambioFotograma > 100:
            self.__fotogramaActual = (self.__fotogramaActual + 1) % self.NUMERO_FOTOGRAMAS 
            self.__tiempoCambioFotograma = pygame.time.get_ticks()

        self.image = self.__fotogramasActuales[self.__fotogramaActual]
        
        global sprites  
        #se obtiene todos los sprites con los que colisiona. El ultimo parametro indica que no queremos destruir automaticamente los sprites con los que colisiona  
        sprites_choque = pygame.sprite.spritecollide(self, sprites, False)
        for sprite in sprites_choque:
            if sprite != self:
                if hasattr ( sprite, "comestible" ): #comprobamos si el sprite tiene un atributo llamado "comestible"
                    if sprite.comestible:
                        if hasattr ( sprite, "puntos" ):
                            self.puntos += sprite.puntos
                        sprite.kill() #destruimos el sprite
        
#--- Fin Pacman -----------------------------------------------            


#--- Inicio fantasma -----------------------------------------------  

class Fantasma ( SpriteMovil ):
    def __init__(self, fichero_imagen, pos_inicial, velocidad):
        SpriteMovil.__init__(self, fichero_imagen, pos_inicial, velocidad) 


    def update (self):  
        #comprobamos si el fantasma ha capturado al pacman 
        global sprites
        sprites_choque = pygame.sprite.spritecollide(self, sprites, False)
        for sprite in sprites_choque:
            if hasattr(sprite, "vidas"):
                sprite.vidas -= 1
                if sprite.vidas <= 0:
                    sprite.kill()
                else:
                    sprite.rect.topleft = [0,0]  
        
        #su velocidad es 0 si ha colisionado con un objeto infranqueable   
        if self.velocidad[0] == 0 and self.velocidad[1] == 0:
            self.velocidad[0]= random.choice([-2, -1, 1 , 2])
            self.velocidad[1] = random.choice([-2, -1, 1 , 2])
        else:
            if self.rect.top <= 0:
                self.velocidad[1] = random.choice([1,2])
                self.velocidad[0]= random.choice([-2, -1, 1 , 2])
            elif self.rect.bottom >= pygame.display.get_surface().get_height():
                self.velocidad[1] = -random.choice([1,2])
                self.velocidad[0]= random.choice([-2, -1, 1 , 2])
            
            if self.rect.left <= 0:
                self.velocidad[0] = random.choice([1,2])
                self.velocidad[1]= random.choice([-2, -1, 1 , 2])
            elif sprite.rect.right >= pygame.display.get_surface().get_width():
                self.velocidad[0] = -random.choice([1,2])
                self.velocidad[1]= random.choice([-2, -1, 1 , 2])
        
        SpriteMovil.update (self)
      
        
#--- Fin fantasma -----------------------------------------------  
        
#--- Inicio Pared ---------------------------------------------

class Pared ( MiSprite ):
    def __init__(self, color, pos_inicial, dimension):
        MiSprite.__init__(self)
    
        self.image = pygame.Surface(dimension) #creamos una superficie de las dimensiones indicadas
        self.image.fill(color)
            
        self.rect = self.image.get_rect()
        self.rect.topleft = pos_inicial
        self.infranqueable = True

    
    def update(self):
        MiSprite.update(self)
  
#--- Fin Pared ---------------------------------------------    
  
class Marcador (MiSprite):
    def __init__(self, pacman):
        MiSprite.__init__(self)
        self.pacman = pacman
        self.font = pygame.font.SysFont("None", 20)
        self.rect = pygame.rect.Rect(0,0,0,0)

        
    def update(self):
        self.text = "vidas: %d, puntos: %d" % (self.pacman.vidas, self.pacman.puntos)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
        
        #situamos al marcador en la esquina inferior derecha
        self.rect.topleft = (pygame.display.get_surface().get_width() - self.rect.width, 
                     pygame.display.get_surface().get_height() - self.rect.height)
        
        MiSprite.update (self)

        
#--- funciones del modulo -------------------------------------

def ManejarEventos():
    global eventos # explicitamente declaramos que "eventos" es una variable global
    for event in eventos: 
        print event
        if event.type == pygame.QUIT: 
            sys.exit(0) #se termina el programa
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print event.pos

imagenes = {}
def cargar_imagen ( fichero_imagen ):
    global imagenes
    imagen = imagenes.get ( fichero_imagen, None )
    if imagen is None:
        imagen = pygame.image.load(os.path.join("imagenes",fichero_imagen)).convert()
        imagenes[fichero_imagen] = imagen
        imagen.set_colorkey (  imagen.get_at((0,0)) , pygame.RLEACCEL )
    return imagen

#--- Codigo de ejecucion inicial ------------------------------

if __name__ == "__main__":    
    #inicializamos pygame y la pantalla de juego
    pygame.init()
    
    #Indicamos la dimension de la pantlla de juego
    window = pygame.display.set_mode([300,400])
    pygame.display.set_caption("pacman")  

    #Inicializamos la pantalla con fondo negro
    screen = pygame.display.get_surface()
    screen.fill ([0,0,0])
    
    #creamos una copia de la pantalla para evitar su repintado completo cuando
    #    se redibujen los sprites
    background = screen.copy()

    #creamos los sprites
    sprites = pygame.sprite.RenderUpdates()
    
    pacman = Pacman("pacman.gif", [0,0])
    sprites.add ( pacman )
    
    sprite = Fantasma("fantasma.gif",[100,0], [1, 1] )
    sprites.add ( sprite )
    
    sprite = Pared ( [150,150,150], [72,72], [100,10] )
    sprites.add ( sprite )

    sprite = Pared ( [150,150,150], [172,172], [10,100] )
    sprites.add ( sprite )
 
   #items o premios
    sprite = MiSprite ("fruta.gif", [0, 100])
    sprite.comestible = True
    sprite.puntos = 10
    sprites.add ( sprite )

    sprite = MiSprite ("fruta.gif", [200, 150])
    sprite.comestible = True
    sprite.puntos = 10
    sprites.add ( sprite )
 
    sprite = MiSprite ("bola.gif", [130, 330])
    sprite.comestible = True
    sprite.puntos = 5
    sprites.add ( sprite )
       
    
    marcador = Marcador ( pacman )
    sprites.add ( marcador )


    #bucle de redibujado de los screens
    reloj = pygame.time.Clock() 
                
    while True: 
        eventos = pygame.event.get()
        ManejarEventos ()
        
        sprites.update ()
        sprites.clear (screen, background) 
        pygame.display.update (sprites.draw (screen))
        
        reloj.tick (40) #tiempo de espera entre frames
        
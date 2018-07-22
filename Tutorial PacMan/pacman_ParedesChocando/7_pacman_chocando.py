#----------------------------------------------
#  
#  Autor: Santiago Galvan Sanchez
#  e-mail: galvangalvan@gmail.com
#
#----------------------------------------------

import pygame
import sys, copy

#--- Inicio MiSprite -----------------------------------------------            
 
class MiSprite ( pygame.sprite.Sprite ):
    '''Todos los objetos que se representan en pantalla son sprites'''
    def __init__(self, fichero_imagen, pos_inicial, velocidad):
        pygame.sprite.Sprite.__init__(self) 
        
        #Un sprite debe tener definida las propiedades "image" y "rect"
        #    Image representa la imagen a visualizar. Es de tipo "surface".
        #    Rect es un rectangulo que representa la zona de la pantalla que ocupara la imagen
        self.image = pygame.image.load(fichero_imagen).convert()
        self.rect = self.image.get_rect()
        
        self.rect.topleft = pos_inicial
        self.velocidad = velocidad
    
    def update (self):
        '''Esta funcion es llamada repetidamente para hacer cualquier cambio
           en el sprite. Por ejemplo, para cambiar su posicion'''
        
        #la funcion "copy" crea una copia del rectangulo  
        copia_rect = copy.copy(self.rect)
       
        self.rect.move_ip ( self.velocidad[0], self.velocidad[1]) 
       
        colisiones = pygame.sprite.spritecollide(self, sprites, False)
        for colision in colisiones:
            if colision != self:
                if hasattr ( colision, "infranqueable" ):
                    if colision.infranqueable:
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
        
#--- Fin MiSprite -----------------------------------------------            
           
         
#--- Inicio Pacman -----------------------------------------------            
 
class Pacman ( MiSprite ):
    def __init__(self, fichero_imagen, pos_inicial):
        MiSprite.__init__(self, fichero_imagen, pos_inicial, [0,0]) 

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

        MiSprite.update(self)
        
        global sprites  
        #se obtiene todos los sprites con los que colisiona. El ultimo parametro indica que no queremos destruir automaticamente los sprites con los que colisiona  
        sprites_choque = pygame.sprite.spritecollide(self, sprites, False)
        for sprite in sprites_choque:
            if sprite != self:
                if hasattr ( sprite, "comestible" ): #comprobamos si el sprite tiene un atributo llamado "comestible"
                    if sprite.comestible:
                        sprite.kill() #destruimos el sprite
        
      
  
#--- Fin Pacman -----------------------------------------------            

#--- Inicio Pared ---------------------------------------------

class Pared ( pygame.sprite.Sprite ):
    def __init__(self, color, pos_inicial, dimension):
        pygame.sprite.Sprite.__init__(self)
    
        self.image = pygame.Surface(dimension) #creamos una superficie de las dimensiones indicadas
        self.image.fill(color)
            
        self.rect = self.image.get_rect()
        self.rect.topleft = pos_inicial
        self.infranqueable = True

    
    def update(self):
        pygame.sprite.Sprite.update(self)
  
#--- Fin Pared ---------------------------------------------    
  
#--- funciones del modulo -------------------------------------

def ManejarEventos():
    global eventos # explicitamente declaramos que "eventos" es una variable global
    for event in eventos: 
        print event
        if event.type == pygame.QUIT: 
            sys.exit(0) #se termina el programa
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print event.pos



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
    
    sprite = Pacman("pacman.gif", [0,0])
    sprites.add ( sprite )
    
    sprite = MiSprite("fantasma.gif",[100,0], [1, 1] )
    sprites.add ( sprite )
    
    sprite = MiSprite ("fruta.gif", [0, 100], [0,0])
    sprite.comestible = True
    sprites.add ( sprite )
 
    sprite = MiSprite ("bola.gif", [100, 100], [0,0] )
    sprite.comestible = True
    sprites.add ( sprite )
    
    sprite = Pared ( [150,150,150], [72,72], [100,10] )
    sprites.add ( sprite )

    sprite = Pared ( [150,150,150], [172,172], [10,100] )
    sprites.add ( sprite )

    #bucle de redibujado de los screens
    reloj = pygame.time.Clock() 
                
    while True: 
        eventos = pygame.event.get()
        ManejarEventos ()
        
        sprites.update ()
        sprites.clear (screen, background) 
        pygame.display.update (sprites.draw (screen))
        
        reloj.tick (60) #tiempo de espera entre frames
        
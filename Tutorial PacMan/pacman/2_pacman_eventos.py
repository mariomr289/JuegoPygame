import pygame
import sys
 
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
        
        #la funcion move_ip desplaza el rectangulo que ocupa el sprite
        self.rect.move_ip ( self.velocidad[0], self.velocidad[1]) 
  

def ManejarEventos(): 
    global eventos # explicitamente declaramos que "eventos" es una variable global
    for event in eventos: 
        print event
        if event.type == pygame.QUIT: 
            sys.exit(0) #se termina el programa
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print event.pos


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
    sprite = MiSprite("pacman.gif", [0,0], [1,1])
    sprites.add ( sprite )
    sprite = MiSprite("fantasma.gif",[100,0], [1, 1] )
    sprites.add ( sprite )
    sprite = MiSprite ("fruta.gif", [0, 100], [0,0])
    sprites.add ( sprite )
    sprite = MiSprite ("bola.gif", [100, 100], [0,0] )
    sprites.add ( sprite )

    #bucle de redibujado de los screens
    reloj = pygame.time.Clock() 
                
    while True: 
        eventos = pygame.event.get() #capturamos todos los eventos de la cola. Estos eventos se eliminan de la cola.
        ManejarEventos ()
        
        sprites.update ()
        sprites.clear (screen, background) 
        pygame.display.update (sprites.draw (screen))
        
        reloj.tick (60) #tiempo de espera entre frames
        
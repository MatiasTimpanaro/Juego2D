import pygame
import constantes

class Personaje():
   
    #definimos el constructor (donde va a estar en pantalla se define con "x" e "y" y que imagen va a ser)
    def __init__(self, x, y, animaciones):
       
       
        self.animaciones = animaciones
        #imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0
        self.image = animaciones[self.frame_index]
        #cuanto ms han concurrido desde que se inicio pygame
        self.update_time = pygame.time.get_ticks()

        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE) #inicia en 0, 0 y es de tamaño 10, 10 QUE ESTA EN LAS CONSTANTES
        self.forma.center = (x,y) #con esto, cuando inicie se movera al centro de donde lo creamos
        self.flip = False #para que se voltee al moverse
    
    #funciona para que se vaya actualizando la immagen de animacion y para que si no se aprieta nada no se mueva
    def update (self, en_movimiento):
        
        cooldow_animacion = constantes.VELOCIDAD_ANIMACION
        if en_movimiento:
            if pygame.time.get_ticks() - self.update_time >= cooldow_animacion:
                self.frame_index += 1
                self.update_time = pygame.time.get_ticks()
                if self.frame_index >= len(self.animaciones):
                    self.frame_index = 0
        else:
            self.frame_index = 0
        self.image = self.animaciones[self.frame_index]


    def dibujar (self, interfaz):
        
         #para dar vuelta la imagen, el primer False es para eje x y el 2do para el eje y       
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)    

        #mostramos el personaje (forma)
        interfaz.blit(imagen_flip, self.forma)
        
            #esto dibuja en la "ventana", algo fucsia (CONSTANTE), que es la forma (self.forma)        
            #esta comentada para que no moleste
        #pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma, 1)
    
    #funcion de movimiento
    def movimiento (self, delta_x, delta_y):
        
        #para que mira para ambos lados
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
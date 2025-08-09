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

    #funcion de dibujo del personaje, flip 
    def dibujar(self, interfaz):
        imagen = self.image
        if self.flip:
            imagen = pygame.transform.flip(self.image, True, False)
        rect_imagen = imagen.get_rect()

        if hasattr(self, "tipo_animacion") and self.tipo_animacion == "atacarArco":
            if self.flip:
                rect_imagen.width += constantes.EXPANSION
                rect_imagen.right = self.forma.right
            else:
                rect_imagen.width += constantes.EXPANSION
                rect_imagen.left = self.forma.left
        else:
            if self.flip:
                rect_imagen.right = self.forma.right
            else:
                rect_imagen.left = self.forma.left

        rect_imagen.top = self.forma.top

        interfaz.blit(imagen, rect_imagen)

       #mostrar rectangulo del personaje
        pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, rect_imagen, 1)

    #funcion de movimiento
    def movimiento(self, delta_x, delta_y):
        flip_anterior = self.flip

        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False

        # Compensar el salto al cambiar el flip
        if self.flip != flip_anterior:
            constantes.EXPANSION if hasattr(self, "tipo_animacion") and self.tipo_animacion == "atacarArco" else 0
            if self.flip:
                # De derecha a izquierda: mantener el borde derecho fijo
                self.forma.right = self.forma.left + self.forma.width + constantes.EXPANSION
            else:
                # De izquierda a derecha: mantener el borde izquierdo fijo
                self.forma.left = self.forma.right - self.forma.width - constantes.EXPANSION

        self.forma.x += delta_x
        self.forma.y += delta_y
import pygame
import constantes

class casilla_arma ():
    def __init__(self, x, y, cuad_arma):
        self.image = cuad_arma #imagen del cuadrado
        #self.forma = self.cuad_arma.get #El get.rect() le da un rectangulo a la imagen del arma
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_CUA_HUD, constantes.ALTO_CUA_HUD) #inicia en 0, 0 y es de tamaño 10, 10 QUE ESTA EN LAS CONSTANTES
        self.forma.center = (x,y) #con esto, cuando inicie se movera al centro de donde lo creamos

    def dibujar (self, interfaz):
        interfaz.blit (self.image, self.forma)
import pygame

class weapon():
    def __init__(self, image):
        self.imagen_original = image #imagen del arma
        self.angulo = 0 #angulo que va a apuntar el arma
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect() #El get.rect() le da un rectangulo a la imagen del arma

    def update (self, personaje):
        self.forma.center = personaje.forma.center

    def dibujar (self, interfaz):
        interfaz.blit (self.imagen, self.forma)
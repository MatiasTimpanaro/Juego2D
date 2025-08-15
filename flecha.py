import math
import pygame
import constantes

#clase que hace la flecha
class Flecha:
    def __init__(self, x, y, objetivo, imagen):
        self.x = x
        self.y = y
        self.image_original = imagen
        dx = objetivo[0] - x
        dy = objetivo[1] - y
        self.angle = math.atan2(dy, dx)
        self.vx = math.cos(self.angle) * 12
        self.vy = math.sin(self.angle) * 12
        self.image = pygame.transform.rotate(self.image_original, -math.degrees(self.angle))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def fuera_de_pantalla(self):
        return (self.x < 0 or self.x > constantes.WIDTH or
                self.y < 0 or self.y > constantes.HEIGHT)

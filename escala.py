import pygame

def escalar_img (image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image,(w*scale, h*scale))
    return nueva_imagen
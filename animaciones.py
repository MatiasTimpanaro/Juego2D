import pygame
import constantes
from escala import escalar_img

#esta es la clase que da animaciones al personaje
class AnimacionesPersonaje:
    def __init__(self):
        self.caminar = []
        self.atacar = []
        self.arrow = []
        # Animación de caminar
        for i in range(8):
            img = pygame.image.load(f"assets/images/characters/Characters(100x100)/Soldier/Soldier/SoldierWalkDivide/soldier-{i}.png")
            img = escalar_img(img, constantes.ESCALA_PERSONAJE)
            self.caminar.append(img)
        # Animación de atacar con arco
        for i in range(9):
            img_at_bow = pygame.image.load(f"assets/images/characters/Characters(100x100)/Soldier/Soldier/SoldierAttackBow/soldier_at_bow_{i}.png")
            img_at_bow = escalar_img(img_at_bow, constantes.ESCALA_PERSONAJE)
            self.atacar.append(img_at_bow)
       
        # Animacion de la flecha
        img_arrow = pygame.image.load("assets/images/arrow(Projectile)/Arrow01.png")
        img_arrow = escalar_img(img_arrow, constantes.ESCALA_ARROW)
        self.arrow.append(img_arrow)
                        

#llamar a la animacion correspondiente
    def get_animacion(self, tipo):
         match tipo:
            case "caminar":
                return self.caminar
            case "atacarArco":
                return self.atacar
            case "arrow":
                 return self.arrow
            case _:
                return self.caminar  # Por defecto
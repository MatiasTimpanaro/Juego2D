import pygame
import constantes
from escala import escalar_img

#esta es la clase que da animaciones al personaje
class AnimacionesPersonaje:
    def __init__(self):
        self.caminar = []
        self.atacar = []
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
            

#llamar a la animacion correspondiente
    def get_animacion(self, tipo):
        if tipo == "caminar":
            return self.caminar
        elif tipo == "atacarArco":
            return self.atacar
        else:
            return self.caminar  # Por defecto
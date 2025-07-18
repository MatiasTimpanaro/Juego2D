import pygame
import constantes
from escala import escalar_img
from personaje import Personaje
from weapons import weapon
from hud import casilla_arma
  
   #inicilizar pygame
pygame.init() 

#crear la ventana
ventana = pygame.display.set_mode((constantes.WIDTH, constantes.HEIGHT))
    #nombre de la ventana
pygame.display.set_caption("Juego 2D")

#Importar imagenes
    #imagen, animacion y escala del personaje
animaciones = []
for i in range (8):
    img = pygame.image.load(f"assets\images\characters\Characters(100x100)\Soldier\Soldier\SoldierWalkDivide\soldier-{i}.png")
    img = escalar_img(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)

    #HUD (seleccion arma)
imagen_selec_arma = pygame.image.load("assets\\images\\Recuadros\\recuadro_arma_1.png")
imagen_selec_arma = escalar_img(imagen_selec_arma, constantes.ESCALA_CUAD_ARMA)
cuad_arma = casilla_arma(680, 500, imagen_selec_arma)


    #Arma / // // // seguir aca 
imagen_arco = pygame.image.load(f"assets\images\characters\Characters(100x100)\Soldier\Soldier\SoldierWalkDivide\soldier-{i}.png")

#creamos un objeto (en este caso, personaje)
jugador = Personaje(50,50, animaciones)

#crear un arma de la clase weapons / /// // ¡SEGUIR ACA!
arco = weapon(imagen_arco) 


    #definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

 #controlar el Frame Rate
reloj = pygame.time.Clock()

    #crear el loop para que permanezca abierta la ventana
run = True

while run:
   
    #que vaya a 60 FPS (constante)
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_FONDO)
    #Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD
    
    #mover al jugador
    jugador.movimiento(delta_x, delta_y)
    
    #animar el personaje y hacer que si no se presiona nada, no se mueva (se hacen con los delta x/y)
    en_movimiento = delta_x != 0 or delta_y != 0
    jugador.update(en_movimiento)
    
    #dibujamos el personaje
    jugador.dibujar(ventana)

    #dibujamos el cuadrado de seleccion de arma
    cuad_arma.dibujar(ventana)
    
    #los eventos son los comandos (teclas apretada/clics)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         run = False   
        
        #esto es el evento de aprentar una tecla
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_a:
                mover_izquierda = True
           if event.key == pygame.K_s:
                mover_abajo = True
           if event.key == pygame.K_d:
                mover_derecha = True
           if event.key == pygame.K_w:
                mover_arriba = True
        
        #esto es el evento de soltar una tecla

        if event.type == pygame.KEYUP:
           if event.key == pygame.K_a:
                mover_izquierda = False
           if event.key == pygame.K_s:
                mover_abajo = False
           if event.key == pygame.K_d:
                mover_derecha = False
           if event.key == pygame.K_w:
                mover_arriba = False

    #esto actualiza la pantalla constantemente para que se vayan mostrando los cambios
    pygame.display.update()

#esto cierra el juego 
pygame.quit()   
        



import pygame
import constantes
from escala import escalar_img
from personaje import Personaje
from weapons import weapon
from hud import casilla_arma
from animaciones import AnimacionesPersonaje
from flecha import Flecha
  
   #inicilizar pygame

pygame.init()
ventana = pygame.display.set_mode((constantes.WIDTH, constantes.HEIGHT))
pygame.display.set_caption("Monsters")

# Cargar la imagen del fondo
background_image = pygame.image.load("assets\\images\\fondos\\fondo1.jpg")

# Ajustar la imagen al tamaño de la pantalla (opcional)
background_image = pygame.transform.scale(background_image, (constantes.WIDTH, constantes.HEIGHT))

animaciones_personaje = AnimacionesPersonaje()
animaciones = animaciones_personaje.get_animacion("caminar")

imagen_selec_arma = pygame.image.load("assets\\images\\Recuadros\\recuadro_arma_1.png")
imagen_selec_arma = escalar_img(imagen_selec_arma, constantes.ESCALA_CUAD_ARMA)
cuad_arma = casilla_arma(680, 500, imagen_selec_arma)

jugador = Personaje(50, 50, animaciones)
arrow = animaciones_personaje.get_animacion("arrow")

mover_arriba = mover_abajo = mover_izquierda = mover_derecha = False
clic_izquiero = False

flechas = []
ultimo_disparo = 0
cooldown_disparo = 500  # milisegundos entre disparos

reloj = pygame.time.Clock()
run = True

while run:
    reloj.tick(constantes.FPS)
   # ventana.fill(constantes.COLOR_FONDO)

    # Dibujar el fondo
    ventana.blit(background_image, (0, 0))


    delta_x = 0
    delta_y = 0

    if mover_derecha:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo:
        delta_y = constantes.VELOCIDAD

    jugador.movimiento(delta_x, delta_y)
    posic_X = jugador.forma.centerx
    posic_Y = jugador.forma.centery

    # Actualizar animaciones
    en_movimiento = delta_x != 0 or delta_y != 0 or clic_izquiero
    jugador.update(en_movimiento)

    # Disparo automático sincronizado con animación
    if clic_izquiero:
        tiempo_actual = pygame.time.get_ticks()
        # Verificamos cooldown
        if tiempo_actual - ultimo_disparo >= cooldown_disparo:
            # Disparo sincronizado en frame 7 (ajustar según animación real)
            if jugador.frame_index == 7:
                mouse_pos = pygame.mouse.get_pos()
                # Offset según dirección
                offset_x = 30 if not jugador.flip else -30
                offset_y = 30
                spawn_x = posic_X + offset_x
                spawn_y = posic_Y + offset_y
                flechas.append(Flecha(spawn_x, spawn_y, mouse_pos, arrow[0]))
                ultimo_disparo = tiempo_actual

    # Dibujar jugador y HUD
    jugador.dibujar(ventana)
    cuad_arma.dibujar(ventana)

   
    # Actualizar y dibujar flechas
    for f in flechas[:]:
        f.update()
        f.draw(ventana)
        if f.fuera_de_pantalla():
            flechas.remove(f)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clic_izquiero = True
            jugador.animaciones = animaciones_personaje.get_animacion("atacarArco")
            jugador.frame_index = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_s:
                mover_abajo = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clic_izquiero = False
            jugador.animaciones = animaciones_personaje.get_animacion("caminar")

    pygame.display.update()

pygame.quit()


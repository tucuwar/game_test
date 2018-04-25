# -*- coding: utf-8 -*-
# http://programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=es#section_5
#  

# Importar e inicializar Pygame
# Importa  la libraria de funciones llamada 'pygame'
import pygame


# Definir algunos colores
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

PI = 3.141592653

# Inicializa el motor de juegos
pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
# Establecer el título de la ventana
pygame.display.set_caption("Juego Mortal")

# Establecer el bucle principal del programa
# Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False
 
# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
# -------- Bucle Principal del Programa -----------
while not hecho:

    #

    # ----- EVENTOS DE PROCESAMIENTO ----------------------------------------
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Esto que indica que hemos acabado y sale de este bucle
            print("El usuario solicitó salir.")
        elif evento.type == pygame.KEYDOWN:
            print("El usuario presionó una tecla.")
        elif evento.type == pygame.KEYUP:
            print("El usuario soltó una tecla.")
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print("El usuario presionó un botón del ratón")


    ### maneja todos las pulsaciones del teclado, los clicks del ratón
    ### y algunos otros tipos de eventos. 
    ### añadir código que maneje las entradas del teclado y ratón.

    # -------FIN EVENTOS DE PROCESAMIENTO -----------------------------------
 
 
    # ------INICIO LOGICA DEL JUEGO--------------------------------
    ### cuándo disparar las balas y el cómo se mueven los objetos
        
    # ------FIN LOGICA DEL JUEGO-----------------------------------
 
 
    # ------INICIO CÓDIGO DE DIBUJO--------------------------------
    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(BLANCO)
     
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
    #pygame.rect.draw(pantalla, VERDE, [50,50,100,100])
 
    # ------FIN CÓDIGO DE DIBUJO-----------------------------------
    
    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()


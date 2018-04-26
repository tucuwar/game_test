# -*- coding: utf-8 -*-
# http://programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=es#section_5
#  

# Importar e inicializar Pygame
# Importa  la libraria de funciones llamada 'pygame'
import pygame
import math
from math import pi


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

# Establecemos las dimensiones de la pantalla [ancho,altura]
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

    # Draw on the screen a VERDE line from (0,0) to (50.75) 
    # 5 pixels wide.
    #pygame.draw.line(pantalla, VERDE, [0, 0], [50,30], 20)

    # Dibuja sobre la pantalla varias líneas desde (0, 10) hasta (100, 110)
    # de 5 píxeles de grosor usando un bucle for
    #for desplazar_y in range(0, 100, 10):
    #    pygame.draw.line(pantalla,ROJO, [0, 10 + desplazar_y], [100, 110 + desplazar_y], 5)
    #for desplazar_x in range(100, 200, 10):
    #    pygame.draw.line(pantalla,AZUL, [105, 10 + desplazar_x], [200, -90 + desplazar_x], 5)
    

    for desplazar_y in range(0, 100, 1):
        pygame.draw.line(pantalla,ROJO, [0, 130 + desplazar_y], [150, 0 + desplazar_y], 5)
    for desplazar_x in range(0, 100, 1):
        pygame.draw.line(pantalla,AZUL, [150, 0 + desplazar_x], [300, 130 + desplazar_x], 5)

    # Draw a rectangle outline
    pygame.draw.rect(pantalla, NEGRO, [0, 210, 300, 100], 5)
    # Draw a solid rectangle
    pygame.draw.rect(pantalla, AZUL, [130, 260, 50, 50])

    # Draw on the screen a VERDE line from (0,0) to (50.75) 
    # 5 pixels wide.
    #pygame.draw.lines(pantalla, NEGRO, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    
    # Draw on the screen a VERDE line from (0,0) to (50.75) 
    # 5 pixels wide.
    #pygame.draw.aaline(pantalla, VERDE, [0, 50],[50, 80], True)

    
     
    
    
     
    # Draw an ellipse outline, using a rectangle as the outside boundaries
    #pygame.draw.ellipse(pantalla, ROJO, [225, 10, 50, 20], 2) 

    # Draw an solid ellipse, using a rectangle as the outside boundaries
    #pygame.draw.ellipse(pantalla, ROJO, [300, 10, 50, 20]) 
 
    # This draws a triangle using the polygon command
    #pygame.draw.polygon(pantalla, NEGRO, [[100, 100], [0, 200], [200, 200]], 5)
  
    # Draw an arc as part of an ellipse. 
    # Use radians to determine what angle to draw.
    #pygame.draw.arc(pantalla, NEGRO,[210, 75, 150, 125], 0, PI/2, 2)
    #pygame.draw.arc(pantalla, VERDE,[210, 75, 150, 125], PI/2, PI, 2)
    #pygame.draw.arc(pantalla, AZUL, [210, 75, 150, 125], PI,3*PI/2, 2)
    #pygame.draw.arc(pantalla, ROJO,  [210, 75, 150, 125], 3*PI/2, 2*PI, 2)
    
    # Draw a circle
    #pygame.draw.circle(pantalla, AZUL, [60, 250], 40)
     
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
    
    # ------FIN CÓDIGO DE DIBUJO-----------------------------------
    
    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()


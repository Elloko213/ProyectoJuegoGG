import pygame
import sys
import time

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ancho = 900
alto = 900
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Rectángulo Cambiante")

# Configurar colores
negro = pygame.Color("black")
blanco = pygame.Color("white")
amarillo = pygame.Color("yellow")

# Configurar dimensiones y posición del rectángulo
ancho_rectangulo = 100
alto_rectangulo = 100
posicion_x_rectangulo = 0
posicion_y_rectangulo = 0

# Configurar velocidad del rectángulo
velocidad_rectangulo = 0.5

# Configurar dimensiones y posición del bloque
posicion_x_bloque1 = 600
posicion_y_bloque1 = 0
ancho_bloque1 = 300
alto_bloque1 = 300

posicion_x_bloque2 = 0
posicion_y_bloque2 = 300
ancho_bloque2 = 300
alto_bloque2 = 600

posicion_x_bloque3 = 300
posicion_y_bloque3 = 600
ancho_bloque3 = 300
alto_bloque3 = 300

# Configurar dimensiones y posición del círculo
posicion_x_circulo = 800
posicion_y_circulo = 800
radio_circulo = 50

# Configurar tiempo límite
tiempo_limite = 30
tiempo_inicio = time.time()

#imagen del personaje
personaje_imagen = pygame.image.load("./assets/cat2.png")
personaje_imagen = pygame.transform.scale(personaje_imagen, (ancho_rectangulo, alto_rectangulo))
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    # Movimiento del rectángulo
    if teclas[pygame.K_UP]:
        # Verificar colisión con los bloques antes de mover hacia arriba
        if not (posicion_x_rectangulo < posicion_x_bloque1 + ancho_bloque1 and
                posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque1 and
                posicion_y_rectangulo - velocidad_rectangulo < posicion_y_bloque1 + alto_bloque1 and
                posicion_y_rectangulo - velocidad_rectangulo + alto_rectangulo > posicion_y_bloque1) and \
                not (posicion_x_rectangulo < posicion_x_bloque2 + ancho_bloque2 and
                     posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque2 and
                     posicion_y_rectangulo - velocidad_rectangulo < posicion_y_bloque2 + alto_bloque2 and
                     posicion_y_rectangulo - velocidad_rectangulo + alto_rectangulo > posicion_y_bloque2) and \
                not (posicion_x_rectangulo < posicion_x_bloque3 + ancho_bloque3 and
                     posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque3 and
                     posicion_y_rectangulo - velocidad_rectangulo < posicion_y_bloque3 + alto_bloque3 and
                     posicion_y_rectangulo - velocidad_rectangulo + alto_rectangulo > posicion_y_bloque3):
            posicion_y_rectangulo = max(posicion_y_rectangulo - velocidad_rectangulo, 0)
    if teclas[pygame.K_DOWN]:
        # Verificar colisión con los bloques antes de mover hacia abajo
        if not (posicion_x_rectangulo < posicion_x_bloque1 + ancho_bloque1 and
                posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque1 and
                posicion_y_rectangulo + velocidad_rectangulo < posicion_y_bloque1 + alto_bloque1 and
                posicion_y_rectangulo + velocidad_rectangulo + alto_rectangulo > posicion_y_bloque1) and \
                not (posicion_x_rectangulo < posicion_x_bloque2 + ancho_bloque2 and
                     posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque2 and
                     posicion_y_rectangulo + velocidad_rectangulo < posicion_y_bloque2 + alto_bloque2 and
                     posicion_y_rectangulo + velocidad_rectangulo + alto_rectangulo > posicion_y_bloque2) and \
                not (posicion_x_rectangulo < posicion_x_bloque3 + ancho_bloque3 and
                     posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque3 and
                     posicion_y_rectangulo + velocidad_rectangulo < posicion_y_bloque3 + alto_bloque3 and
                     posicion_y_rectangulo + velocidad_rectangulo + alto_rectangulo > posicion_y_bloque3):
            posicion_y_rectangulo = min(posicion_y_rectangulo + velocidad_rectangulo, alto - alto_rectangulo)
    if teclas[pygame.K_LEFT]:
        # Verificar colisión con los bloques antes de mover hacia la izquierda
        if not (posicion_x_rectangulo - velocidad_rectangulo < posicion_x_bloque1 + ancho_bloque1 and
                posicion_x_rectangulo - velocidad_rectangulo + ancho_rectangulo > posicion_x_bloque1 and
                posicion_y_rectangulo < posicion_y_bloque1 + alto_bloque1 and
                posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque1) and \
                not (posicion_x_rectangulo - velocidad_rectangulo < posicion_x_bloque2 + ancho_bloque2 and
                     posicion_x_rectangulo - velocidad_rectangulo + ancho_rectangulo > posicion_x_bloque2 and
                     posicion_y_rectangulo < posicion_y_bloque2 + alto_bloque2 and
                     posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque2) and \
                not (posicion_x_rectangulo - velocidad_rectangulo < posicion_x_bloque3 + ancho_bloque3 and
                     posicion_x_rectangulo - velocidad_rectangulo + ancho_rectangulo > posicion_x_bloque3 and
                     posicion_y_rectangulo < posicion_y_bloque3 + alto_bloque3 and
                     posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque3):
            posicion_x_rectangulo = max(posicion_x_rectangulo - velocidad_rectangulo, 0)
    if teclas[pygame.K_RIGHT]:
        # Verificar colisión con los bloques antes de mover hacia la derecha
        if not (posicion_x_rectangulo + velocidad_rectangulo < posicion_x_bloque1 + ancho_bloque1 and
                posicion_x_rectangulo + velocidad_rectangulo + ancho_rectangulo > posicion_x_bloque1 and
                posicion_y_rectangulo < posicion_y_bloque1 + alto_bloque1 and
                posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque1) and \
                not (posicion_x_rectangulo + velocidad_rectangulo < posicion_x_bloque2 + ancho_bloque2 and
                     posicion_x_rectangulo + velocidad_rectangulo + ancho_rectangulo > posicion_x_bloque2 and
                     posicion_y_rectangulo < posicion_y_bloque2 + alto_bloque2 and
                     posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque2) and \
                not (posicion_x_rectangulo + velocidad_rectangulo < posicion_x_bloque3 + ancho_bloque3 and
                     posicion_x_rectangulo + velocidad_rectangulo + ancho_rectangulo > posicion_x_bloque3 and
                     posicion_y_rectangulo < posicion_y_bloque3 + alto_bloque3 and
                     posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque3):
            posicion_x_rectangulo = min(posicion_x_rectangulo + velocidad_rectangulo, ancho - ancho_rectangulo)

    # Colisión del rectángulo con el bloque y el círculo
    if (posicion_x_rectangulo < posicion_x_bloque1 + ancho_bloque1 and
            posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque1 and
            posicion_y_rectangulo < posicion_y_bloque1 + alto_bloque1 and
            posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque1):
        posicion_x_rectangulo = ancho  # Mover el rectángulo fuera de la ventana para terminar el programa

    if (posicion_x_rectangulo < posicion_x_circulo + radio_circulo and
            posicion_x_rectangulo + ancho_rectangulo > posicion_x_circulo - radio_circulo and
            posicion_y_rectangulo < posicion_y_circulo + radio_circulo and
            posicion_y_rectangulo + alto_rectangulo > posicion_y_circulo - radio_circulo):
        ejecutando = False  # Terminar el programa

    # Verificar el tiempo transcurrido
    tiempo_actual = time.time()
    tiempo_transcurrido = int(tiempo_actual - tiempo_inicio)
    tiempo_restante = tiempo_limite - tiempo_transcurrido

    if tiempo_restante <= 0:
        ejecutando = False  # Terminar el programa

    ventana.fill(blanco)
    pygame.draw.rect(ventana, negro, (posicion_x_rectangulo, posicion_y_rectangulo, ancho_rectangulo, alto_rectangulo))
    pygame.draw.rect(ventana, negro, (posicion_x_bloque1, posicion_y_bloque1, ancho_bloque1, alto_bloque1))
    pygame.draw.rect(ventana, negro, (posicion_x_bloque2, posicion_y_bloque2, ancho_bloque2, alto_bloque2))
    pygame.draw.rect(ventana, negro, (posicion_x_bloque3, posicion_y_bloque3, ancho_bloque3, alto_bloque3))
    pygame.draw.circle(ventana, amarillo, (posicion_x_circulo, posicion_y_circulo), radio_circulo)
    

    # Mostrar tiempo restante en la ventana
    fuente = pygame.font.Font(None, 36)
    mensaje_tiempo = fuente.render("Tiempo restante: " + str(tiempo_restante) + " segundos", True, negro)
    ventana.blit(mensaje_tiempo, (10, 10))

    pygame.display.flip()

# Mostrar mensaje de resultado
    ventana.fill(blanco)
if tiempo_restante <= 0:
    mensaje_perdiste = fuente.render("¡Perdiste el juego!", True, negro)
    ventana.blit(mensaje_perdiste, (ancho // 2 - mensaje_perdiste.get_width() // 2, alto // 2 - mensaje_perdiste.get_height() // 2))
else:
    mensaje_ganaste = fuente.render("¡Has ganado!", True, negro)
    ventana.blit(mensaje_ganaste, (ancho // 2 - mensaje_ganaste.get_width() // 2, alto // 2 - mensaje_ganaste.get_height() // 2))
ventana.blit(personaje_imagen, (posicion_x_rectangulo, posicion_y_rectangulo))
pygame.display.flip()

time.sleep(2)  # Mostrar el mensaje de resultado durante 2 segundos
exec(open("./main.py").read())
pygame.quit()
sys.exit()
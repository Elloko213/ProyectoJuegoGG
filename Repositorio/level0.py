import pygame

pygame.init()

# RGB
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Nombres predefinidos
negro = pygame.Color("black")
blanco = pygame.Color("white")
amarillo = pygame.Color("yellow")

# Valores decimales
cian = (0.0, 1.0, 1.0)
magenta = (1.0, 0.0, 1.0)
gris = (0.5, 0.5, 0.5)

ancho = 900
alto = 900
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Rectángulo Cambiante")

ancho_rectangulo = 100
alto_rectangulo = 100
posicion_x_rectangulo = 0
posicion_y_rectangulo = 0

velocidad_rectangulo = 0.5  # Variable para moderar la velocidad de movimiento

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

posicion_x_circulo = 800
posicion_y_circulo = 800
radio_circulo = 50

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        print(evento)

    teclas = pygame.key.get_pressed()

    # ------------COLISIÓN----------------------
    if teclas[pygame.K_UP]:
        posicion_y_rectangulo = max(posicion_y_rectangulo - velocidad_rectangulo, 0)  # Limitar el movimiento hacia arriba dentro de la ventana
        if (posicion_y_rectangulo < posicion_y_bloque1 + alto_bloque1 and
                posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque1):
            if posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque1 and posicion_x_rectangulo < posicion_x_bloque1 + ancho_bloque1:
                posicion_y_rectangulo = posicion_y_bloque1 + alto_bloque1

    if teclas[pygame.K_DOWN]:
        posicion_y_rectangulo = min(posicion_y_rectangulo + velocidad_rectangulo, alto - alto_rectangulo)  # Limitar el movimiento hacia abajo dentro de la ventana
        if (posicion_y_rectangulo < posicion_y_bloque1 + alto_bloque1 and
                posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque1):
            if posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque1 and posicion_x_rectangulo < posicion_x_bloque1 + ancho_bloque1:
                posicion_y_rectangulo = posicion_y_bloque1 - alto_rectangulo

        if (posicion_y_rectangulo < posicion_y_bloque2 + alto_bloque2 and
                posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque2):
            if posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque2 and posicion_x_rectangulo < posicion_x_bloque2 + ancho_bloque2:
                posicion_y_rectangulo = posicion_y_bloque2 - alto_rectangulo

        if (posicion_y_rectangulo < posicion_y_bloque3 + alto_bloque3 and
                posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque3):
            if posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque3 and posicion_x_rectangulo < posicion_x_bloque3 + ancho_bloque3:
                posicion_y_rectangulo = posicion_y_bloque3 - alto_rectangulo

    if teclas[pygame.K_LEFT]:
        posicion_x_rectangulo = max(posicion_x_rectangulo - velocidad_rectangulo, 0)  # Limitar el movimiento hacia la izquierda dentro de la ventana

    if teclas[pygame.K_RIGHT]:
        posicion_x_rectangulo = min(posicion_x_rectangulo + velocidad_rectangulo, ancho - ancho_rectangulo)  # Limitar el movimiento hacia la derecha dentro de la ventana

    if (posicion_x_rectangulo < posicion_x_bloque1 + ancho_bloque1 and
            posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque1):
        if posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque1 and posicion_y_rectangulo < posicion_y_bloque1 + alto_bloque1:
            if posicion_x_rectangulo < posicion_x_bloque1 + ancho_bloque1 // 2:
                posicion_x_rectangulo = posicion_x_bloque1 - ancho_rectangulo
            else:
                posicion_x_rectangulo = posicion_x_bloque1 + ancho_bloque1

    if (posicion_x_rectangulo < posicion_x_bloque2 + ancho_bloque2 and
            posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque2):
        if posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque2 and posicion_y_rectangulo < posicion_y_bloque2 + alto_bloque2:
            if posicion_x_rectangulo < posicion_x_bloque2 + ancho_bloque2 // 2:
                posicion_x_rectangulo = posicion_x_bloque2 - ancho_rectangulo
            else:
                posicion_x_rectangulo = posicion_x_bloque2 + ancho_bloque2

    if (posicion_x_rectangulo < posicion_x_bloque3 + ancho_bloque3 and
            posicion_x_rectangulo + ancho_rectangulo > posicion_x_bloque3):
        if posicion_y_rectangulo + alto_rectangulo > posicion_y_bloque3 and posicion_y_rectangulo < posicion_y_bloque3 + alto_bloque3:
            if posicion_x_rectangulo < posicion_x_bloque3 + ancho_bloque3 // 2:
                posicion_x_rectangulo = posicion_x_bloque3 - ancho_rectangulo
            else:
                posicion_x_rectangulo = posicion_x_bloque3 + ancho_bloque3
    # ------------COLISIÓN----------------------

    ventana.fill(blanco)
    pygame.draw.rect(ventana, (10, 10, 10), (posicion_x_rectangulo, posicion_y_rectangulo, ancho_rectangulo, alto_rectangulo))
    pygame.draw.rect(ventana, (50, 50, 50), (posicion_x_bloque1, posicion_y_bloque1, ancho_bloque1, alto_bloque1))
    pygame.draw.rect(ventana, (50, 50, 50), (posicion_x_bloque2, posicion_y_bloque2, ancho_bloque2, alto_bloque2))
    pygame.draw.rect(ventana, (50, 50, 50), (posicion_x_bloque3, posicion_y_bloque3, ancho_bloque3, alto_bloque3))
    pygame.draw.circle(ventana, (amarillo), (posicion_x_circulo, posicion_y_circulo), radio_circulo)
    pygame.display.flip()

pygame.quit()

import pygame
import time
import os
from piezas import pieza, Figura

pygame.init()

abrir_puerta = False


def colision_ventana(personaje_x, personaje_y, personaje_ancho, personaje_alto, piezas):
    for p in piezas:
        if p.tipo == "ventana":
            # Obtener la posición y dimensiones de la ventana
            x_ventana, y_ventana = p.figura.posicion
            ancho_ventana, alto_ventana = p.figura.dimensiones

            # Verificar si el personaje colisiona con la ventana
            if (personaje_x < x_ventana + ancho_ventana
                and personaje_x + personaje_ancho > x_ventana
                and personaje_y < y_ventana + alto_ventana
                    and personaje_y + personaje_alto > y_ventana):
                # El personaje colisionó con la ventana

                # Si la pieza no ha sido atravesada
                if not p.atravesada:
                    # Cambiar el color de la ventana a azul
                    p.cambiar_color(pygame.Color("blue"))

                    # Si el color original de la ventana es amarillo, cambiar su tipo a "pito bloque"
                    if p.color == pygame.Color("yellow"):
                        p.tipo = "bloque"

                    # Marcar la pieza como atravesada
                    p.atravesada = True
            else:
                # Restaurar el color original de la ventana si la pieza ha sido atravesada
                if p.atravesada:
                    p.cambiar_color(pygame.Color("yellow"))
                    p.atravesada = False


def abir_cerrar_puertas(piezas, personaje_x, personaje_y, personaje_ancho, personaje_alto, abrir_puerta):
    for p in piezas:
        if p.tipo == "puerta":
            # Obtener la posición y dimensiones del bloque
            x_bloque, y_bloque = p.figura.posicion
            ancho_bloque, alto_bloque = p.figura.dimensiones

            # Verificar si el personaje colisiona con el bloque
            if (personaje_x < x_bloque + ancho_bloque and
                    personaje_x + personaje_ancho > x_bloque and
                    personaje_y < y_bloque + alto_bloque and
                    personaje_y + personaje_alto > y_bloque):

                # Calcular las áreas de colisión
                area_colision_x = min(
                    personaje_x + personaje_ancho, x_bloque + ancho_bloque) - max(personaje_x, x_bloque)
                area_colision_y = min(
                    personaje_y + personaje_alto, y_bloque + alto_bloque) - max(personaje_y, y_bloque)

                # Calcular el área de colisión mínima (el área más pequeña entre el personaje y el bloque)
                area_colision_minima = min(area_colision_x, area_colision_y)

                # Actualizar la posición del personaje en función del área de colisión mínima
                if area_colision_minima == area_colision_x:
                    if personaje_x < x_bloque:
                        personaje_x = x_bloque - personaje_ancho
                    else:
                        personaje_x = x_bloque + ancho_bloque
                else:
                    if personaje_y < y_bloque:
                        personaje_y = y_bloque - personaje_alto
                    else:
                        personaje_y = y_bloque + alto_bloque

                # Cambiar las dimensiones de la puerta en función de ancho y alto
                if abrir_puerta:
                    if ancho_bloque > alto_bloque:
                        p.figura.dimensiones = (10, 50)
                    else:
                        p.figura.dimensiones = (50, 10)

    return personaje_x, personaje_y


def verificar_piezas_bloque(piezas, personaje_x, personaje_y, personaje_ancho, personaje_alto):
    for p in piezas:
        if p.tipo == "bloque":
            # Obtener la posición y dimensiones del bloque
            x_bloque, y_bloque = p.figura.posicion
            ancho_bloque, alto_bloque = p.figura.dimensiones

            # Verificar si el personaje colisiona con el bloque
            if (personaje_x < x_bloque + ancho_bloque and
                    personaje_x + personaje_ancho > x_bloque and
                    personaje_y < y_bloque + alto_bloque and
                    personaje_y + personaje_alto > y_bloque):
                # Calcular las áreas de colisión
                area_colision_x = min(
                    personaje_x + personaje_ancho, x_bloque + ancho_bloque) - max(personaje_x, x_bloque)
                area_colision_y = min(
                    personaje_y + personaje_alto, y_bloque + alto_bloque) - max(personaje_y, y_bloque)

                # Calcular el área de colisión mínima (el área más pequeña entre el personaje y el bloque)
                area_colision_minima = min(area_colision_x, area_colision_y)

                # Actualizar la posición del personaje en función del área de colisión mínima
                if area_colision_minima == area_colision_x:
                    if personaje_x < x_bloque:
                        personaje_x = x_bloque - personaje_ancho
                    else:
                        personaje_x = x_bloque + ancho_bloque
                else:
                    if personaje_y < y_bloque:
                        personaje_y = y_bloque - personaje_alto
                    else:
                        personaje_y = y_bloque + alto_bloque

    return personaje_x, personaje_y


def colision_cookie(personaje_x, personaje_y, personaje_ancho, personaje_alto, cookies):
    for p in cookies:
        if p.tipo == "ventana":
            # Obtener la posición y dimensiones de la cookie
            x_cookie, y_cookie = p.figura.posicion
            ancho_cookie, alto_cookie = p.figura.dimensiones

            # Verificar si el personaje colisiona con la cookie
            if (personaje_x < x_cookie + ancho_cookie
                and personaje_x + personaje_ancho > x_cookie
                and personaje_y < y_cookie + alto_cookie
                    and personaje_y + personaje_alto > y_cookie):
                # El personaje colisionó con la cookie
                cookies.remove(p)
            else:
                # Restaurar el color original de la ventana si la pieza ha sido atravesada
                if p.atravesada:
                    p.cambiar_color(pygame.Color("yellow"))
                    p.atravesada = False


# Dimensiones de la ventana
ancho = 1200
alto = 900

# Crear la ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento de Personaje")

# Colores
negro = (0,0,0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
celeste = (0, 191, 255)
CAFE = (101, 67, 33)
PLOMO = (169, 169, 169)
AMARILLO = (255, 255, 0)
yellow = pygame.Color(255, 255, 0)

# Tamaño y posición inicial del personaje
personaje_ancho = 30
personaje_alto = 30
personaje_x = 30
personaje_y = 850

# Velocidad de movimiento del personaje
velocidad = 0.4

# Crear una lista de piezas
piezas = [
    pieza("bloque", CAFE, Figura("rectangulo", (100, 100), (50, 10))),
    pieza("ventana", celeste, Figura("rectangulo", (150, 100), (60, 10))),

    pieza("bloque", CAFE, Figura("rectangulo", (210, 100), (40, 10))),
    pieza("ventana", celeste, Figura("rectangulo", (250, 100), (60, 10))),

    pieza("bloque", CAFE, Figura("rectangulo", (310, 100), (680, 10))),
    pieza("ventana", celeste, Figura("rectangulo", (990, 100), (60, 10))),

    pieza("bloque", CAFE, Figura("rectangulo", (1050, 100), (50, 10))),


    pieza("bloque", CAFE, Figura("rectangulo", (100, 100), (10, 700))),
    pieza("bloque", CAFE, Figura("rectangulo", (1100, 100), (10, 700))),


    pieza("bloque", CAFE, Figura("rectangulo", (100, 800), (50, 10))),

    pieza("bloque", CAFE, Figura("rectangulo", (200, 800), (790, 10))),

    pieza("bloque", CAFE, Figura("rectangulo", (1050, 800), (60, 10))),
    pieza("ventana", celeste, Figura("rectangulo", (990, 800), (60, 10))),

    pieza("puerta", rojo, Figura("rectangulo", (150, 800), (50, 10))),




    pieza("bloque", PLOMO, Figura("rectangulo", (350, 400), (50, 10))),

    pieza("puerta", rojo, Figura("rectangulo", (400, 400), (50, 10))),
    pieza("bloque", PLOMO, Figura("rectangulo", (450, 400), (250, 10))),
    pieza("puerta", rojo, Figura("rectangulo", (700, 400), (50, 10))),
    pieza("bloque", PLOMO, Figura("rectangulo", (750, 400), (100, 10))),
    pieza("bloque", PLOMO, Figura("rectangulo", (350, 100), (10, 310))),

    pieza("bloque", PLOMO, Figura("rectangulo", (820, 390), (280, 130))),

    pieza("bloque", PLOMO, Figura("rectangulo", (680, 100), (10, 310))),

    pieza("bloque", PLOMO, Figura("rectangulo", (270, 500), (430, 10))),
    pieza("puerta", rojo, Figura("rectangulo", (700, 500), (50, 10))),
    pieza("bloque", PLOMO, Figura("rectangulo", (750, 500), (80, 10))),

    pieza("bloque", PLOMO, Figura("rectangulo", (680, 500), (10, 310))),


    # Agregar un círculo
    # pieza("bloque", AMARILLO, Figura("circulo", (600, 200), (20,0))),

    # Agregar un triángulo
    # pieza("ventana", amarillo, Figura("triangulo", (800, 200), (30, 30))),
]

cookies = [
    pieza("ventana", AMARILLO, Figura("circulo", (600, 200), (20, 0))),
    pieza("ventana", AMARILLO, Figura("circulo", (800, 700), (20, 0))),
    pieza("ventana", AMARILLO, Figura("circulo", (900, 200), (20, 0))),]

bg_surf = pygame.image.load('./assets/map2.png').convert()
bg_surf = pygame.transform.scale(bg_surf, (ancho, alto))
imagen_cookie_original = pygame.image.load('./assets/cookie.png')
# Configurar tiempo límite
tiempo_limite = 30
tiempo_inicio = time.time()

# Bucle principal del juego
ejecutando = True

while ejecutando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Obtener el estado de las teclas
    teclas = pygame.key.get_pressed()

    # Movimiento del personaje
    if teclas[pygame.K_UP]:
        personaje_y -= velocidad
    if teclas[pygame.K_DOWN]:
        personaje_y += velocidad
    if teclas[pygame.K_LEFT]:
        personaje_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        personaje_x += velocidad

    # Limitar el personaje dentro de los límites de la ventana
    if personaje_x < 0:
        personaje_x = 0
    if personaje_x > ancho - personaje_ancho:
        personaje_x = ancho - personaje_ancho
    if personaje_y < 0:
        personaje_y = 0
    if personaje_y > alto - personaje_alto:
        personaje_y = alto - personaje_alto

    # Limpiar la ventana
    ventana.fill(CAFE)
    ventana.blit(bg_surf, (0, 0))
    # Verificar colisión con ventanas
    colision_ventana(personaje_x, personaje_y,personaje_ancho, personaje_alto, piezas)
    # verify collision with coookie
    colision_cookie(personaje_x, personaje_y,personaje_ancho, personaje_alto, cookies)

    # Verificar si las piezas bloque impiden el movimiento del personaje
    personaje_x, personaje_y = verificar_piezas_bloque(
        piezas, personaje_x, personaje_y, personaje_ancho, personaje_alto)
   # Verificar si las piezas bloque impiden el movimiento del personaje
    personaje_x, personaje_y = verificar_piezas_bloque(
        piezas, personaje_x, personaje_y, personaje_ancho, personaje_alto)

    # Verificar si se presiona la tecla ENTER para abrir la puerta
    if teclas[pygame.K_RETURN]:
        abrir_puerta = True
    else:
        abrir_puerta = False

    # Verificar el tiempo transcurrido
    tiempo_actual = time.time()
    tiempo_transcurrido = int(tiempo_actual - tiempo_inicio)
    tiempo_restante = tiempo_limite - tiempo_transcurrido

    if tiempo_restante <= 0:
        # Mostrar mensaje de resultado
        ventana.fill(blanco)
        if tiempo_restante <= 0:
            mensaje_perdiste = fuente.render("¡Perdiste el juego!", True, negro)
            ventana.blit(mensaje_perdiste, (
                ancho // 2 - mensaje_perdiste.get_width() // 2, alto // 2 - mensaje_perdiste.get_height() // 2))

        pygame.display.flip()

        time.sleep(2)  # Mostrar el mensaje de resultado durante 2 segundos
        exec(open("./main.py").read())
        ejecutando = False  # Terminar el programa

    # Mostrar tiempo restante en la ventana
    fuente = pygame.font.Font(None, 36)
    mensaje_tiempo = fuente.render("Tiempo restante: " + str(tiempo_restante) + " segundos", True, negro)
    ventana.blit(mensaje_tiempo, (10, 10))

    # Verificar si se comieron todas las cookies
    if len(cookies) == 0:
        # Mostrar mensaje de resultado
        ventana.fill(blanco)
        if tiempo_restante <= 0:
            mensaje_perdiste = fuente.render("¡Perdiste el juego!", True, negro)
            ventana.blit(mensaje_perdiste, (
            ancho // 2 - mensaje_perdiste.get_width() // 2, alto // 2 - mensaje_perdiste.get_height() // 2))
        else:
            mensaje_ganaste = fuente.render("¡Has ganado!", True, negro)
            ventana.blit(mensaje_ganaste,
                         (ancho // 2 - mensaje_ganaste.get_width() // 2, alto // 2 - mensaje_ganaste.get_height() // 2))

        pygame.display.flip()

        time.sleep(2)  # Mostrar el mensaje de resultado durante 2 segundos
        exec(open("./main.py").read())


    # Dibujar el personaje
    pygame.draw.rect(ventana, rojo, (personaje_x, personaje_y,
                     personaje_ancho, personaje_alto))
    personaje_x, personaje_y = abir_cerrar_puertas(
        piezas, personaje_x, personaje_y, personaje_ancho, personaje_alto, abrir_puerta)

    # Dibujar las piezas
    for p in piezas:
        if p.tipo == "ventana" and p.color == pygame.Color("yellow"):
            p.tipo = "bloque"
        p.dibujar(ventana)

    for p in cookies:  
        # Redimensionar la imagen al tamaño de la cookie
        imagen_cookie = pygame.transform.scale(imagen_cookie_original, (2 * p.figura.dimensiones[0], 2 * p.figura.dimensiones[0]))
        
        if p.tipo == "ventana":
            ventana.blit(imagen_cookie, (p.figura.posicion[0] - p.figura.dimensiones[0], p.figura.posicion[1] - p.figura.dimensiones[0]))
        else:
            p.dibujar(ventana)
    # Actualizar la ventana
    pygame.display.flip()

# Salir de Pygame
pygame.quit()

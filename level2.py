import pygame
import time
from piezas import pieza, Figura

# pygame setup
pygame.init()

abrir_puerta = False
def colision_asp(personaje_x, personaje_y, personaje_ancho, personaje_alto, aspiradora):
    if aspiradora.tipo == "bloque":
            # Obtener la posición y dimensiones de la ventana
            x_aspiradora, y_aspiradora = aspiradora.figura.posicion
            ancho_aspiradora, alto_aspiradora = aspiradora.figura.dimensiones

            # Verificar si el personaje colisiona con la ventana
            if (personaje_x < x_aspiradora + ancho_aspiradora
                and personaje_x + personaje_ancho > x_aspiradora
                and personaje_y < y_aspiradora + alto_aspiradora
                    and personaje_y + personaje_alto > y_aspiradora):
                # Mostrar mensaje de resultado
                screen.fill(blanco)
                mensaje_perdiste = fuente.render("¡Perdiste el juego!", True, negro)
                screen.blit(mensaje_perdiste, (
                        ancho // 2 - mensaje_perdiste.get_width() // 2, alto // 2 - mensaje_perdiste.get_height() // 2))

                pygame.display.flip()

                time.sleep(2)  # Mostrar el mensaje de resultado durante 2 segundos
                exec(open("./main.py").read())
                ejecutando = False  # Terminar el programa

def colision_screen(personaje_x, personaje_y, personaje_ancho, personaje_alto, piezas):
    for p in piezas:
        if p.tipo == "screen":
            # Obtener la posición y dimensiones de la screen
            x_screen, y_screen = p.figura.posicion
            ancho_screen, alto_screen = p.figura.dimensiones

            # Verificar si el personaje colisiona con la screen
            if (personaje_x < x_screen + ancho_screen
                and personaje_x + personaje_ancho > x_screen
                and personaje_y < y_screen + alto_screen
                    and personaje_y + personaje_alto > y_screen):
                # El personaje colisionó con la screen

                # Si la pieza no ha sido atravesada
                if not p.atravesada:
                    # Cambiar el color de la screen a azul
                    p.cambiar_color(pygame.Color("blue"))

                    # Si el color original de la screen es amarillo, cambiar su tipo a "pito bloque"
                    if p.color == pygame.Color("yellow"):
                        p.tipo = "bloque"

                    # Marcar la pieza como atravesada
                    p.atravesada = True
            else:
                # Restaurar el color original de la screen si la pieza ha sido atravesada
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

ancho = 1280
alto = 736

screen = pygame.display.set_mode((1280,736))
pygame.display.set_caption("Movimiento de Personaje")

# Colores
negro = (0,0,0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
celeste = (0, 191, 255)
CAFE = (101, 67, 33)
PLOMO = (74,74,74)
AMARILLO = (255, 255, 0)
BLACK = (0,0,0)
yellow = pygame.Color(255, 255, 0)

# Tamaño y posición inicial del personaje
personaje_ancho = 30
personaje_alto = 30
personaje_x = 30
personaje_y = 850

# Velocidad de movimiento del personaje
velocidad = 0.6

#piezas
piezas = [
    #horizontal
    pieza("bloque", PLOMO, Figura("rectangulo", (0, 0), (246, 20))),
    pieza("bloque", PLOMO, Figura("rectangulo", (458, 0), (44, 20))),
    pieza("bloque", PLOMO, Figura("rectangulo", (745, 0), (110, 20))),
    pieza("bloque", PLOMO, Figura("rectangulo", (1160, 0), (120, 20))),
    pieza("bloque", PLOMO, Figura("rectangulo", (0, 330), (405, 43))),
    pieza("bloque", PLOMO, Figura("rectangulo", (535, 363), (305, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (950, 363), (370, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (845, 715), (170, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (845, 715), (170, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (0, 715), (85, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (170, 715), (43, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (715, 715), (43, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (1100, 715), (43, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (1225, 715), (55, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (300, 715), (330, 40))),
    pieza("bloque", PLOMO, Figura("rectangulo", (620, 490), (330, 40))),
    
    #vertical
    pieza("bloque", PLOMO, Figura("rectangulo", (0, 0), (20, 85))),
    pieza("bloque", PLOMO, Figura("rectangulo", (0, 235), (20, 235))),
    pieza("bloque", PLOMO, Figura("rectangulo", (0, 615), (20, 235))),
    pieza("bloque", PLOMO, Figura("rectangulo", (365, 545), (40, 235))),
    pieza("bloque", PLOMO, Figura("rectangulo", (365, 245), (40, 175))),
    pieza("bloque", PLOMO, Figura("rectangulo", (490, 490), (40, 235))),
    pieza("bloque", PLOMO, Figura("rectangulo", (910, 490), (40, 235))),
    pieza("bloque", PLOMO, Figura("rectangulo", (780, 0), (40, 405))),
    pieza("bloque", PLOMO, Figura("rectangulo", (1255, 0), (25, 55))),
    pieza("bloque", PLOMO, Figura("rectangulo", (1255, 135), (25, 45))),
    pieza("bloque", PLOMO, Figura("rectangulo", (1255, 330), (25, 110))),
    pieza("bloque", PLOMO, Figura("rectangulo", (1255, 520), (25, 50))),
    pieza("bloque", PLOMO, Figura("rectangulo", (1255, 650), (25, 80))),
    
    #windows with block type
    pieza("bloque", celeste, Figura("rectangulo", (255, 0), (195, 20))),
    pieza("bloque", celeste, Figura("rectangulo", (511, 0), (225, 20))),
    pieza("bloque", celeste, Figura("rectangulo", (865, 0), (290, 20))),
    pieza("bloque", celeste, Figura("rectangulo", (95, 715), (65, 20))),
    pieza("bloque", celeste, Figura("rectangulo", (225, 715), (65, 20))),
    pieza("bloque", celeste, Figura("rectangulo", (640, 715), (65, 20))),
    pieza("bloque", celeste, Figura("rectangulo", (768, 715), (65, 20))),
    pieza("bloque", celeste, Figura("rectangulo", (1025, 715), (65, 20))),
    pieza("bloque", celeste, Figura("rectangulo", (1150, 715), (65, 20))),
    
    pieza("bloque", celeste, Figura("rectangulo", (0, 95), (20, 130))),
    pieza("bloque", celeste, Figura("rectangulo", (0, 480), (20, 128))),
    pieza("bloque", celeste, Figura("rectangulo", (1260, 65), (20, 63))),
    pieza("bloque", celeste, Figura("rectangulo", (1260, 190), (20, 130))),
    pieza("bloque", celeste, Figura("rectangulo", (1260, 448), (20, 64))),
    pieza("bloque", celeste, Figura("rectangulo", (1260, 575), (20, 64))),


    # Agregar un círculo
    # pieza("bloque", AMARILLO, Figura("circulo", (600, 200), (20,0))),

    # Agregar un triángulo
    # pieza("screen", amarillo, Figura("triangulo", (800, 200), (30, 30))),
]

cookies = [
    pieza("ventana", AMARILLO, Figura("circulo", (600, 200), (20, 0))),
    pieza("ventana", AMARILLO, Figura("circulo", (800, 700), (20, 0))),
    pieza("ventana", AMARILLO, Figura("circulo", (900, 200), (20, 0))),
    pieza("ventana", AMARILLO, Figura("circulo", (200, 200), (20, 0))),
    pieza("ventana", AMARILLO, Figura("circulo", (200, 650), (20, 0))),]

aspiradora1 = pieza("bloque", CAFE, Figura("rectangulo", (420, 50), (50, 50)))
aspiradora2 = pieza("bloque", CAFE, Figura("rectangulo", (550, 580), (50, 50)))
aspiradora3 = pieza("bloque", CAFE, Figura("rectangulo", (850, 240), (50, 50)))
aspiradora4 = pieza("bloque", CAFE, Figura("rectangulo", (170, 460), (50, 50)))
#aspiradora5 = pieza("bloque", CAFE, Figura("rectangulo", (600, 300), (50, 50)))
FPS = 0.5
# game setup
bg_surf = pygame.image.load('./assets/map3.png').convert()
bg_surf = pygame.transform.scale(bg_surf, (ancho, alto))
imagen_cookie_original = pygame.image.load('./assets/cookie.png')
#imagen del personaje
personaje_imagen = pygame.image.load("./assets/cat2.png")
personaje_imagen = pygame.transform.scale(personaje_imagen, (personaje_ancho, personaje_alto))
#imagen de la aspiradora
aspiradora_image = pygame.image.load('./assets/aspiradora2.png')
# Configurar tiempo límite
tiempo_limite = 30
tiempo_inicio = time.time()

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

    # Limitar el personaje dentro de los límites de la screen
    if personaje_x < 0:
        personaje_x = 0
    if personaje_x > ancho - personaje_ancho:
        personaje_x = ancho - personaje_ancho
    if personaje_y < 0:
        personaje_y = 0
    if personaje_y > alto - personaje_alto:
        personaje_y = alto - personaje_alto

    # Limpiar la screen
    screen.fill(CAFE)
    screen.blit(bg_surf, (0, 0))
    # Verificar colisión con screens
    colision_screen(personaje_x, personaje_y,personaje_ancho, personaje_alto, piezas)
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
        screen.fill(blanco)
        if tiempo_restante <= 0:
            mensaje_perdiste = fuente.render("¡Perdiste el juego!", True, negro)
            screen.blit(mensaje_perdiste, (ancho // 2 - mensaje_perdiste.get_width() // 2, alto // 2 - mensaje_perdiste.get_height() // 2))
        pygame.display.flip()

        time.sleep(2)  # Mostrar el mensaje de resultado durante 2 segundos
        exec(open("./main.py").read())
        ejecutando = False  # Terminar el programa

    # Mostrar tiempo restante en la screen
    fuente = pygame.font.Font(None, 36)
    mensaje_tiempo = fuente.render("Tiempo restante: " + str(tiempo_restante) + " segundos", True, negro)
    screen.blit(mensaje_tiempo, (40, 50))

    # Verificar si se comieron todas las cookies
    if len(cookies) == 0:
        # Mostrar mensaje de resultado
        screen.fill(blanco)
        if tiempo_restante <= 0:
            mensaje_perdiste = fuente.render("¡Perdiste el juego!", True, negro)
            screen.blit(mensaje_perdiste, (ancho // 2 - mensaje_perdiste.get_width() // 2, alto // 2 - mensaje_perdiste.get_height() // 2))
        else:
            mensaje_ganaste = fuente.render("¡Has ganado!", True, negro)
            screen.blit(mensaje_ganaste,
                         (ancho // 2 - mensaje_ganaste.get_width() // 2, alto // 2 - mensaje_ganaste.get_height() // 2))
        pygame.display.flip()

        time.sleep(2)  # Mostrar el mensaje de resultado durante 2 segundos
        exec(open("./main.py").read())


    # Dibujar el personaje
    #pygame.draw.rect(screen, rojo, (personaje_x, personaje_y,personaje_ancho, personaje_alto))

    screen.blit(personaje_imagen,(personaje_x,personaje_y))
    #screen.blit(personaje_imagen2, (personaje_x, personaje_y))
    personaje_x, personaje_y = abir_cerrar_puertas(piezas, personaje_x, personaje_y, personaje_ancho, personaje_alto, abrir_puerta)

    for p in piezas:
        if p.tipo == "screen" and p.color == pygame.Color("yellow"):
            p.tipo = "bloque"
        p.dibujar(screen)

    for p in cookies:
        # Redimensionar la imagen al tamaño de la cookie
        imagen_cookie = pygame.transform.scale(imagen_cookie_original, (2 * p.figura.dimensiones[0], 2 * p.figura.dimensiones[0]))
        
        if p.tipo == "ventana":
            screen.blit(imagen_cookie, (p.figura.posicion[0] - p.figura.dimensiones[0], p.figura.posicion[1] - p.figura.dimensiones[0]))
        else:
            p.dibujar(screen)

    posicion_aspiradora1 = list(aspiradora1.figura.posicion)
    posicion_aspiradora2 = list(aspiradora2.figura.posicion)
    posicion_aspiradora3 = list(aspiradora3.figura.posicion)
    posicion_aspiradora4 = list(aspiradora4.figura.posicion)

    if posicion_aspiradora1[1] == 640:
        switch_asp1 = "izq1"
    if posicion_aspiradora1[1] == 50:
        switch_asp1 = "der1"


    if switch_asp1 == "izq1":
        posicion_aspiradora1[1] -= FPS
    if switch_asp1 == "der1":
        posicion_aspiradora1[1] += FPS
    aspiradora1.figura.posicion = tuple(posicion_aspiradora1)


    if posicion_aspiradora2[0] == 830:
        switch_asp2 = "izq2"
    if posicion_aspiradora2[0] == 550:
        switch_asp2 = "der2"


    if switch_asp2 == "izq2":
        posicion_aspiradora2[0] -= FPS
    if switch_asp2 == "der2":
        posicion_aspiradora2[0] += FPS
    aspiradora2.figura.posicion = tuple(posicion_aspiradora2)


    if posicion_aspiradora3[0] == 1050:
        switch_asp3 = "izq3"
    if posicion_aspiradora3[0] == 850:
        switch_asp3 = "der3"


    if switch_asp3 == "izq3":
        posicion_aspiradora3[0] -= FPS
    if switch_asp3 == "der3":
        posicion_aspiradora3[0] += FPS
    aspiradora3.figura.posicion = tuple(posicion_aspiradora3)


    if posicion_aspiradora4[0] == 350:
        switch_asp4 = "izq4"
    if posicion_aspiradora4[0] == 170:
        switch_asp4 = "der4"


    if switch_asp4 == "izq4":
        posicion_aspiradora4[0] -= FPS
    if switch_asp4 == "der4":
        posicion_aspiradora4[0] += FPS
    aspiradora4.figura.posicion = tuple(posicion_aspiradora4)

    colision_asp(personaje_x, personaje_y, personaje_ancho, personaje_alto, aspiradora1)
    colision_asp(personaje_x, personaje_y, personaje_ancho, personaje_alto, aspiradora2)
    colision_asp(personaje_x, personaje_y, personaje_ancho, personaje_alto, aspiradora3)
    colision_asp(personaje_x, personaje_y, personaje_ancho, personaje_alto, aspiradora4)

    screen.blit(aspiradora_image, aspiradora1.figura.posicion)
    screen.blit(aspiradora_image, aspiradora2.figura.posicion)
    screen.blit(aspiradora_image, aspiradora3.figura.posicion)
    screen.blit(aspiradora_image, aspiradora4.figura.posicion)

    pygame.display.flip()

# Salir de Pygame
pygame.quit()


import pygame
import time
from piezas import pieza, Figura

pygame.init()

abrir_puerta=False

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
                area_colision_x = min(personaje_x + personaje_ancho, x_bloque + ancho_bloque) - max(personaje_x, x_bloque)
                area_colision_y = min(personaje_y + personaje_alto, y_bloque + alto_bloque) - max(personaje_y, y_bloque)

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
        if p.tipo == "bloque" :
            # Obtener la posición y dimensiones del bloque
            x_bloque, y_bloque = p.figura.posicion
            ancho_bloque, alto_bloque = p.figura.dimensiones

            # Verificar si el personaje colisiona con el bloque
            if (personaje_x < x_bloque + ancho_bloque and
                    personaje_x + personaje_ancho > x_bloque and
                    personaje_y < y_bloque + alto_bloque and
                    personaje_y + personaje_alto > y_bloque):
                # Calcular las áreas de colisión
                area_colision_x = min(personaje_x + personaje_ancho, x_bloque + ancho_bloque) - max(personaje_x, x_bloque)
                area_colision_y = min(personaje_y + personaje_alto, y_bloque + alto_bloque) - max(personaje_y, y_bloque)

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

# Dimensiones de la ventana
ancho = 1200
alto = 900

# Crear la ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento de Personaje")

# Colores
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
celeste= (0, 191, 255)
CAFE = (101, 67, 33)
PLOMO = (169, 169, 169)
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
    #pieza("ventana", amarillo, Figura("circulo", (600, 200), (10,0))),

    # Agregar un triángulo
    #pieza("ventana", amarillo, Figura("triangulo", (800, 200), (30, 30))),
       
]


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
    ventana.fill(blanco)
    # Verificar colisión con ventanas
    colision_ventana(personaje_x, personaje_y, personaje_ancho, personaje_alto, piezas)
    # Verificar si las piezas bloque impiden el movimiento del personaje
    personaje_x, personaje_y = verificar_piezas_bloque(piezas, personaje_x, personaje_y, personaje_ancho, personaje_alto)
   # Verificar si las piezas bloque impiden el movimiento del personaje
    personaje_x, personaje_y = verificar_piezas_bloque(piezas, personaje_x, personaje_y, personaje_ancho, personaje_alto)
     

    # Verificar si se presiona la tecla ENTER para abrir la puerta
    if teclas[pygame.K_RETURN]:
        abrir_puerta = True
    else:
        abrir_puerta = False

    # Dibujar el personaje
    pygame.draw.rect(ventana, rojo, (personaje_x, personaje_y, personaje_ancho, personaje_alto))
    personaje_x, personaje_y = abir_cerrar_puertas(piezas, personaje_x, personaje_y, personaje_ancho, personaje_alto, abrir_puerta)

    # Dibujar las piezas
    for p in piezas:
        if p.tipo == "ventana" and p.color == pygame.Color("yellow"):
            p.tipo = "bloque"
        p.dibujar(ventana)
    # Actualizar la ventana
    pygame.display.flip()

# Salir de Pygame
pygame.quit()


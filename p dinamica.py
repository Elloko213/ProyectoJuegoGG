import pygame
import time
import os
from piezas import pieza, Figura
from queue import PriorityQueue
from math import sqrt


pygame.init()
ancho = 1200
alto = 900

# Crear la ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento de Personaje")


costos_memoizados = {}


def distancia(punto1, punto2):
    # Calcular la distancia euclidiana entre dos puntos
    x1, y1 = punto1
    x2, y2 = punto2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def buscar_camino(inicio, objetivo, obstaculos):
    frontera = PriorityQueue()
    frontera.put((0, inicio))
    padres = {}
    costos = {}
    padres[inicio] = None
    costos[inicio] = 0

    while not frontera.empty():
        _, actual = frontera.get()

        if actual == objetivo:
            camino = [actual]
            while actual != inicio:
                actual = padres[actual]
                camino.append(actual)
            camino.reverse()
            return camino

        for vecino in obtener_vecinos(actual, obstaculos):
            nuevo_costo = costos[actual] + distancia(actual, vecino)
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + distancia(vecino, objetivo)
                frontera.put((prioridad, vecino))
                padres[vecino] = actual

                # Almacenar el costo calculado en la memoria
                costos_memoizados[vecino] = nuevo_costo

    return None

def obtener_vecinos(punto, obstaculos):
    x, y = punto
    vecinos = [(x + 10, y), (x - 10, y), (x, y + 10), (x, y - 10)]
    vecinos_validos = []
    for vecino in vecinos:
        if vecino not in costos_memoizados:  # Verificar si ya está memoizado
            if not vecino_ocupado(vecino[0], vecino[1], obstaculos):
                vecinos_validos.append(vecino)
        else:
            # Utilizar el costo memoizado en lugar de calcularlo nuevamente
            vecinos_validos.append(vecino)

    return vecinos_validos


def vecino_ocupado(x, y, obstaculos):
    for obstaculo in obstaculos:
        if obstaculo.tipo == "bloque" and (
            x >= obstaculo.figura.posicion[0]
            and x <= obstaculo.figura.posicion[0] + obstaculo.figura.dimensiones[0]
            and y >= obstaculo.figura.posicion[1]
            and y <= obstaculo.figura.posicion[1] + obstaculo.figura.dimensiones[1]
        ):
            return True
    return False


# Colores
rosado = (255, 192, 203)  # R = 255, G = 192, B = 203
negro = (0, 0, 0)
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
personaje_x = 600
personaje_y = 200
velocidad = 0.4
cookies = [
    pieza("ventana", AMARILLO, Figura("circulo", (800, 700), (20, 0))),
    pieza("ventana", AMARILLO, Figura("circulo", (900, 200), (20, 0))),
    pieza("ventana", AMARILLO, Figura("circulo", (600, 200), (20, 0)))]
obstaculos = [
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
]

enemigo = pieza("bloque", azul, Figura("rectangulo", (600, 850), (50, 50)))
velocidad_enemigo = 0.01

enemigo_imagen = pygame.image.load("./assets/cat2.png")
enemigo_imagen = pygame.transform.scale(enemigo_imagen, (enemigo.figura.dimensiones[0], enemigo.figura.dimensiones[1]))


bg_surf = pygame.image.load('./assets/map2.png').convert()
bg_surf = pygame.transform.scale(bg_surf, (ancho, alto))
imagen_cookie_original = pygame.image.load('./assets/cookie.png')

ejecutando = True
objetivo_actual = 0  # Índice del objetivo actual en la lista de cookies

while ejecutando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
   
    # Calcular el camino óptimo para el enemigo
    inicio_enemigo = (enemigo.figura.posicion[0], enemigo.figura.posicion[1])
    objetivo_enemigo = (cookies[objetivo_actual].figura.posicion[0], cookies[objetivo_actual].figura.posicion[1])
    camino_enemigo = buscar_camino(inicio_enemigo, objetivo_enemigo, obstaculos)
    
    if camino_enemigo is not None:
        # Mover el enemigo por el camino óptimo
        siguiente_paso = camino_enemigo[1]
        enemigo.figura.posicion = (siguiente_paso[0], siguiente_paso[1])
        
        if enemigo.figura.posicion == objetivo_enemigo:
            objetivo_actual += 1
            if objetivo_actual >= len(cookies):
                objetivo_actual = 0

    # Limpiar la ventana
    ventana.fill(blanco)

    # Dibujar el camino
    for p in obstaculos:
        p.dibujar(ventana)
    
    # Dibujar el enemigo
    ventana.blit(enemigo_imagen, (enemigo.figura.posicion[0], enemigo.figura.posicion[1]))
    
    for p in cookies:
        imagen_cookie = pygame.transform.scale(imagen_cookie_original, (2 * p.figura.dimensiones[0], 2 * p.figura.dimensiones[0]))
        
        if p.tipo == "ventana":
            ventana.blit(imagen_cookie, (p.figura.posicion[0] - p.figura.dimensiones[0], p.figura.posicion[1] - p.figura.dimensiones[0]))
        else:
            p.dibujar(ventana)
    
     # Mostrar mensaje "GALLETAS"
    fuente = pygame.font.Font(None, 20)
    mensaje = fuente.render(str(costos_memoizados), True, (0, 0, 0))
    ventana.blit(mensaje, (10 , 10 - mensaje.get_height() // 2))

    pygame.display.flip()

# Salir de Pygame
pygame.quit()
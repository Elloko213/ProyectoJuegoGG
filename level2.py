import pygame, sys 
from piezas import pieza, Figura

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,736))
clock = pygame.time.Clock()

# Colores
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
    # pieza("ventana", amarillo, Figura("triangulo", (800, 200), (30, 30))),
]


# game setup
bg_surf = pygame.image.load('./assets/map3.png').convert()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(bg_surf,(0,0))
	# pathfinder.update()


	for p in piezas:
		if p.tipo == "ventana" and p.color == pygame.Color("yellow"):
			p.tipo = "bloque"
		p.dibujar(screen)

	pygame.display.update()
	clock.tick(60)
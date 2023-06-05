import pygame, sys 
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from piezas import pieza, Figura

# class Pathfinder:
# 	def __init__(self,matrix):

# 		# setup
# 		self.matrix = matrix
# 		self.grid = Grid(matrix = matrix)
# 		self.select_surf = pygame.image.load('./assets/selection.png').convert_alpha()

# 		# pathfinding
# 		self.path = []

# 		# Roomba
# 		self.roomba = pygame.sprite.GroupSingle(Roomba(self.empty_path))

# 	def empty_path(self):
# 		self.path = []

# 	def draw_active_cell(self):
# 		mouse_pos = pygame.mouse.get_pos()
# 		row =  mouse_pos[1] // 32
# 		col =  mouse_pos[0] // 32
# 		current_cell_value = self.matrix[row][col]
# 		if current_cell_value == 1:
# 			rect = pygame.Rect((col * 32,row * 32),(32,32))
# 			screen.blit(self.select_surf,rect)

# 	def create_path(self):

# 		# start
# 		start_x, start_y = self.roomba.sprite.get_coord()
# 		start = self.grid.node(start_x,start_y)

# 		# end
# 		mouse_pos = pygame.mouse.get_pos()
# 		end_x,end_y =  mouse_pos[0] // 32, mouse_pos[1] // 32  
# 		end = self.grid.node(end_x,end_y) 

# 		# path
# 		finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
# 		self.path,_ = finder.find_path(start,end,self.grid)
# 		self.grid.cleanup()
# 		self.roomba.sprite.set_path(self.path)

# 	def draw_path(self):
# 		if self.path:
# 			points = []
# 			for point in self.path:
# 				x = (point[0] * 32) + 16
# 				y = (point[1] * 32) + 16
# 				points.append((x,y))

# 			pygame.draw.lines(screen,'#4a4a4a',False,points,5)

# 	def update(self):
# 		self.draw_active_cell()
# 		self.draw_path()

# 		# roomba updating and drawing
# 		self.roomba.update()
# 		self.roomba.draw(screen)

# class Roomba(pygame.sprite.Sprite):
# 	def __init__(self,empty_path):

# 		# basic
# 		super().__init__()
# 		self.image = pygame.image.load('./assets/roomba.png').convert_alpha()
# 		self.rect = self.image.get_rect(center = (60,60))

# 		# movement 
# 		self.pos = self.rect.center
# 		self.speed = 3
# 		self.direction = pygame.math.Vector2(0,0)

# 		# path
# 		self.path = []
# 		self.collision_rects = []
# 		self.empty_path = empty_path

# 	def get_coord(self):
# 		col = self.rect.centerx // 32
# 		row = self.rect.centery // 32
# 		return (col,row)

# 	def set_path(self,path):
# 		self.path = path
# 		self.create_collision_rects()
# 		self.get_direction()

# 	def create_collision_rects(self):
# 		if self.path:
# 			self.collision_rects = []
# 			for point in self.path:
# 				x = (point[0] * 32) + 16
# 				y = (point[1] * 32) + 16
# 				rect = pygame.Rect((x - 2,y - 2),(4,4))
# 				self.collision_rects.append(rect)

# 	def get_direction(self):
# 		if self.collision_rects:
# 			start = pygame.math.Vector2(self.pos)
# 			end = pygame.math.Vector2(self.collision_rects[0].center)
# 			self.direction = (end - start).normalize()
# 		else:
# 			self.direction = pygame.math.Vector2(0,0)
# 			self.path = []

# 	def check_collisions(self):
# 		if self.collision_rects:
# 			for rect in self.collision_rects:
# 				if rect.collidepoint(self.pos):
# 					del self.collision_rects[0]
# 					self.get_direction()
# 		else:
# 			self.empty_path()

# 	def update(self):
# 		self.pos += self.direction * self.speed
# 		self.check_collisions()
# 		self.rect.center = self.pos

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
matrix = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0],
	[0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0],
	[0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# pathfinder = Pathfinder(matrix)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# if event.type == pygame.MOUSEBUTTONDOWN:
		# 	pathfinder.create_path()

	screen.blit(bg_surf,(0,0))
	# pathfinder.update()

	for p in piezas:
		if p.tipo == "ventana" and p.color == pygame.Color("yellow"):
			p.tipo = "bloque"
		p.dibujar(screen)

	pygame.display.update()
	clock.tick(60)
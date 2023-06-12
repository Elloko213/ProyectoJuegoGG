import pygame

class Galleta:
    def __init__(self, peso, beneficio):
        self.peso = peso
        self.beneficio = beneficio

class Mochila:
    def __init__(self, peso_maximo, galletas):
        self.peso_maximo = peso_maximo
        self.galletas = galletas
        self.tabla = [[-1] * (peso_maximo + 1) for _ in range(len(galletas) + 1)]

    def resolver_mochila(self):
        for i in range(len(self.galletas) + 1):
            for j in range(self.peso_maximo + 1):
                if i == 0 or j == 0:
                    self.tabla[i][j] = 0
                elif self.galletas[i-1].peso <= j:
                    self.tabla[i][j] = max(
                        self.galletas[i-1].beneficio + self.tabla[i-1][j-self.galletas[i-1].peso],
                        self.tabla[i-1][j]
                    )
                else:
                    self.tabla[i][j] = self.tabla[i-1][j]

    def obtener_configuracion_optima(self):
        i = len(self.galletas)
        j = self.peso_maximo
        configuracion_optima = []
        while i > 0 and j > 0:
            if self.galletas[i-1].peso <= j and self.tabla[i][j] != self.tabla[i-1][j]:
                configuracion_optima.append(self.galletas[i-1])
                j -= self.galletas[i-1].peso
            i -= 1
        return configuracion_optima[::-1]

# Crear galletas del juego
galletas = [
    Galleta(1, 10),
    Galleta(2, 20),
    Galleta(3, 30),
    Galleta(4, 40),
    Galleta(5, 50)
]

# Crear una mochila de ejemplo
mochila = Mochila(8, galletas)

# Resolver el problema de la mochila utilizando programación dinámica
mochila.resolver_mochila()

# Obtener la configuración óptima de la mochila
configuracion_optima = mochila.obtener_configuracion_optima()

# Mostrar la configuración óptima en la consola
for galleta in configuracion_optima:
    print(f"Galleta: Peso={galleta.peso}, Beneficio={galleta.beneficio}")

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la mochila con galletas")

# Resto de la lógica del juego y la visualización de las galletas en la ventana de Pygame
# ...


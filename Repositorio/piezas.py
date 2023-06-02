import pygame

# Definición de colores
blanco = pygame.Color("white")

class Pieza:
    def __init__(self, tipo, color, figura):
        self.tipo = tipo
        self.color = color
        self.figura = figura
    
    def dibujar(self, ventana):
        if self.figura:
            self.figura.dibujar(ventana, self.color)
    
    def cambiar_color(self, color):
        self.color = color

    def cambiar_tipo(self, tipo):
        self.tipo = tipo

class Figura:
    def __init__(self, forma, posicion, dimensiones):
        self.forma = forma
        self.posicion = posicion
        self.dimensiones = dimensiones
    
    def dibujar(self, ventana, color):
        if self.forma == "rectangulo":
            pygame.draw.rect(ventana, color, pygame.Rect(self.posicion, self.dimensiones))
        elif self.forma == "circulo":
            pygame.draw.circle(ventana, color, self.posicion, self.dimensiones[0])
        elif self.forma == "triangulo":
            puntos = [(self.posicion[0] - self.dimensiones[0], self.posicion[1] + self.dimensiones[1]),
                      (self.posicion[0] + self.dimensiones[0], self.posicion[1] + self.dimensiones[1]),
                      (self.posicion[0], self.posicion[1] - self.dimensiones[1])]
            pygame.draw.polygon(ventana, color, puntos)

def pieza(tipo, color, figura):
    if tipo not in ["bloque","ventana","puerta"]:
        raise ValueError("El tipo de pieza no es válido")
    return Pieza(tipo, color, figura)
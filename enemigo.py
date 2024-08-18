import pygame

class Enemigo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 75 
        self.alto = 75
        self.velocidad = 5
        self.color = "purple"
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.ancho)
        
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)
        self.rect = pygame.Rect(self.x, self.y, self.alto, self.ancho)
        
    def movimiento(self):
        self.y += self.velocidad
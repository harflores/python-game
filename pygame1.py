import pygame
from personaje import Cubo

#DEFINIR CONSTANTES
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO,ALTO])

#DEFINIMOS EL ESTADO DE NUESTRO JUEGO
jugando = True
#DEFINIMOS LA POSICION DE NUESTRO PERSONAJE
cubo = Cubo(100,100)


#GESTIONAR TECLAS PRESIONADAS
def gestionar_teclas(teclas):
    if teclas[pygame.K_w]:
        cubo.y -=cubo.velocidad
    if teclas[pygame.K_s]:
        cubo.y +=cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -=cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x +=cubo.velocidad

while jugando:
    eventos = pygame.event.get()
    teclas = pygame.key.get_pressed()
    
    gestionar_teclas(teclas)
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("white")
    cubo.dibujar(VENTANA)
    pygame.display.update()
    

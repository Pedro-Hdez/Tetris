
import pygame
from constantes import *

#ESTA FUNCIÓN BUSCA LA ALTURA MÁXIMA QUE ABARCAN TODAS LAS PIEZAS AL MOMENTO DE RECORRERLAS HACIA ABAJO CUANDO SE LLENA UNA FILA
def ajustarAltura():
    for i in juego.zonasColision:
        if i[1] < juego.altura_max:
            juego.altura_max = i[1] #i[i]?????

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Esta función cambia de posición la pieza mediante una animación: Primero se borra la pieza actual y después se dibuja...
#...en otra posición de la cuadrícula.
def moverPieza(pieza, direccion):
    pieza.borrarPieza()

    if direccion == "IZQ":
        for i in range(0, 4):
            cuadro = pygame.Rect(pieza.componentes()[i].left - (juego.tamañoCuadro + 1), pieza.componentes()[i].top,juego.tamañoComponente, juego.tamañoComponente)
            pygame.draw.rect(juego.ventana, pieza.componentes()[4], cuadro, 0)

    elif direccion == "DER":
        for i in range(0, 4):
            cuadro = pygame.Rect(pieza.componentes()[i].left + (juego.tamañoCuadro + 1), pieza.componentes()[i].top, juego.tamañoComponente, juego.tamañoComponente)
            pygame.draw.rect(juego.ventana, pieza.componentes()[4], cuadro, 0)

    elif direccion == "ABAJO":
        for i in range(0, 4):
            cuadro = pygame.Rect(pieza.componentes()[i].left, pieza.componentes()[i].top + (juego.tamañoCuadro + 1), juego.tamañoComponente, juego.tamañoComponente)
            pygame.draw.rect(juego.ventana, pieza.componentes()[4], cuadro, 0)

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Esta función se encarga de rotar una pieza
def rotarPieza(pieza):
    pieza.borrarPieza()
    pieza.ajustarRotacion()
    pieza.dibujar()

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Esta es la animación de la caída de la pieza
def caidaPieza(pieza):
    moverPieza(pieza, "ABAJO")
    pieza.ajustarPosicion("abajo")

#---------------------------------------------------------------------------------------------------------------------------------------------------

#ESTA FUNCIÓN RECORRE UNA FILA HACIA ABAJO CUANDO DEBE ELIMINARSE OTRA
def recorrerPiezas(origen):
    for i in range(3, 311, (juego.tamañoCuadro + 1)): #Se recorre toda la pantalla horizontalmente de izquierda a derecha
        '''Se recorre toda la pantalla vericalmente desde la fila que se eliminará hasta la fila que abarca todas
           las piezas existentes en el tablero'''
        for j in range (origen, juego.altura_max-(juego.tamañoCuadro + 1), -(juego.tamañoCuadro + 1)):
            color = juego.ventana.get_at((i, j-(juego.tamañoCuadro + 1)))[:3] #Se obtiene el color del cuadro que está arriba del cuadro j
            cuadro = pygame.Rect(i, j, 27,27) #Se crea un cuadro que servirá para llenar el hueco
            '''Si arriba del cuadro (i,j) no hay nada, entonces este lugar quedará vacío, por lo tanto, este cuadro
               se remueve de las zonas de colisión y se agrega a la zona limpia'''
            if color == (50,50,50) and cuadro in juego.zonasColision:
                juego.zonasColision.remove(cuadro)
                juego.zonaLimpia.append(cuadro)
            #Si el cuadro (i,j) es una posición vacía, pero arriba de éste hay un cuadro perteneciente a otra pieza,
            #entonces el cuadro (i,j) será ocupado cuando se de el ajuste; por lo tanto, se agrega a las zonas de colisión y 
            #se saca de la zona limpia

            elif color != (50,50,50) and not cuadro in juego.zonasColision:
                juego.zonasColision.append(cuadro)
                juego.zonaLimpia.remove(cuadro)
            pygame.draw.rect(juego.ventana, color, cuadro, 0)#Se rellena el cuadro (i,j)
    ajustarAltura()  # Se busca una nueva altura máxima.
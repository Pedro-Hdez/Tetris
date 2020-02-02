import pygame
from variablesJuego import *

pygame.font.init()
fuente = pygame.font.Font('DESIB___.ttf', 25)

juego = Variables()

#---------------------------------------------CONSTANTES----------------------------------------------------------
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()


#-----------------------------------------------SONIDOS DEL JUEGO------------------------------------------------------
sonidoFilas = pygame.mixer.Sound("bloop.wav") #Sonido al completar una fila
rotacion = pygame.mixer.Sound("rotacion.wav") #Sonido al rotar una pieza
encajar = pygame.mixer.Sound("encajado.wav") #Sonido al encajar una pieza
gameover = pygame.mixer.Sound("gameover.wav") #Sonido al encajar una pieza
tetris = pygame.mixer.Sound("4combo.wav") #Sonido al completar 4 filas!

#--------------------------------------------ENUMERACIONES----------------------------------------------------------

#Nombre de los colores de las piezas
nombresColores = ["AQUA", "AZUL", "NARANJA", "AMARILLO", "VERDE", "MORADO", "ROJO"] 

#Colores del juego en RGB
rgbColores = {"AQUA": (0, 255, 255), "AZUL": (0, 0, 255), "NARANJA": (255, 140, 0), "AMARILLO": (255, 255, 0),
              "VERDE": (0, 255, 0),
              "MORADO": (138, 43, 226), "ROJO": (255, 0, 0)} #Código RGB de los colores de las piezas

#Nombre de las piezas
nombresPiezas=["linea", "t", "LIzq", "LDer", "ZIzq", "ZDer", "cuadro"]

#Posición inicial de los 4 cuadros que conforman una pieza
piezas = {"linea":[(96, -28), (127, -28), (158, -28), (189, -28)], "t":[(96, -59), (127, -59), (158, -59), (127, -28)], "LIzq":[(127, -59), (158, -59), (189, -59), (189, -28)],
          "LDer":[(96, -59), (127, -59), (158, -59), (96, -28)], "ZIzq":[(127, -59), (158, -59), (158, -28), (189, -28)], "ZDer":[(96, -28), (127, -28), (127, -59), (158, -59)],
          "cuadro":[(127, -59), (158, -59), (127, -28), (158, -28)]}

#siguientes
siguientes = {"linea":[(350,90), (373, 90), (396, 90), (419, 90)], 
              "t":[(360, 80), (383, 80), (406, 80), (383, 103)], 
              "LIzq":[(360, 80), (383, 80), (406, 80), (406, 103)],
              "LDer":[(360, 80), (383, 80), (406, 80), (360, 103)], 
              "ZIzq":[(360, 80), (383, 80), (383, 103), (406, 103)], 
              "ZDer":[(360, 103), (383, 103), (383, 80), (406, 80)],
              "cuadro":[(373, 80), (396, 80), (373, 103), (396, 103)]}

puntuacion = { "0":[40, 100, 300, 1200],
               "1":[80, 200, 600, 2400],
               "2":[120, 300, 900, 3500],
               "3":[160, 400, 1200, 4800],
               "4":[200, 500, 1500, 6000],
               "5":[240, 600, 1800, 7200],
               "6":[280, 700, 2100, 8400],
               "7":[320, 800, 2400, 9600],
               "8":[360, 900, 2700, 10800],
               "9":[400, 1000, 3000, 12000],
               "10:":[440, 1100, 3300, 13200] }
velocidad = {"1":.45,
             "2":.35,
             "3":.25,
             "4":.20,
             "5":.15,
             "6":.12,
             "7":.1,
             "8":.1,
             "9":.1,
             "10":.05}

import pygame

class Variables():
    def __init__(self):
        self.delta = 3
        self.tamañoCuadro = 30 #Tamaño del cuadro de la cuadrícula
        self.tamañoComponente = self.tamañoCuadro - self.delta #Tamaño de los cuadros que forman las piezas (deben ser mas chicos que los cuadros para que la animación se vea bien)

        self.tamañoVentanaJuego = (311, 621) #Tamaño de la ventana (cuadrícula) en donde se jugará
        self.tamañoVentanaCompleta = (655,621)
        self.ventana = pygame.display.set_mode(self.tamañoVentanaCompleta) #Se crea una ventana

        self.limIzqPantalla = self.delta #Limite izquierdo de la cuadrícula
        self.limDerPantalla = 309 #Límite derecho de la cuadrícula
        self.limInfPantalla = 619 #Límite inferior de la cuadrícula
        self.zonasColision = [] #Arreglo que guarda todas las zonas en donde puede existir una colisión entre piezas
        self.zonaLimpia = []

        self.altura_max = self.limInfPantalla

        self.nivel = 0
        self.velocidad = .65
        self.velocidad_doble = .05
        self.velocidad_aux = self.velocidad
        self.acelerar = False



        self.puntos = 0
        self.lineas = 0
        self.contador_lineas_nivel = 0

        self.x_titulo_siguiente = 323
        self.y_titulo_siguiente = 5

        self.x_cuadro_siguiente = 320
        self.y_cuadro_siguiente = 35

        self.x_titulo_puntos = 430
        self.y_titulo_puntos = 250

        self.x_cuadro_marcador = 320
        self.y_cuadro_marcador = 280

        self.x_puntos = 327
        self.y_puntos = 290
        self.x_lineas = 327 
        self.y_lineas = 340

        self.x_titulo_nivel = 345
        self.y_titulo_nivel = 500

        self.x_cuadro_nivel = 324
        self.y_cuadro_nivel = 530

        self.x_nivel_normal = 360
        self.y_nivel_normal = 535

        self.x_nivel_diez = 345
        self.y_nivel_diez = 535

        self.tamañoSiguiente = 20

        self.x_ventana_gameover = 0
        self.y_ventana_gameover = 141

        self.x_texto_gameover = 8
        self.y_texto_gameover = 143

        self.color_ventana_gameover = (0, 0, 0)

        self.alto_ventana_gameover = 250
        self.ancho_ventana_gameover = 311

        self.x_continuar = 70
        self.y_continuar = 250
        
        self.x_salir = 125
        self.y_salir = 310

        self.opcion_gameover = 'reintentar'

        self.color_opcion = (113, 223, 33)

    def Reiniciar(self):
        self.delta = 3
        self.tamañoCuadro = 30 #Tamaño del cuadro de la cuadrícula
        self.tamañoComponente = self.tamañoCuadro - self.delta #Tamaño de los cuadros que forman las piezas (deben ser mas chicos que los cuadros para que la animación se vea bien)

        self.tamañoVentanaJuego = (311, 621) #Tamaño de la ventana (cuadrícula) en donde se jugará
        self.tamañoVentanaCompleta = (655,621)
        self.ventana = pygame.display.set_mode(self.tamañoVentanaCompleta) #Se crea una ventana

        self.limIzqPantalla = self.delta #Limite izquierdo de la cuadrícula
        self.limDerPantalla = 309 #Límite derecho de la cuadrícula
        self.limInfPantalla = 619 #Límite inferior de la cuadrícula
        self.zonasColision = [] #Arreglo que guarda todas las zonas en donde puede existir una colisión entre piezas
        self.zonaLimpia = []

        self.altura_max = self.limInfPantalla

        self.nivel = 0
        self.velocidad = .65
        self.velocidad_doble = .05
        self.velocidad_aux = self.velocidad
        self.acelerar = False



        self.puntos = 0
        self.lineas = 0
        self.contador_lineas_nivel = 0

        self.x_titulo_siguiente = 323
        self.y_titulo_siguiente = 5

        self.x_cuadro_siguiente = 320
        self.y_cuadro_siguiente = 35

        self.x_titulo_puntos = 430
        self.y_titulo_puntos = 250

        self.x_cuadro_marcador = 320
        self.y_cuadro_marcador = 280

        self.x_puntos = 327
        self.y_puntos = 290
        self.x_lineas = 327 
        self.y_lineas = 340

        self.x_titulo_nivel = 345
        self.y_titulo_nivel = 500

        self.x_cuadro_nivel = 324
        self.y_cuadro_nivel = 530

        self.x_nivel_normal = 360
        self.y_nivel_normal = 535

        self.x_nivel_diez = 345
        self.y_nivel_diez = 535

        self.tamañoSiguiente = 20

        self.x_ventana_gameover = 0
        self.y_ventana_gameover = 141

        self.x_texto_gameover = 8
        self.y_texto_gameover = 143

        self.color_ventana_gameover = (0, 0, 0)

        self.alto_ventana_gameover = 250
        self.ancho_ventana_gameover = 311

        self.x_continuar = 70
        self.y_continuar = 250
        
        self.x_salir = 125
        self.y_salir = 310

        self.opcion_gameover = 'reintentar'

        self.color_opcion = (113, 223, 33)

    

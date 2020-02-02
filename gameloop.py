import pygame
from funcionesMovimiento import *
from funciones_AjustePartida import *
from pieza import *
from pygame.locals import *
from time import *
from constantes import *

import sys

def jugar():

    juego.Reiniciar()
    aux = 0 #Variable auxiliar que nos ayudará a repetir ciertos eventos en un determinado lapso de tiempo

    #--------------------------------------------------JUEGO-------------------------------------------------------------
    #Se dibuja la cuadrícula
    dibujarCuadricula()

    #Se construye la primer pieza del juego
    posPieza = []
    piezaNueva(posPieza, nombresPiezas[randint(0,6)])
    pieza = Piezas(posPieza[4], posPieza[0], posPieza[1], posPieza[2], posPieza[3], seleccionarColor(), posPieza[5])

    #Se construye la primer pieza siguiente
    siguiente = generarSiguientePieza()


    #Se inicializa la música de fondo
    pygame.mixer_music.load("Tetris.wav")
    pygame.mixer_music.set_volume(.6)
    pygame.mixer_music.play(-1)
    #--------------------------------------------------GAMELOOP------------------------------------------------------------
    game = True
    dibujaMarcadores()
    dibujaSiguiente(siguiente)
    while True:
        while game:

            if juego.acelerar:
                juego.velocidad = .05
            elif juego.velocidad != 0:
                juego.velocidad = juego.velocidad_aux

            # ----ESTE BLOQUE CREA UNA NUEVA PIEZA CUANDO LA PIEZA ACTUAL YA NO PUEDE SEGUIR CAYENDO-------------------------
            if pieza.limite("abajo") == juego.limInfPantalla and b-aux > .2:
                juego.velocidad = juego.velocidad_aux
                crearColision(pieza) #Se crea una nueva zona de colisión
                buscarAltura(pieza.componentes())  # Se busca una nueva altura
                filaCompleta(pieza.componentes()) #Se revisa si se completó una fila
                posPieza.clear()#Se 'destruye' la pieza encajada

                piezaNueva(posPieza, siguiente[0]) #Se inicializan los valores de una nueva pieza
                pieza = Piezas(posPieza[4], posPieza[0], posPieza[1], posPieza[2], posPieza[3], siguiente[1], posPieza[5]) #Se crea una pieza nueva

                siguiente = generarSiguientePieza()#Se crea una pieza siguiente
                dibujaSiguiente(siguiente) #Se dibuja la pieza siguiente
                aux = b #Se ajusta la variable auxiliar para el tiempo de espera cuando se encaja una pieza


            #Este bloque ejecuta la animación de la caída cada .75 segundos mientras no se llegue al límite inferior del frame
            b = perf_counter()
            if (b - aux > juego.velocidad) and (pieza.limite("abajo") < juego.limInfPantalla):
                if not Colision(pieza, "abajo"): #Si no hay colisión abajo de la pieza, ésta sigue cayendo
                    caidaPieza(pieza)
                elif Colision(pieza, "abajo"): #Si se da una colisión, entonces se crea otra pieza
                    juego.velocidad = juego.velocidad_aux
                    
                    crearColision(pieza) #Se crea una nueva zona de colisión con la pieza
                    #Se revisa si la pieza sigue dentro del área de juego, si la pantalla ya está llena, entonces el juego se termina
                    for i in pieza.componentes()[1:4]: 
                        if i.y <= 3:
                            game = False 
                    buscarAltura(pieza.componentes())  # Buscas una nueva altura
                    filaCompleta(pieza.componentes()) #Se revisa si se completó alguna fila
                    posPieza.clear()#Se 'destruye' la pieza encajada

                    piezaNueva(posPieza, siguiente[0]) #Se inicializan los valores de una nueva pieza
                    pieza = Piezas(posPieza[4], posPieza[0], posPieza[1], posPieza[2], posPieza[3], siguiente[1], posPieza[5]) #Se crea una pieza nueva

                    siguiente = generarSiguientePieza()#Se crea una pieza siguiente
                    dibujaSiguiente(siguiente) #Se dibuja la pieza siguiente
                
                aux = b #Se ajusta la variable auxiliar para la animación de caída

            #---------------------------------------------------------------------------------------------------------------
            
            #Se checan los eventos
            for event in pygame.event.get():
                #Bloque que cierra la aplicación cuando el usuario cierra la ventana
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                #******ESTE BLOQUE DECIDE HACIA DONDE MOVER LA PIEZA EN CASO DE QUE SE PULSE ALGUNA FLECHA DEL TECLADO*********
                        #Mientras no se llegue al límite, entonces se mueve la pieza a alguna dirección y se ajustan sus...
                        #...componentes
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        if pieza.limite("izq") > juego.limIzqPantalla and not Colision(pieza, "izq"):
                            moverPieza(pieza, "IZQ")
                            pieza.ajustarPosicion("izq")

                    elif event.key == K_RIGHT:
                        if pieza.limite("der") < juego.limDerPantalla and not Colision(pieza, "der"):
                            moverPieza(pieza, "DER")
                            pieza.ajustarPosicion("der")

                    elif event.key == K_DOWN:
                        if pieza.limite("abajo") < juego.limInfPantalla and not Colision(pieza, "abajo"):
                            juego.velocidad_aux = juego.velocidad
                            juego.acelerar = True
                            moverPieza(pieza, "ABAJO")
                            pieza.ajustarPosicion("abajo")

                    elif event.key == K_z:# and pieza.limite("abajo") < juego.limInfPantalla:
                        rotacion.play()
                        if not pieza.tipoPieza() == "cuadro":
                            rotarPieza(pieza)

                    elif event.key == K_x:
                        juego.velocidad = 0

                elif event.type == pygame.KEYUP:
                    if event.key == K_DOWN:
                        juego.acelerar = False
                #**************************************************************************************************************
            pygame.display.update()
        break

    del posPieza, pieza, siguiente, game, b, aux
    #Suena la música de game over
    pygame.mixer_music.stop()
    pygame.mixer_music.load("gameover.wav")
    pygame.mixer_music.set_volume(.6)
    pygame.mixer_music.play()

    pygame.time.wait(3000)

    MostrarGameover()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN or event.key == pygame.K_UP:
                    if juego.opcion_gameover == 'reintentar':
                        EscogerOpcion('salir')
                    elif juego.opcion_gameover == 'salir':
                        EscogerOpcion('reintentar')
                elif event.key == K_RETURN:
                    if juego.opcion_gameover == 'reintentar': jugar()
                    elif juego.opcion_gameover == 'salir': exit()
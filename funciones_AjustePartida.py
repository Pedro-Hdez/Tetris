import pygame
from constantes import *
from random import randint
from funcionesMovimiento import *

pygame.display.set_caption("TETRIS") #Se le asigna un título a la ventana

#Esta función dibuja la cuadrícula sobre la cuál jugaremos
def dibujarCuadricula():
    juego.ventana.fill((0, 0, 0))
    for i in range(1, juego.tamañoVentanaJuego[0], juego.tamañoCuadro + 1):
        for j in range(1, juego.tamañoVentanaJuego[1], juego.tamañoCuadro + 1):
            juego.zonaLimpia.append(pygame.Rect(i + 2, j + 2, juego.tamañoComponente, juego.tamañoComponente)) #Se llena los cuadros de la zona limpia
            pygame.draw.rect(juego.ventana, (50, 50, 50), [i, j, juego.tamañoCuadro, juego.tamañoCuadro], 0)

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Esta función dibuja la cuadrícula sobre la cuál jugaremos
def dibujaMarcadores():
    fuente = pygame.font.Font('DESIB___.ttf', 22)
    texto = fuente.render('PIEZA SIGUIENTE', False,(255, 255, 255))
    juego.ventana.blit(texto,(juego.x_titulo_siguiente, juego.y_titulo_siguiente))

    pygame.draw.polygon(juego.ventana, 
                        (255, 255, 255), 
                        [(juego.x_cuadro_siguiente, juego.y_cuadro_siguiente),
                            (juego.x_cuadro_siguiente + 150, juego.y_cuadro_siguiente),
                            (juego.x_cuadro_siguiente + 150, juego.y_cuadro_siguiente + 130),
                            (juego.x_cuadro_siguiente, juego.y_cuadro_siguiente + 130)],
                            1)    
    
    fuente = pygame.font.Font('DESIB___.ttf', 25)
    texto = fuente.render('MARCADOR', False,(255, 255, 255))
    juego.ventana.blit(texto,(juego.x_titulo_puntos,juego.y_titulo_puntos))

    texto = fuente.render('Puntos: 0', False,(255, 255, 255))
    juego.ventana.blit(texto,(juego.x_puntos,juego.y_puntos))

    texto = fuente.render('Lineas completadas: 0', False, (255, 255, 255))
    juego.ventana.blit(texto,(juego.x_lineas,juego.y_lineas))

    pygame.draw.polygon(juego.ventana, 
                        (255, 255, 255), 
                        [(juego.x_cuadro_marcador, juego.y_cuadro_marcador),
                        (juego.x_cuadro_marcador + 330, juego.y_cuadro_marcador),
                        (juego.x_cuadro_marcador + 330, juego.y_cuadro_marcador + 100),
                        (juego.x_cuadro_marcador, juego.y_cuadro_marcador + 100)],
                        1)    
    
    texto = fuente.render('NIVEL', False, (255, 255, 255))
    juego.ventana.blit(texto,(juego.x_titulo_nivel,juego.y_titulo_nivel))

    pygame.draw.polygon(juego.ventana, 
                        (255, 255, 255), 
                        [(juego.x_cuadro_nivel, juego.y_cuadro_nivel),
                        (juego.x_cuadro_nivel + 100, juego.y_cuadro_nivel),
                        (juego.x_cuadro_nivel + 100, juego.y_cuadro_nivel + 90),
                        (juego.x_cuadro_nivel, juego.y_cuadro_nivel + 90)],
                        1)

    fuente = pygame.font.Font('DESIB___.ttf', 60)
    texto = fuente.render(str(juego.nivel), False, (255, 255, 255))
    juego.ventana.blit(texto,(juego.x_nivel_normal, juego.y_nivel_normal))
    fuente = pygame.font.Font('DESIB___.ttf', 25)
#---------------------------------------------------------------------------------------------------------------------------------------------------
def dibujaSiguiente(pieza):
    #Se borra la pieza anterior
    areaBorrado = pygame.Rect(juego.x_cuadro_siguiente + 1, juego.y_cuadro_siguiente + 1, 140, 120)
    pygame.draw.rect(juego.ventana, (0, 0, 0), areaBorrado, 0)

    #Se dibuja la nueva pieza
    componentes = siguientes.get(pieza[0])
    for componente in componentes:
        cuadro = pygame.Rect(componente[0], componente[1], juego.tamañoSiguiente, juego.tamañoSiguiente)
        pygame.draw.rect(juego.ventana, pieza[1], cuadro, 0)


#---------------------------------------------------------------------------------------------------------------------------------------------------
def generarSiguientePieza():
    clave = nombresPiezas[randint(0,6)]
    color = seleccionarColor()
    return(clave,color)
#---------------------------------------------------------------------------------------------------------------------------------------------------

#Esta función selecciona algún color al azar para la pieza.
def seleccionarColor():
    clave = nombresColores[randint(0, 6)]
    return rgbColores.get(clave)

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Esta función selecciona una pieza al azar para construirla.
def piezaNueva(arreglo, clave):
    arreglo += piezas.get(clave)
    arreglo.append(clave)
    arreglo.append(0)

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Esta función crea zonas de colisión y remueve los cuadros ocupados de la zona limpia
def crearColision(pieza):
    for i in range (0, 4):
        juego.zonasColision.append(pieza.componentes()[i])
        if pieza.componentes()[i].y >= 3:
            juego.zonaLimpia.remove(pieza.componentes()[i])

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Esta función detecta las colisiones entre piezas
def Colision(pieza, direccion):

    if direccion == "abajo":
        for i in range (0, 4):
            if pygame.Rect(pieza.componentes()[i][0], pieza.componentes()[i][1]+(juego.tamañoCuadro + 1), 27, 27) in juego.zonasColision:
                #encajar.play()
                return True
    elif direccion == "izq":
        for i in range (0, 4):
            if pygame.Rect(pieza.componentes()[i][0]-(juego.tamañoCuadro + 1), pieza.componentes()[i][1], 27, 27) in juego.zonasColision:
                encajar.play()
                return True
    elif direccion =="der":
        for i in range (0, 4):
            if pygame.Rect(pieza.componentes()[i][0]+(juego.tamañoCuadro + 1), pieza.componentes()[i][1], 27, 27) in juego.zonasColision:
                encajar.play()
                return True
    else:
        for i in range (0, 4):
            if pygame.Rect(pieza.componentes()[i][0], pieza.componentes()[i][1]-(juego.tamañoCuadro + 1), 27, 27) in juego.zonasColision:
                encajar.play()
                return True
    return False

#---------------------------------------------------------------------------------------------------------------------------------------------------

def actualizarMarcador(filasCompletas):
    fuente = pygame.font.Font('DESIB___.ttf', 25)
    texto = fuente.render('Puntos: %i'%(juego.puntos), False, (0, 0, 0))
    juego.ventana.blit(texto,(juego.x_puntos,juego.y_puntos))

    texto = fuente.render('Lineas completadas: %i'%(juego.lineas), False, (0, 0, 0))
    juego.ventana.blit(texto,(juego.x_lineas,juego.y_lineas))

    juego.puntos += puntuacion.get( str( juego.nivel ) )[filasCompletas-1]

    juego.lineas += filasCompletas
    juego.contador_lineas_nivel += filasCompletas


    if juego.nivel < 10 and juego.contador_lineas_nivel >= 10:
        fuente = pygame.font.Font('DESIB___.ttf', 60)
        texto = fuente.render(str(juego.nivel), False, (0, 0, 0))
        juego.ventana.blit(texto,(juego.x_nivel_normal, juego.y_nivel_normal))

        juego.nivel += 1
        juego.velocidad = juego.velocidad_aux = velocidad.get(str(juego.nivel))

        texto = fuente.render(str(juego.nivel), False, (255, 255, 255))
        juego.ventana.blit(texto,(juego.x_nivel_normal, juego.y_nivel_normal))
        fuente = pygame.font.Font('DESIB___.ttf', 25)
        juego.contador_lineas_nivel -= 10
        print("FIlas completas: %d"%(juego.contador_lineas_nivel))

    texto = fuente.render('Puntos: %i'%(juego.puntos), False, (255, 255, 255))
    juego.ventana.blit(texto,(juego.x_puntos,juego.y_puntos))
    texto = fuente.render('Líneas completadas: %i'%(juego.lineas), False, (255, 255, 255))
    juego.ventana.blit(texto,(juego.x_lineas, juego.y_lineas))

#---------------------------------------------------------------------------------------------------------------------------------------------------

def animacionTetris():
    cuadros_piezas = []
    for i in juego.zonasColision:
        cuadros_piezas.append( ( i, juego.ventana.get_at( (i.left, i.top) ) )[:3] )

    for _ in range (0,2):
        for i in juego.zonaLimpia:
            pygame.draw.rect(juego.ventana, (randint(200, 255),randint(200, 255), randint(200, 255)), i)
        for i in cuadros_piezas:
            pygame.draw.rect(juego.ventana, (randint(0, 100), randint(0, 100), randint(0, 100)), i[0])

        pygame.display.flip()
        pygame.time.wait(90)

        for i in juego.zonaLimpia:
            pygame.draw.rect(juego.ventana, (50,50,50), i)
        for i in cuadros_piezas:
            pygame.draw.rect(juego.ventana, i[1], i[0])
        pygame.display.flip()
        pygame.time.wait(90)
    pygame.time.wait(150)
    
    del cuadros_piezas[:]
    del cuadros_piezas



#ESTA FUNCIÓN REVISA SI ALGUNA FILA SE COMPLETÓ
def filaCompleta(compPieza):
    combo_4 = False
    filasCompletas = [] #En este arreglo se guardan las filas que se pudieron completar
    contadorMatches = int #Este contador nos ayudará a saber si una fila está completamente llena

    for i in range (0,4): #Se recorrerán todas las componentes de la pieza que acabamos de encajar
        col = compPieza[i][1] #Se extrae la columna (altura) en donde se encuentra la componente 'i'
        contadorMatches = 0 #El contador de matches se hace cero

        for j in range (3, 311, (juego.tamañoCuadro + 1)): #Se recorre toda la pantalla horizontalmente en esa misma columna (col)
            rect = pygame.Rect(j,col,27,27) #Se crea un rectángulo para buscar un match con los cuadros que se encuentran en la zona de colisión
            if rect in juego.zonasColision: #Si hay un match, el contador de éstos se incrementa en 1
                contadorMatches += 1
        if contadorMatches == 10: #Si cuando se recorre toda la pantalla hubo 10 matches, entonces esa fila se agrega a las filas completas
            '''Puede ser que dos o más componentes de la misma pieza ayuden a llenar la misma fila, por eso,
               si ya se indicó que una fila está completa, ésta no vuelve a considerarse'''
            if not col in filasCompletas:
                filasCompletas.append(col)

    #Si hay por lo menos una fila completa, entonces se procede a eliminarla y ajustar tod0 lo demás
    if len(filasCompletas) > 0:
        if len(filasCompletas) < 4: sonidoFilas.play()
        else:
            combo_4 = True
            tetris.play()
            animacionTetris()
        actualizarMarcador(len(filasCompletas)) #Se le dan los puntos al jugador
        filasCompletas.sort()
        for i in filasCompletas: #Por cada fila que se debe eliminar, se deben recorrer las piezas que están arriba de ésta
            if not combo_4:
                for j in range (3, 311, (juego.tamañoCuadro + 1)):
                    pygame.draw.rect(juego.ventana, (50,50,50), pygame.Rect(j,i,27,27))
                    pygame.display.flip()
                    pygame.time.wait(10)

            recorrerPiezas(i)
        return

    encajar.play()

#---------------------------------------------------------------------------------------------------------------------------------------------------

#ESTA FUNCIÓN BUSCA LA ALTURA MÁXIMA QUE ABARCAN TODAS LAS PIEZAS AL MOMENTO DE ENCAJAR UNA NUEVA
def buscarAltura(componentes):
    for i in range (0, 4):
        if componentes[i][1] < juego.altura_max:
            juego.altura_max = componentes[i][1]
            return

#---------------------------------------------------------------------------------------------------------------------------------------------------

def MostrarGameover():
    pygame.draw.rect(juego.ventana, juego.color_ventana_gameover, (juego.x_ventana_gameover, juego.y_ventana_gameover, juego.ancho_ventana_gameover, juego.alto_ventana_gameover), 0)

    fuente = pygame.font.Font('DESIB___.ttf', 65)
    texto = fuente.render('GAME OVER', False, (255, 255, 255))
    juego.ventana.blit(texto,(juego.x_texto_gameover,juego.y_texto_gameover))

    fuente = pygame.font.Font('DESIB___.ttf', 35)
    texto = fuente.render('Reintentar', False, juego.color_opcion)
    juego.ventana.blit(texto,(juego.x_continuar,juego.y_continuar))

    fuente = pygame.font.Font('DESIB___.ttf', 35)
    texto = fuente.render('Salir', False, (255, 255, 255))
    juego.ventana.blit(texto,(juego.x_salir,juego.y_salir))
    
    pygame.display.flip()

def EscogerOpcion(cual):
    if cual == 'reintentar':
        fuente = pygame.font.Font('DESIB___.ttf', 35)
        texto = fuente.render('Reintentar', False, juego.color_opcion)
        juego.ventana.blit(texto,(juego.x_continuar,juego.y_continuar))

        fuente = pygame.font.Font('DESIB___.ttf', 35)
        texto = fuente.render('Salir', False, (255, 255, 255))
        juego.ventana.blit(texto,(juego.x_salir,juego.y_salir))

        juego.opcion_gameover = 'reintentar'

    elif cual == 'salir':
        fuente = pygame.font.Font('DESIB___.ttf', 35)
        texto = fuente.render('Reintentar', False, (255, 255, 255))
        juego.ventana.blit(texto,(juego.x_continuar,juego.y_continuar))

        fuente = pygame.font.Font('DESIB___.ttf', 35)
        texto = fuente.render('Salir', False, juego.color_opcion)
        juego.ventana.blit(texto,(juego.x_salir,juego.y_salir))

        juego.opcion_gameover = 'salir'
    
    pygame.display.flip()

    
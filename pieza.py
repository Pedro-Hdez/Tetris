import pygame
from constantes import *
from funcionesMovimiento import *
from funciones_AjustePartida import *
class Piezas():
    def __init__(self, tipo, comp1, comp2, comp3, comp4, color, gradRot):
        #Se almacenan los valores dados en los atributos de la pieza
        self.tipo = tipo
        self.x1 = comp1[0]
        self.y1 = comp1[1]
        self.x2 = comp2[0]
        self.y2 = comp2[1]
        self.x3 = comp3[0]
        self.y3 = comp3[1]
        self.x4 = comp4[0]
        self.y4 = comp4[1]
        self.color = color
        self.gradRot = gradRot

        #Cada pieza se compone de 4 cuadros, entonces se construyen en su posición inicial
        self.cuadro1 = pygame.Rect(self.x1, self.y1, juego.tamañoComponente, juego.tamañoComponente)
        self.cuadro2 = pygame.Rect(self.x2, self.y2, juego.tamañoComponente, juego.tamañoComponente )
        self.cuadro3 = pygame.Rect(self.x3, self.y3, juego.tamañoComponente, juego.tamañoComponente)
        self.cuadro4 = pygame.Rect(self.x4, self.y4, juego.tamañoComponente, juego.tamañoComponente)

        #Los límites de las piezas están delimitados por el extremo de algún cuadro y dependen del tipo de pieza...tamañoComponent
        #..., aquí se asignan dichos valores iniciales y nos sirven para que la pieza no se salga de la pantalla

        #Límite izquierdo
        self.limIzq = self.cuadro1.left

        #Límite derecho
        if self.tipo == "t" or self.tipo == "LDer":
            self.limDer = self.cuadro3.right
        else:
            self.limDer = self.cuadro4.right
        
        #Límite inferior
        if self.tipo == "ZDer":
            self.limAbajo = self.cuadro1.bottom
        else:
            self.limAbajo = self.cuadro4.bottom

        #Para manipular las piezas necesitamos conocer a sus componentes (los 4 cuadros que la forman), entonces...
        #...se crea una lista con estos objetos
        self.cuadros = [self.cuadro1, self.cuadro2, self.cuadro3, self.cuadro4, self.color, self.gradRot]

    #Este método dibuja cada cuadrado en su posición inicial; sirve para animar el movimiento
    def dibujar(self):
        for i in range (0, 4):
            pygame.draw.rect(juego.ventana, self.color, self.cuadros[i], 0)

    # Esta método borra una pieza; sirve para animar el movimiento.
    def borrarPieza(self):
        for i in range(0, 4):
            pygame.draw.rect(juego.ventana, (50, 50, 50), self.cuadros[i], 0)

    #Este método regresa el arreglo de los cuadros que componen la pieza
    def componentes(self):
        return self.cuadros

    #Este método regresa el valor del límite actual que se le pida.
    def limite(self, lim):
        if lim == "izq":
            return self.limIzq
        elif lim == "der":
            return self.limDer
        elif lim == "abajo":
            return self.limAbajo

    #Este método ajusta la posición de cada cuadro que compone a la pieza cuando ésta se mueve. Depende de...
    #...la dirección del movimiento, del tipo de pieza y de los grados que la pieza esté rotado.
    def ajustarPosicion(self, como):
        
        #Se ajustan las posiciones de los cuadros
        if como == "izq":
            for i in range(0, 4):
                self.cuadros[i][0] -= (juego.tamañoCuadro + 1)
        elif como == "der":
            for i in range(0, 4):
                self.cuadros[i][0] += (juego.tamañoCuadro + 1)
        elif como == "abajo":
            for i in range(0, 4):
                self.cuadros[i][1] +=  (juego.tamañoCuadro + 1)

        #Se ajustan los límites 
        if self.tipo == "t" or self.tipo == "LIzq" or self.tipo == "LDer":
            if self.gradRot == 0:
                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[2].right
                self.limAbajo = self.cuadros[3].bottom

            elif self.gradRot == 90:
                self.limIzq = self.cuadros[3].left
                self.limDer = self.cuadros[1].right
                self.limAbajo = self.cuadros[2].bottom

            elif self.gradRot == 180:
                self.limIzq = self.cuadros[2].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[1].bottom

            elif self.gradRot == 270:
                self.limIzq = self.cuadros[1].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[0].bottom

        elif self.tipo == "ZIzq":
            if self.gradRot == 0:
                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[3].bottom
            elif self.gradRot == 90:
                self.limIzq = self.cuadros[2].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[3].bottom

        elif self.tipo == "ZDer":
            if self.gradRot == 0:
                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[1].bottom
            elif self.gradRot == 90:
                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[3].bottom

        elif self.tipo == "linea":
            if self.gradRot == 0:
                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[3].bottom
            elif self.gradRot == 90:
                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[3].bottom

        elif self.tipo == "cuadro":
            self.limIzq = self.cuadros[0].left
            self.limDer = self.cuadros[1].right
            self.limAbajo = self.cuadros[2].bottom

    #ESTE MÉTODO REGRESA EL TIPO DE PIEZA
    def tipoPieza(self):
        return self.tipo

    #ESTE MÉTODO AJUSTA LA POSICIÓN DE LAS COMPONENTES DE LA PIEZA CUANDO SE DA UNA ROTACIÓN.
    def ajustarRotacion(self):
        if self.tipo == "t":
            if self.gradRot == 0:
                if Colision(self,"arriba"):
                    return
                else:
                    self.cuadros[0].left += (juego.tamañoCuadro + 1)
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].top += (juego.tamañoCuadro + 1)
                    self.cuadros[3].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].top -= (juego.tamañoCuadro + 1)

                self.limIzq = self.cuadros[3].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[2].bottom

                self.gradRot += 90

            elif self.gradRot == 90:
                if self.limDer == juego.limDerPantalla or Colision(self, "der"):
                    return
                else:
                    self.cuadros[0].left += (juego.tamañoCuadro + 1)
                    self.cuadros[0].top += (juego.tamañoCuadro + 1)
                    self.cuadros[2].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].left += (juego.tamañoCuadro + 1)
                    self.cuadros[3].top -= (juego.tamañoCuadro + 1)

                self.limIzq = self.cuadros[2].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[0].bottom

                self.gradRot += 90

            elif self.gradRot == 180:
                if self.limAbajo == juego.limInfPantalla or Colision(self, "abajo"):
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[1].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1) * 2
                    self.cuadros[3].left += (juego.tamañoCuadro + 1)
                else:
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[0].top += (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].left += (juego.tamañoCuadro + 1)
                    self.cuadros[3].top += (juego.tamañoCuadro + 1)

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[0].bottom


                self.gradRot += 90

            elif self.gradRot == 270:
                if self.limIzq == juego.limIzqPantalla or Colision(self, "izq"):
                    return

                else:
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top += (juego.tamañoCuadro + 1)
                    self.cuadros[3].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].top += (juego.tamañoCuadro + 1)

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[2].right
                self.limAbajo = self.cuadros[3].bottom

                self.gradRot -= 270

        elif self.tipo == "LIzq":
            if self.gradRot == 0:
                if Colision(self,"arriba"):
                    return
                else:
                    self.cuadros[0].left += (juego.tamañoCuadro + 1)
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].top += (juego.tamañoCuadro + 1)
                    self.cuadros[3].left -= (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[3].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[2].bottom

                self.gradRot += 90

            elif self.gradRot == 90:
                if self.limDer == juego.limDerPantalla or Colision(self, "der"):
                    return
                else:
                    self.cuadros[0].left += (juego.tamañoCuadro + 1)
                    self.cuadros[0].top += (juego.tamañoCuadro + 1)
                    self.cuadros[2].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].top -= (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[2].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[0].bottom

                self.gradRot += 90

            elif self.gradRot == 180:
                if self.limAbajo == juego.limInfPantalla or Colision(self,"abajo"):
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[1].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1) * 2
                    self.cuadros[3].left += (juego.tamañoCuadro + 1) * 2
                    self.cuadros[3].top -= (juego.tamañoCuadro + 1)
                else:
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[0].top += (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].left += (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[0].bottom


                self.gradRot += 90

            elif self.gradRot == 270:
                if self.limIzq == juego.limIzqPantalla or Colision(self, "izq"):
                    return
                else:
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top += (juego.tamañoCuadro + 1)
                    self.cuadros[3].top += (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[2].right
                self.limAbajo = self.cuadros[3].bottom

                self.gradRot -= 270

        elif self.tipo == "LDer":
            if self.gradRot == 0:
                if Colision(self,"arriba"):
                    return
                else:
                    self.cuadros[0].left += (juego.tamañoCuadro + 1)
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].top += (juego.tamañoCuadro + 1)
                    self.cuadros[3].top -=  (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[3].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[2].bottom

                self.gradRot += 90

            elif self.gradRot == 90:
                if self.limDer == juego.limDerPantalla or Colision(self, "der"):
                    return
                else:
                    self.cuadros[0].left +=  (juego.tamañoCuadro + 1)
                    self.cuadros[0].top +=  (juego.tamañoCuadro + 1)
                    self.cuadros[2].left -=  (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -=  (juego.tamañoCuadro + 1)
                    self.cuadros[3].left += (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[2].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[0].bottom

                self.gradRot += 90

            elif self.gradRot == 180:
                if self.limAbajo == juego.limInfPantalla or Colision(self,"abajo"):
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[1].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1) * 2
                    self.cuadros[3].top += (juego.tamañoCuadro + 1)
                else:
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[0].top += (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].top += (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[0].bottom


                self.gradRot += 90

            elif self.gradRot == 270:
                if self.limIzq == juego.limIzqPantalla or Colision(self, "izq"):
                    return
                else:
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top += (juego.tamañoCuadro + 1)
                    self.cuadros[3].left -= (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[2].right
                self.limAbajo = self.cuadros[3].bottom

                self.gradRot -= 270

        elif self.tipo == "ZIzq":
            if self.gradRot == 0:
                if self.limAbajo == juego.limInfPantalla or Colision(self,"abajo"):
                    self.cuadros[0].left += (juego.tamañoCuadro + 1) * 2
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[1].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].left -= (juego.tamañoCuadro + 1)
                else:
                    self.cuadros[0].left += (juego.tamañoCuadro + 1) * 2
                    self.cuadros[1].left += (juego.tamañoCuadro + 1)
                    self.cuadros[1].top += (juego.tamañoCuadro + 1)
                    self.cuadros[3].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].top += (juego.tamañoCuadro + 1)

                self.limIzq = self.cuadros[2].left
                self.limDer = self.cuadros[1].right
                self.limAbajo = self.cuadros[3].bottom

                self.gradRot += 90

            elif self.gradRot == 90:
                if self.limIzq == juego.limIzqPantalla or Colision(self, "izq"):
                    return
                else:
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1) * 2
                    self.cuadros[1].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[1].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].left += (juego.tamañoCuadro + 1)
                    self.cuadros[3].top -= (juego.tamañoCuadro + 1)

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[1].bottom

                self.gradRot -= 90

        elif self.tipo == "ZDer":
            if self.gradRot == 0:
                if self.limAbajo == juego.limInfPantalla or Colision(self,"abajo"):
                    self.cuadros[0].left += (juego.tamañoCuadro + 1)
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1) * 2
                    self.cuadros[1].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[3].top += (juego.tamañoCuadro + 1)
                else:
                    self.cuadros[0].left += (juego.tamañoCuadro + 1)
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].left += (juego.tamañoCuadro + 1)
                    self.cuadros[2].top += (juego.tamañoCuadro + 1)
                    self.cuadros[3].top += (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[3].bottom

                self.gradRot += 90

            elif self.gradRot == 90:
                if self.limIzq == juego.limIzqPantalla or Colision(self, "izq"):
                    return
                else:
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[0].top += (juego.tamañoCuadro + 1)
                    self.cuadros[2].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].top -= (juego.tamañoCuadro + 1) * 2

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[1].bottom

                self.gradRot -= 90

        elif self.tipo == "linea":
            if self.gradRot == 0:
                if self.limAbajo == juego.limInfPantalla or Colision(self,"abajo"):
                    self.cuadros[0].left += (juego.tamañoCuadro + 1) * 2
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1) * 3
                    self.cuadros[1].left += (juego.tamañoCuadro + 1)
                    self.cuadros[1].top -= (juego.tamañoCuadro + 1) * 2
                    self.cuadros[2].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].left -= (juego.tamañoCuadro + 1)
                else:
                    self.cuadros[0].left += (juego.tamañoCuadro + 1) * 2
                    self.cuadros[0].top -= (juego.tamañoCuadro + 1) * 2
                    self.cuadros[1].left += (juego.tamañoCuadro + 1)
                    self.cuadros[1].top -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[3].top += (juego.tamañoCuadro + 1)

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[0].right
                self.limAbajo = self.cuadros[3].bottom

                self.gradRot += 90

            elif self.gradRot == 90:
                if self.limIzq == juego.limIzqPantalla or Colision(self, "izq"):
                    return
                elif self.limIzq == juego.limIzqPantalla + (juego.tamañoCuadro + 1):
                    return
                elif pygame.Rect(self.cuadros[0][0]-(juego.tamañoCuadro + 1) * 2,self.cuadros[0][1],27,27) in juego.zonasColision or pygame.Rect(self.cuadros[1][0]-(juego.tamañoCuadro + 1) * 2,self.cuadros[1][1],27,27) in juego.zonasColision or pygame.Rect(self.cuadros[2][0]-(juego.tamañoCuadro + 1) * 2,self.cuadros[2][1],27,27) in juego.zonasColision:
                    return
                elif self.limDer == juego.limDerPantalla or Colision(self, "der"):
                    return
                else:
                    self.cuadros[0].left -= (juego.tamañoCuadro + 1) * 2
                    self.cuadros[0].top += (juego.tamañoCuadro + 1) * 2
                    self.cuadros[1].left -= (juego.tamañoCuadro + 1)
                    self.cuadros[1].top += (juego.tamañoCuadro + 1)
                    self.cuadros[3].left += (juego.tamañoCuadro + 1)
                    self.cuadros[3].top -= (juego.tamañoCuadro + 1)

                self.limIzq = self.cuadros[0].left
                self.limDer = self.cuadros[3].right
                self.limAbajo = self.cuadros[3].bottom

                self.gradRot -= 90

    #ESTE MÉTODO REGRESA LOS GRADOS DE ROTACIÓN DE LA PIEZA
    def gradosRotados(self):
        return self.gradRot
from Casilla import Casilla
class Tablero:

    def __init__(self):
        self.casillas = []
    
    def add_casillas(self, casillas):
        self.casillas=casillas

    def get_casillas(self):
        return self.casillas

    def definir_poisicion_color_cuadro(self, i):
        informacion = []

        if (i == 0):
            informacion.append("red")
            informacion.append(-230)
            informacion.append(440)
        elif (i == 1):
            informacion.append("blue")
            informacion.append(160)
            informacion.append(510)
        elif (i == 2):
            informacion.append("green")
            informacion.append(230)
            informacion.append(-440)
        elif (i == 3):
            informacion.append("yellow")
            informacion.append(-160)
            informacion.append(-510)

        return informacion
    
    def crearCuadro(self, turtleDraw):
        informacion = []

        for i in range(4):
            informacion = self.definir_poisicion_color_cuadro(i)

            turtleDraw.penup()
            turtleDraw.goto(informacion[1], informacion[2])
            turtleDraw.pendown()
            turtleDraw.fillcolor(informacion[0])
            turtleDraw.begin_fill()
            turtleDraw.forward(280)
            turtleDraw.right(90)
            turtleDraw.forward(280)
            turtleDraw.right(90)
            turtleDraw.forward(280)
            turtleDraw.right(90)
            turtleDraw.forward(280)
            turtleDraw.end_fill()

    def crearCasillas(self, turtleDraw):
        
        turtleDraw.shape("turtle")
        turtleDraw.speed(50)
        turtleDraw.penup()
        turtleDraw.goto(-440, -90)
        turtleDraw.pendown()
        # variable del tamaño de un ala del tablero
        # 510 (440+70)
        posicion = 440

        # Dibujar ala izquierda el tablero y derecha
        for i in range(6):
            turtleDraw.left(90)
            turtleDraw.forward(180)
            turtleDraw.left(90)
            turtleDraw.forward(70)
            turtleDraw.left(90)
            turtleDraw.forward(180)
            turtleDraw.left(90)
            if i == 5:

                turtleDraw.penup()
                # Dibujar ala izquierda el tablero
                # 90+70
                posicion = 160
                turtleDraw.goto((posicion), -90)
                for i in range(6):
                    turtleDraw.pendown()
                    turtleDraw.left(90)
                    turtleDraw.forward(180)
                    turtleDraw.left(90)
                    turtleDraw.forward(70)
                    turtleDraw.left(90)
                    turtleDraw.forward(180)
                    turtleDraw.left(90)
                    turtleDraw.forward(70)
                    turtleDraw.penup()
                    posicion = posicion+70
                    turtleDraw.goto(posicion, -90)
            else:
                turtleDraw.forward(70)
                posicion = posicion-70
                turtleDraw.goto(-(posicion), -90)

        # Dibujar ala superior
        # variable del tamaño de un ala del tablero
        posicion = 440
        turtleDraw.goto(90, posicion)
        turtleDraw.left(90)
        turtleDraw.left(90)
        # turtleDraw.left(180)

        # dibujar ala superior e inferior
        for i in range(6):
            turtleDraw.pendown()
            turtleDraw.forward(180)
            turtleDraw.right(90)
            turtleDraw.forward(70)
            turtleDraw.right(90)
            turtleDraw.forward(180)
            turtleDraw.right(90)
            turtleDraw.forward(70)
            turtleDraw.right(90)
            turtleDraw.penup()
            posicion = posicion-70
            turtleDraw.goto(90, posicion)

            if i == 5:
                posicion = 510
                turtleDraw.goto(90, -(posicion))
                for i in range(6):
                    turtleDraw.pendown()
                    turtleDraw.forward(180)
                    turtleDraw.right(90)
                    turtleDraw.forward(70)
                    turtleDraw.right(90)
                    turtleDraw.forward(180)
                    turtleDraw.right(90)
                    turtleDraw.forward(70)
                    turtleDraw.right(90)
                    turtleDraw.penup()
                    posicion = posicion-70
                    turtleDraw.goto(90, -(posicion))

        # Posicion relleno ala izq
        turtleDraw.goto(-370, 90)
        # variable del tamaño de un ala del tablero
        # 510 (440+70)
        posicion = 90
        turtleDraw.pendown()
        turtleDraw.fillcolor("red")
        turtleDraw.left(90)

        # Iniciar el relleno
        # Dibujar ala izquierda del tablero
        for i in range(2):
            # dibuja 2 cuadros verticales
            turtleDraw.begin_fill()
            turtleDraw.forward(60)
            turtleDraw.right(90)
            turtleDraw.forward(70)
            turtleDraw.right(90)
            turtleDraw.forward(60)
            turtleDraw.right(90)
            turtleDraw.forward(70)
            turtleDraw.end_fill()
            posicion = posicion-60
            turtleDraw.goto(-370, posicion)
            turtleDraw.right(90)

            if (i == 1):
                x = 370
                for i in range(4):
                    turtleDraw.left(90)
                    turtleDraw.begin_fill()
                    turtleDraw.forward(70)
                    turtleDraw.left(90)
                    turtleDraw.forward(60)
                    turtleDraw.left(90)
                    turtleDraw.forward(70)
                    turtleDraw.left(90)
                    turtleDraw.forward(60)
                    turtleDraw.end_fill()
                    x = x-70
                    turtleDraw.goto(-(x), posicion)

                    # Construccion del triangulo izq
                    if (i == 3):
                        turtleDraw.begin_fill()
                        turtleDraw.goto(-90, -90)
                        turtleDraw.left(90)
                        turtleDraw.goto(0, 0)
                        turtleDraw.goto(-90, 90)
                        turtleDraw.end_fill()

        turtleDraw.penup()
        # Relleno ala derecha
        # Posicion relleno ala izq
        turtleDraw.goto(440, -90)
        # variable del tamaño de un ala del tablero
        # 510 (440+70)
        posicion = 90
        turtleDraw.pendown()
        turtleDraw.fillcolor("green")
        turtleDraw.left(90)

        # Iniciar el relleno
        # Dibujar ala derecha del tablero
        for i in range(2):
            # dibuja 2 cuadros verticales
            turtleDraw.begin_fill()
            turtleDraw.forward(60)
            turtleDraw.left(90)
            turtleDraw.forward(70)
            turtleDraw.left(90)
            turtleDraw.forward(60)
            turtleDraw.left(90)
            turtleDraw.forward(70)
            turtleDraw.end_fill()
            posicion = posicion-60
            turtleDraw.goto(440, -posicion)
            turtleDraw.left(90)

            if (i == 1):
                turtleDraw.penup()
                x = 370
                turtleDraw.left(90)
                turtleDraw.goto(370, posicion)
                turtleDraw.pendown()
                for i in range(4):
                    turtleDraw.begin_fill()
                    turtleDraw.forward(70)
                    turtleDraw.right(90)
                    turtleDraw.forward(60)
                    turtleDraw.right(90)
                    turtleDraw.forward(70)
                    turtleDraw.right(90)
                    turtleDraw.forward(60)
                    turtleDraw.right(90)
                    turtleDraw.end_fill()
                    x = x-70
                    turtleDraw.goto(x, posicion)

                    # Construccion del triangulo izq
                    if (i == 3):
                        turtleDraw.begin_fill()
                        turtleDraw.goto(90, 90)
                        turtleDraw.left(90)
                        turtleDraw.goto(0, 0)
                        turtleDraw.goto(90, -90)
                        turtleDraw.end_fill()

        turtleDraw.left(180)
        turtleDraw.penup()
        # Posicion relleno ala izq
        turtleDraw.goto(90, 440)
        # variable del tamaño de un ala del tablero
        # 510 (440+70)
        posicion = 90
        turtleDraw.pendown()
        turtleDraw.fillcolor("blue")
        turtleDraw.left(90)

        # Iniciar el relleno
        # Dibujar ala superior del tablero
        for i in range(2):
            # dibuja 2 cuadros verticales
            turtleDraw.begin_fill()
            turtleDraw.forward(60)
            turtleDraw.left(90)
            turtleDraw.forward(70)
            turtleDraw.left(90)
            turtleDraw.forward(60)
            turtleDraw.left(90)
            turtleDraw.forward(70)
            turtleDraw.end_fill()
            posicion = posicion-60
            turtleDraw.goto(posicion, 440)
            turtleDraw.left(90)

            if (i == 1):
                x = 370
                turtleDraw.left(90)
                turtleDraw.goto(posicion, 370)
                for i in range(4):
                    turtleDraw.begin_fill()
                    turtleDraw.forward(70)
                    turtleDraw.left(90)
                    turtleDraw.forward(60)
                    turtleDraw.left(90)
                    turtleDraw.forward(70)
                    turtleDraw.left(90)
                    turtleDraw.forward(60)
                    turtleDraw.left(90)
                    turtleDraw.end_fill()
                    x = x-70
                    turtleDraw.goto(posicion, x)

                    # Construccion del triangulo izq
                    if (i == 3):
                        turtleDraw.begin_fill()
                        turtleDraw.goto(-90, 90)
                        turtleDraw.left(90)
                        turtleDraw.goto(0, 0)
                        turtleDraw.goto(90, 90)
                        turtleDraw.end_fill()

        turtleDraw.penup()
        # Posicion relleno ala izq
        turtleDraw.goto(-90, -440)
        # variable del tamaño de un ala del tablero
        # 510 (440+70)
        posicion = 90
        turtleDraw.pendown()
        turtleDraw.fillcolor("yellow")
        # Iniciar el relleno
        # Dibujar ala inferior del tablero
        for i in range(2):
            # dibuja 2 cuadros verticales
            turtleDraw.begin_fill()
            turtleDraw.forward(60)
            turtleDraw.left(90)
            turtleDraw.forward(70)
            turtleDraw.left(90)
            turtleDraw.forward(60)
            turtleDraw.left(90)
            turtleDraw.forward(70)
            turtleDraw.end_fill()
            posicion = posicion-60
            turtleDraw.goto(-posicion, -440)
            turtleDraw.left(90)
            if (i == 1):
                x = 370
                turtleDraw.penup()
                turtleDraw.left(90)
                turtleDraw.goto(posicion, -370)
                turtleDraw.pendown()
                for i in range(4):
                    turtleDraw.begin_fill()
                    turtleDraw.forward(70)
                    turtleDraw.right(90)
                    turtleDraw.forward(60)
                    turtleDraw.right(90)
                    turtleDraw.forward(70)
                    turtleDraw.right(90)
                    turtleDraw.forward(60)
                    turtleDraw.right(90)
                    turtleDraw.end_fill()
                    x = x-70
                    turtleDraw.goto(posicion, -x)
                    # Construccion del triangulo izq
                    if (i == 3):
                        turtleDraw.begin_fill()
                        turtleDraw.goto(-90, -90)
                        turtleDraw.goto(0, 0)
                        turtleDraw.goto(90, -90)
                        turtleDraw.end_fill()

        # Dibujar cuadros faltantes (turtle up)
        turtleDraw.penup()
        for i in range(4):
            if (i == 0):
                turtleDraw.goto(-510, 30)
                turtleDraw.pendown()
                for j in range(2):
                    turtleDraw.right(90)
                    turtleDraw.forward(70)
                    turtleDraw.right(90)
                    turtleDraw.forward(60)
            if (i == 1):
                turtleDraw.penup()
                turtleDraw.goto(510, 30)
                turtleDraw.pendown()
                for j in range(2):
                    turtleDraw.left(90)
                    turtleDraw.forward(70)
                    turtleDraw.left(90)
                    turtleDraw.forward(60)
            if (i == 2):
                turtleDraw.penup()
                turtleDraw.goto(30, 510)
                turtleDraw.pendown()
                for j in range(2):
                    turtleDraw.left(90)
                    turtleDraw.forward(60)
                    turtleDraw.left(90)
                    turtleDraw.forward(70)
            if (i == 3):
                turtleDraw.penup()
                turtleDraw.goto(30, -510)
                turtleDraw.pendown()
                turtleDraw.forward(70)
                turtleDraw.left(90)
                turtleDraw.forward(60)
                turtleDraw.left(90)
                turtleDraw.forward(70)


        # Crear cuadros Casas
        self.crearCuadro(turtleDraw)
    
    def asignarCasillas(self):
        pos_casillas=[]

        #Amarillas
        pos_casillas.append(Casilla("Y1",1, -60, -475))
        pos_casillas.append(Casilla("Y2",2, 0, -475))
        pos_casillas.append(Casilla("Y3",3, 60, -475))
        pos_casillas.append(Casilla("Y4",4, 60, -405))
        pos_casillas.append(Casilla("Y5",5,60, -335))
        pos_casillas.append(Casilla("Y6",6, 60, -265))
        pos_casillas.append(Casilla("Y7",7, 60, -195))
        pos_casillas.append(Casilla("Y8",8, 60, -125))
        pos_casillas.append(Casilla("Y9",9, -60, -125))
        pos_casillas.append(Casilla("Y10",10, -60, -195))
        pos_casillas.append(Casilla("Y11",11, -60, -265))
        pos_casillas.append(Casilla("Y12",12,-60, -335))
        pos_casillas.append(Casilla("Y13",13, -60, -405))
        pos_casillas.append(Casilla("Y14",14, 0, -405))
        pos_casillas.append(Casilla("Y15",15, 0, -335))
        pos_casillas.append(Casilla("Y16",16, 0, -265))
        pos_casillas.append(Casilla("Y17",17, 0, -195))
        pos_casillas.append(Casilla("Y18",18, 0, -125))
        pos_casillas.append(Casilla("Y19",19, 0, -60))
        ## AMARILLO A VERDE
        pos_casillas.append(Casilla("YV",20, 60, -60))

        #Verdes
        pos_casillas.append(Casilla("V1",1, 475, -60))
        pos_casillas.append(Casilla("V2",2, 475, 0))
        pos_casillas.append(Casilla("V3",3, 475, 60))
        pos_casillas.append(Casilla("V4",4, 405, 60))
        pos_casillas.append(Casilla("V5",5, 335, 60))
        pos_casillas.append(Casilla("V6",6, 265, 60))
        pos_casillas.append(Casilla("V7",7, 195, 60))
        pos_casillas.append(Casilla("V8",8, 125, 60))
        pos_casillas.append(Casilla("V9",9, 125, -60))
        pos_casillas.append(Casilla("V10",10, 195, -60))
        pos_casillas.append(Casilla("V11",11, 265, -60))
        pos_casillas.append(Casilla("V12",12, 335, -60))
        pos_casillas.append(Casilla("V13",13, 405, -60))
        pos_casillas.append(Casilla("V14",14, 405, 0))
        pos_casillas.append(Casilla("V15",15, 335, 0))
        pos_casillas.append(Casilla("V16",16, 265, 0))
        pos_casillas.append(Casilla("V17",17, 195, 0))
        pos_casillas.append(Casilla("V18",18, 125, 0))
        pos_casillas.append(Casilla("V19",19, 60, 0))
        ## VERDE A AZUL
        pos_casillas.append(Casilla("VA",20, 60, 60))

        #Azul
        pos_casillas.append(Casilla("A1",1, 60, 475))
        pos_casillas.append(Casilla("A2",2, 0, 475))
        pos_casillas.append(Casilla("A3",3, -60, 475))
        pos_casillas.append(Casilla("A4",4, -60, 405))
        pos_casillas.append(Casilla("A5",5, -60, 335))
        pos_casillas.append(Casilla("A6",6, -60, 265))
        pos_casillas.append(Casilla("A7",7, -60, 195))
        pos_casillas.append(Casilla("A8",8, -60, 125))
        pos_casillas.append(Casilla("A9",9, 60, 125))
        pos_casillas.append(Casilla("A10",10, 60, 195))
        pos_casillas.append(Casilla("A11",11, 60, 265))
        pos_casillas.append(Casilla("A12",12, 60, 335))
        pos_casillas.append(Casilla("A13",13, 60, 405))
        pos_casillas.append(Casilla("A14",14, 0, 405))
        pos_casillas.append(Casilla("A15",15, 0, 335))
        pos_casillas.append(Casilla("A16",16, 0, 265))
        pos_casillas.append(Casilla("A17",17, 0, 195))
        pos_casillas.append(Casilla("A18",18, 0, 125))
        pos_casillas.append(Casilla("A19",19, 0, 60))
        ## AZUL A ROJO
        pos_casillas.append(Casilla("AR",20, -60, 60))

        #Rojo
        pos_casillas.append(Casilla("R1",1, -475, 60))
        pos_casillas.append(Casilla("R2",2, -475, 0))
        pos_casillas.append(Casilla("R3",3, -475, -60))
        pos_casillas.append(Casilla("R4",4, -405, -60))
        pos_casillas.append(Casilla("R5",5, -335, -60))
        pos_casillas.append(Casilla("R6",6, -265, -60))
        pos_casillas.append(Casilla("R7",7, -195, -60))
        pos_casillas.append(Casilla("R8",8, -125, -60))
        pos_casillas.append(Casilla("R9",9, -125, 60))
        pos_casillas.append(Casilla("R10",10, -195, 60))
        pos_casillas.append(Casilla("R11",11, -265, 60))
        pos_casillas.append(Casilla("R12",12, -335, 60))
        pos_casillas.append(Casilla("R13",13, -405, 60))
        pos_casillas.append(Casilla("R14",14, -405, 0))
        pos_casillas.append(Casilla("R15",15, -335, 0))
        pos_casillas.append(Casilla("R16",16, -265, 0))
        pos_casillas.append(Casilla("R17",17, -195, 0))
        pos_casillas.append(Casilla("R18",18, -125, 0))
        pos_casillas.append(Casilla("R19",19, -60, 0))
        ## AZUL A AMARILLO
        pos_casillas.append(Casilla("RY",20, -60, -60))

        self.add_casillas(pos_casillas)

    def buscar_casilla(self, id_buscar):
        for i, objeto in enumerate(self.casillas):
            if objeto.id == id_buscar:
                return i
        return -1


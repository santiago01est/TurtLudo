import turtle
import random
from Casilla import Casilla
from Jugador import Jugador
from Partida import Partida
from Tablero import Tablero


# Partida
def iniciar_partida(jugadores):
    # Partida
    partida = Partida(jugadores)
    # panel de juego
    # tortuga que indica el numero del dado
    turtle_control = turtle.Turtle()
    turtle_control.shape("classic")
    turtle_control.speed(50)
    turtle_control.penup()
    turtle_control.goto(0, -50)
    turtle_control.pensize(5)
    turtle_control.color("white")
    turtle_control.goto(0, -40)
    turtle_control.pendown()
    turtle_control.write("Go!", align="center", font=("Arial", 50, "bold"))

    # es true mientras no haya un ganador
    centinela = True
    ronda = 0
    numero_turno=0
    while centinela:
        y, num_dado = tirar_dado()
        # dibuja el numero obtenido por el dado
        turtle_control.clear()
        turtle_control.undo()
        turtle_control.write(num_dado, align="center",font=("Arial", 50, "bold"))
        ## setting turn return numturn
        jugador=jugadores[numero_turno]
        centinela=mover_ficha(num_dado, jugador)
        comer_ficha(jugadores,jugador)

        # verifica si ya se completó una ronda
        if len(partida.jugadores)-1 == numero_turno:
            numero_turno = 0
            ronda = ronda+1
            continue

        # siguiente turno
        numero_turno = numero_turno+1
    turtle_control.clear()
    turtle_control.undo()
    turtle_control.write("Fin del juego", align="center", font=("Arial", 50, "bold"))



def mover_ficha(num_dado, jugador):
    centinela=True
    for i in range(num_dado):
        num_menos,idCasillaSiguiente=jugador.casilla_siguiente()
        #casillaSiguiente= Casilla()
        print(idCasillaSiguiente)
        num_casilla_en_lista=tablero.buscar_casilla(idCasillaSiguiente)
        num_dado=num_dado-num_menos
        casillaSiguiente=tablero.casillas[num_casilla_en_lista]
        #print(casillaSiguiente.id)
        jugador.casilla=casillaSiguiente
        jugador.mover_ficha()

        # Verificar posicion final
        if jugador.casilla.num == 19:
            jugador.ficha.goto(0,50)
            jugador.ficha.write("Ganador Jugador #"+jugador.id, align="center",font=("Arial", 100, "bold"))
            centinela=False
            break
    return centinela

def comer_ficha(jugadores,jugador):
    casilla=jugador.casilla
    for i in range(len(jugadores)):
        if jugador.id != jugadores[i].id:
            if jugadores[i].casilla == casilla:
                print("los mismos")
                jugadores[i].mover_posicion_inicial()

def asignar_turno(partida, numero_turno):
    jugador = partida.jugadores[numero_turno]
    print(jugador.id)


# Tirar dado y obtener el numero
def tirar_dado():
    while True:
        # Solicitamos al usuario que ingrese un número
        tirar_dado = window.textinput(
            "Tirar Dado", "Ingrese d para tirar el Dado:")
        # Verificamos que el valor ingresado sea un número
        try:
            d = str(tirar_dado)
            # Si es un número, devolvemos su valor
            if d == "d":
                num_dado = random.randint(1, 6)
                return d, num_dado
        # Si no es un número, mostramos un mensaje de error y volvemos a solicitar el número
        except ValueError:
            print("Error", "El valor ingresado no es un número válido.")
# Definimos una función que solicita al usuario un número y lo valida


def solicitar_numero():
    while True:
        # Solicitamos al usuario que ingrese un número
        numero_str = window.textinput(
            "Jugadores [Max 4 jugadores]", "Ingrese el número de Jugadores:")
        # Verificamos que el valor ingresado sea un número
        try:
            numero = int(numero_str)
            # Si es un número, devolvemos su valor
            if numero >= 2 and numero <= 4:
                return numero
        # Si no es un número, mostramos un mensaje de error y volvemos a solicitar el número
        except ValueError:
            print("Error", "El valor ingresado no es un número válido.")

# segun el num de jugadores se generan las fichas


def generar_jugadores(num, ficha1):

    jugadores = []
    ## Amarillo
    # Jugador 1 Ubicación de la ficha
    ficha1.speed(5)
    ficha1.color("#efbf4d")
    ficha1.penup()
    ficha1.goto(-125, -(510-35))
    # creacion del Jugador
    ## Se crea la casilla inicial 
    casilla_jug01= Casilla("Y",0,-125, -(510-35))
    jugador1 = Jugador("1", casilla_jug01, ficha1)
    jugadores.append(jugador1)
    ## verde
    if num >= 2:
        # Jugador 2 Ubicación de la ficha
        ficha2 = turtle.Turtle()
        ficha2.shape("triangle")
        ficha2.color("#8ffe09")
        ficha2.speed(5)
        ficha2.penup()
        ficha2.goto((510-35), -125)

        # creacion del Jugador
        casilla_jug02= Casilla("V1",0,(510-35), -125)
        jugador2 = Jugador("2", casilla_jug02, ficha2)
        jugadores.append(jugador2)
    ## azul
    if num >= 3:
        # Jugador 3
        ficha3 = turtle.Turtle()
        ficha3.shape("circle")
        ficha3.color("#99ccff")
        ficha3.speed(5)
        ficha3.penup()
        ficha3.goto(125, (510-35))

        # creacion del Jugador
        casilla_jug03= Casilla("A1",0,125, (510-35))
        jugador3 = Jugador("3", casilla_jug03, ficha3)
        jugadores.append(jugador3)
    ## rojo
    if num == 4:
        # Jugador 4
        ficha4 = turtle.Turtle()
        ficha4.shape("square")
        ficha4.color("#bc012e")
        ficha4.speed(5)
        ficha4.penup()
        ficha4.goto(-(510-35), 125)
        # creacion del Jugador
        casilla_jug04= Casilla("R1",0,-(510-35), 125)
        jugador4 = Jugador("4", casilla_jug04, ficha4)
        jugadores.append(jugador4)

    iniciar_partida(jugadores)


def crearCuadro(turtleDraw):
    informacion = []

    for i in range(4):
        informacion = definir_poisicion_color_cuadro(i)

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


def definir_poisicion_color_cuadro(i):
    informacion = []

    if (i == 0):
        informacion.append("red")
        informacion.append(-230)
        informacion.append(440)
    elif (i == 1):
        informacion.append("green")
        informacion.append(160)
        informacion.append(510)
    elif (i == 2):
        informacion.append("blue")
        informacion.append(230)
        informacion.append(-440)
    elif (i == 3):
        informacion.append("yellow")
        informacion.append(-160)
        informacion.append(-510)

    return informacion


## MAIN

# Abrir tablero de juego
# Configuración del tablero
window = turtle.Screen()
window.setup(width=0.80, height=0.95, startx=None, starty=None)
window.bgcolor("white")
window.title("TurtLudo")
turtleDraw = turtle.Turtle()
# Dibujar el tablero
tablero= Tablero()
tablero.crearCasillas(turtleDraw)
#Asignar casillas
tablero.asignarCasillas()
print("Se asignaron las casillas")
#print(len(tablero.casillas))
# Pedimos el numero de jugadores
num_jugadores = solicitar_numero()

# Mostramos los datos del jugador en la ventana
# Ubicación de la tortuga para ubicar los label info de la partida
turtleDraw.penup()
turtleDraw.goto(-560, -510)
turtleDraw.write(f"Número de Jugadores: {num_jugadores}", align="center", font=(
    "Arial", 14, "bold"))

generar_jugadores(num_jugadores, turtleDraw)

window.mainloop()

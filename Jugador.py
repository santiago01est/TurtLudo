from Casilla import Casilla


class Jugador:
    def __init__(self, id,casilla,ficha):
        self.id = id
        self.casilla=casilla
        self.ficha=ficha

    def mover_ficha(self):
        self.ficha.goto(self.casilla.pos_x, self.casilla.pos_y)
    
    def casilla_siguiente(self):
        idCasillaSiguiente=""
        # obtener letra casilla actual segun su id "R=rojo V=verde etc"  Y3
        idLetra=self.casilla.id[0]
        # obtener numero casilla actual segun su id "R=rojo V=verde etc"
        idNumero=self.casilla.num
        
        print(idNumero)
        if idNumero >= 0 and idNumero <8:
            idNumero=idNumero+1
            if idLetra == "Y":
                return 0,f"Y{idNumero}"
            if idLetra == "V":
                return 0,f"V{idNumero}"
            if idLetra == "A":
                return 0,f"A{idNumero}"
            if idLetra == "R":
                return 0,f"R{idNumero}"
        ## Pasar al centro para luego cambiar de territorio
        if idNumero == 8:
            if idLetra == "Y":
                return 1,"YV"
            if idLetra == "V":
                return 1,"VA"
            if idLetra == "A":
                return 1,"AR"
            if idLetra == "R":
                return 1,"RY"

        ## Pasar de territorio
        if idNumero == 20:
            if self.casilla.id == "YV":
                return 0,"V9"
            if self.casilla.id == "VA":
                return 0,"A9"
            if self.casilla.id == "AR":
                return 0,"R9"
            if self.casilla.id == "RY":
                return 0,"Y9"
        
        ## En otro territorio
        if idNumero >= 9 and idNumero < 13:
            idNumero=idNumero+1
            if idLetra == "Y":
                return 0,f"Y{idNumero}"
            if idLetra == "V":
                return 0,f"V{idNumero}"
            if idLetra == "A":
                return 0,f"A{idNumero}"
            if idLetra == "R":
                return 0,f"R{idNumero}"
        
        ## empezar la victoria
        if idNumero == 13:
            ## jugador Casa Amarillo
            if idLetra== "Y":
                if self.id == "1":
                    idNumero=idNumero+1
                    return 0,f"Y{idNumero}"
                else:
                    return 1,"Y1"
            ## jugador Casa Verde
            if idLetra== "V":
                if self.id == "2":
                    idNumero=idNumero+1
                    return 0,f"V{idNumero}"
                else:
                    return 1,"V1"
            ## jugador Casa Azul
            if idLetra== "A":
                if self.id == "3":
                    idNumero=idNumero+1
                    return 0,f"A{idNumero}"
                else:
                    return 1,"A1"
            ## jugador Casa Roja
            if idLetra=="R":
                if self.id == "4":
                    idNumero=idNumero+1
                    return 0,f"R{idNumero}"
                else:
                    return 1,"R1"
        
        ## camino a la victoria
        if idNumero >= 14 and idNumero <=18:
            idNumero=idNumero+1
            if idLetra == "Y":
                return 0,f"Y{idNumero}"
            if idLetra == "V":
                return 0,f"V{idNumero}"
            if idLetra == "A":
                return 0,f"A{idNumero}"
            if idLetra == "R":
                return 0,f"R{idNumero}"


        return 0,None
    
    def mover_posicion_inicial(self):
        if self.id == "1":
            self.ficha.goto(-125, -(510-35))
            casilla_jug01= Casilla("Y",0,-125, -(510-35))
            self.casilla=casilla_jug01
            print("c movio")
        if self.id == "2":
            self.ficha.goto((510-35), -125)
            casilla_jug02= Casilla("V1",0,(510-35), -125)
            self.casilla=casilla_jug02
            print("c movio")
        if self.id == "3":
            self.ficha.goto(125, (510-35))
            casilla_jug03= Casilla("A1",0,-45,-480)
            self.casilla=casilla_jug03
            print("c movio")
        if self.id == "4":
            self.ficha.goto(-(510-35), 125)
            casilla_jug04= Casilla("R1",0,-45,-480)
            self.casilla=casilla_jug04
            print("c movio")


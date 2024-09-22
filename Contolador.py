import numpy as np
import Operaciones as Op

def Retorno(fx, Ap = 0, Bc = 0, Rf = 0, Nr = 0, Rs = 0, St = 0, dx = 0, Gf = 0):
    Resultado = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    if (Ap == 1):
        aux, count = Op.aproximadoRnd(fx)
        Resultado[0] = aux
        Resultado[1] = count

    if (Bc == 1):
        aux, count = Op.Biseccion(fx)
        Resultado[2] = aux
        Resultado[3] = count
    
    if (Rf == 1):
        aux, count = Op.reglaFalsa(fx)
        Resultado[4] = aux
        Resultado[5] = count

    if (Nr == 1):
        aux, count = Op.newtonRaphson(fx,dx)
        Resultado[6] = aux
        Resultado[7] = count

    if (Rs == 1):
        aux, count = Op.reglaSecante(fx)
        Resultado[8] = aux
        Resultado[9] = count
    
    if (St == 1):
        aux, count = Op.Steffensen(fx)
        Resultado[10] = aux
        Resultado[11] = count

    if (Gf == 1):
        aux, count = Op.reglaFalsa(fx)  
        return aux

    return Resultado
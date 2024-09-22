import random

def aproximadoRnd(fx):
    Contador = 0; lista=[]; bandera = 0
    while True:
        bandera += 1
        x = random.randint(-50, 50)
        if eval(fx.replace('x',(str(x)))) > 0.001:
            while True:
                Contador += 1
                x = aux = x - 0.01
                if eval(fx.replace('x',(str(aux)))) <= 0.001:
                    if round(aux,2) not in lista: lista.append(round(aux,2))
                    break
                if Contador == 200000: 
                    bandera = 200
                    break
        if bandera == 200: break
    return lista, Contador

def Biseccion(fx):
    lista = []; contador = 0 
    X_0 = random.randint(5,7)
    X = random.randint(-7,-5)
    while contador < 200:
        C = (X + X_0) / 2
        if abs(eval(fx.replace('x',str(C)))) < 0.00001 or abs(X_0-X)/2 < 0.00001: 
            if round(C,2) not in lista:
                lista.append(round(C,2))
        if eval(fx.replace('x',str(C))) * eval(fx.replace('x',str(X))) > 0: X = C
        else: X_0 = C
        contador += 1
    return lista, contador

def reglaFalsa(fx):
    a = random.randint(-10,0); b = random.randint(0,10)
    Contador = 0; repeticion = 0; lista=[]; bandera = 0
    while True: 
        bandera +=1 
        try:
            while True:
                repeticion += 1
                c = (a - ((eval(fx.replace('x',(str(a)))) * (b - a)) / (eval(fx.replace('x',(str(b)))) - eval(fx.replace('x',(str(a)))))))
                if (eval(fx.replace('x',(str(a)))) > 0 and eval(fx.replace('x',(str(c)))) < 0): a = c
                else: b = c
                if (abs(eval(fx.replace('x',(str(c))))) <= 0.0000001): 
                    if round(c,2) in lista:
                        a = random.randint(-10,0); b = random.randint(0,10)
                    else:
                        lista.append(round(c,2))
                        Contador += repeticion
                        repeticion = 0
                if  repeticion == 20000:
                    a = random.randint(-10,0); b = random.randint(0,10)
                    repeticion = 0
                    break
        except: a = random.randint(-10,0); b = random.randint(0,10)
        if(bandera == 10): return lista, Contador

def newtonRaphson(fx,dx):
    X_0 = ram = random.randint(0,20)
    contador = 0; repeticion = 0; lista=[]
    while True: 
        try:
            while True:
                repeticion +=1
                if(abs(eval(fx.replace('x',str(X_0)))) <= 0.00000001): 
                    if round(X_0,2) in lista: X_0 = ram = ram - 0.01
                    else:
                        lista.append(round(X_0,2))
                        contador += repeticion
                        repeticion = 0
                if ram <= -20 or repeticion == 50000: 
                    X_0 = ram = ram - 0.01
                    repeticion = 0
                    break
                X_0 = C = X_0 - (eval(fx.replace('x',str(X_0))) / abs(eval(dx.replace('x',str(X_0)))))
        except:  X_0 = ram = ram - 0.01
        if ram <= -20 :return lista, contador

def reglaSecante(fx):
    Xa = random.randint(-20 , 0); Xb = random.randint(0,20)
    contador = 0; repeticion = 0; lista=[]; bandera = 0
    while True:
        bandera += 1
        try:
            while True:
                repeticion += 1
                fx2 = ((eval(fx.replace('x',str(Xa))) - eval(fx.replace('x',str(Xb)))) / (Xa - Xb))
                Xc = Xa - (eval(fx.replace('x',str(Xa))) / fx2)
                Xa = Xc
                if(abs(eval(fx.replace('x',str(Xa)))) <= 0.0001): 
                    if round(Xa,2) in lista:
                        Xa = random.randint(-20 , 0); Xb = random.randint(0,20)
                    else:
                        lista.append(round(Xa,2))
                        contador += repeticion
                        repeticion = 0
                if repeticion == 10000:
                    Xa = random.randint(-20 , 0); Xb = random.randint(0,20)
                    repeticion = 0
                    break
        except:
            Xa = random.randint(-20 , 0); Xb = random.randint(0,20)
        if bandera == 11: return lista, contador

def Steffensen(fx):
    Xc=Xa=ram=random.randint(0,20)
    def F(x): return 2*x**3-5*x**3+2*x**5
    Contador=0; repeticion = 0; lista=[]
    while True:
        try:
            while True:
                repeticion +=1
                if (abs(F(Xc)) <= 0.0001):
                    if round(Xa,2) in lista:
                        Xa=ram=ram-1
                    else:
                        lista.append(round(Xa,2))
                        Contador += repeticion
                        repeticion = 0
                if ram ==-10 or repeticion == 20000: 
                    Xc=Xa=ram=ram-1
                    repeticion = 0
                    break
                fxa = eval(fx.replace('x',str(Xa)))
                fxa_A = eval(fx.replace('x',str((Xa+fxa))))
                Xa=Xc=Xa-(fxa**2)/(fxa_A-fxa)
        except: Xc=Xa=ram=ram-1
        if(ram <= -10):return lista, Contador
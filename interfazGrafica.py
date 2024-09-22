#Librerias necesarias
import numpy as np
import tkinter as tk
from io import BytesIO
import Contolador as ct
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

answer2 = []
#Funciones
def cmd(): 
    if polinomio.get() != '':
        Data = [0,0,0,0,0,0,0,0,0,0,0,0]
        answer = ''
        i = 0; j = 1
        global answer2 
        answer2 = []
        while True:
            solved.set(answer)
            Data = ct.Retorno(polinomio.get().lower() ,Aproximado.get(), Biseccion.get(), ReglaFalsa.get(),newtonRaphson.get(),reglaSecante.get(),Steffensen.get(),derivada.get().lower())
            if(Aproximado.get()==1): answer = ('Tanteo \n Resultado: ' + str(Data[0]) + '\nIteraciones: '+ str(Data[1])+'\n\n')
            if(Biseccion.get()==1): answer += ('Biseccion \n Resultado: ' + str(Data[2]) + '\nIteraciones: '+ str(Data[3])+'\n\n')
            if(ReglaFalsa.get()==1): answer += ('Regla Falsa \n Resultado: ' + str(Data[4]) + '\nIteraciones: '+ str(Data[5])+'\n\n')
            if(newtonRaphson.get()==1): answer += ('Newton Raphson \n Resultado: ' + str(Data[6]) + '\nIteraciones: '+ str(Data[7])+'\n\n')
            if(reglaSecante.get()==1): answer += ('Regla Secante \n Resultado: ' + str(Data[8]) + '\nIteraciones: '+ str(Data[9])+'\n\n')
            if(Steffensen.get()==1): answer += ('Steffensen \n Resultado: ' + str(Data[10]) + '\nIteraciones: '+ str(Data[11])+'\n\n')
            solved.set(answer)
            if(Aproximado.get()==1): answer2.append(('Tanteo Resultado: ' + str(Data[0]) + ' Iteraciones: '+ str(Data[1])))
            if(Biseccion.get()==1): answer2.append( ('Biseccion Resultado: ' + str(Data[2]) + ' Iteraciones: '+ str(Data[3])))
            if(ReglaFalsa.get()==1): answer2.append( ('Regla Falsa Resultado: ' + str(Data[4]) + ' Iteraciones: '+ str(Data[5])))
            if(newtonRaphson.get()==1): answer2.append( ('Newton Raphson Resultado: ' + str(Data[6]) + ' Iteraciones: '+ str(Data[7])))
            if(reglaSecante.get()==1): answer2.append( ('Regla Secante Resultado: ' + str(Data[8]) + ' Iteraciones: '+ str(Data[9])))
            if(Steffensen.get()==1): answer2.append( ('Steffensen Resultado: ' + str(Data[10]) + ' Iteraciones: '+ str(Data[11])))
            break
            
def Grafica():
    if polinomio.get() != '':
        i = 0
        vector = np.array(ct.Retorno(polinomio.get().lower(),0,0,0,0,0,0,0,1))  
        FrameG = tk.Frame(width=530, height=530)
        FrameI.place_forget()
        FrameG.place(x=430, y=155)
        fig, gra = plt.subplots(dpi=100, figsize=(5.3,5.3))             
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        gra.axhline(linewidth=2, color='k')
        gra.axvline(linewidth=2, color='k')
        gra.set_facecolor('lightgray')
        gra.grid()
        x = np.arange(-10, 10, 0.1)
        line = gra.plot(x, eval(polinomio.get().lower()), color ='r', linestyle='solid')
        while i < len(vector):
            plt.plot(vector[i],0,'ob')
            i += 1
        Grafica = FigureCanvasTkAgg(fig, FrameG)
        Grafica.draw()
        Grafica.get_tk_widget().pack()

def Derivada():
    if newtonRaphson.get() == 1: textBox_derivada.place(x=435, y= 10, width=205)
    else: textBox_derivada.place_forget()

def reporte():
    if polinomio.get() != '':
        fig, ax = plt.subplots(dpi=100, figsize=(5,5))
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        ax.axhline(linewidth=2, color='k')
        ax.axvline(linewidth=2, color='k')
        ax.set_facecolor('lightgray')
        ax.grid()
        x = np.arange(-10, 10, 0.1)
        line = ax.plot(x, eval(polinomio.get().lower()), color ='r', linestyle='solid')
        j = 0
        vector = np.array(ct.Retorno(polinomio.get().lower(),0,0,0,0,0,0,0,1)) 
        while j < len(vector):
            plt.plot(vector[j],0,'ob')
            j += 1
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        c = canvas.Canvas("Reporte.pdf", pagesize=letter)
        c.drawString(100, 750, f"Reporte de la ecuacion: {polinomio.get().lower()}")
        i = 730
        for lis in answer2:
            c.drawString(100, i, lis)
            i -= 20
        img = ImageReader(buffer)
        c.drawImage(img, 70, 130)
        c.save()

#Configuracion de la ventana
window = tk.Tk()
window.title("Solucion y Graficacion de Polinomios")
window.config(width=980, height=700, background='gray40')
window.resizable(0, 0)
icono = tk.PhotoImage(file="Sources/Icono.png")
window.iconphoto(True, icono)

#Recuadros
FrameI = tk.Frame(width=530, height=530)
FrameI.place(x=430, y=155)
imgF = tk.PhotoImage(file='Sources/BgPlano.png')
gbackGround = tk.Label(FrameI, image= imgF)
gbackGround.pack()

FrameG = tk.Frame(width=530, height=530)

FrameS = tk.Frame(width=400, height=530)
FrameS.place(x=20, y=155)

FrameChe = tk.Frame(width=940, height=100)
FrameChe.place(x=20, y=45)

#Etiquetas
labelPolinomio = tk.Label(text="Ingrese el polinomio:", bg='gray40', font=("Arial", 14, 'bold'))
labelPolinomio.place(x=20, y=8)

solved = tk.StringVar()
labelSolved = tk.Label(FrameS , font=("Arial", 14, 'bold'), textvariable=solved)
labelSolved.place(x=40, y=10,)

#Cuadros de texto
polinomio = tk.StringVar()
textBox_Polinomio = tk.Entry(bg='white', font=("Arial", 14, 'bold'), textvariable= polinomio)
textBox_Polinomio.place(x=220, y= 10, width=205)

derivada = tk.StringVar()
textBox_derivada = tk.Entry(bg='white', font=("Arial", 14, 'bold'), textvariable= derivada)

#Botones seleccionables
Aproximado = tk.IntVar()
checkBox_Aproximado = tk.Checkbutton(text='Tanteo', variable=Aproximado, onvalue=1, offvalue=0, font=("Arial", 14, 'bold'))
checkBox_Aproximado.place(x=30, y=50)

Biseccion = tk.IntVar()
checkBox_Biseccion = tk.Checkbutton(text='Biseccion', variable=Biseccion, onvalue=1, offvalue=0, font=("Arial", 14, 'bold'))
checkBox_Biseccion.place(x=240, y=50)

ReglaFalsa = tk.IntVar()
checkBox_ReglaFalsa = tk.Checkbutton(text='Regla Falsa', variable=ReglaFalsa, onvalue=1, offvalue=0, font=("Arial", 14, 'bold'))
checkBox_ReglaFalsa.place(x=450, y=50)

newtonRaphson = tk.IntVar()
checkBox_newtonRaphson = tk.Checkbutton(text='Newton Raphson', command=Derivada, variable=newtonRaphson, onvalue=1, offvalue=0, font=("Arial", 14, 'bold'))
checkBox_newtonRaphson.place(x=30, y=100)

reglaSecante = tk.IntVar()
checkBox_reglaSecante = tk.Checkbutton(text='Regla Secante', variable=reglaSecante, onvalue=1, offvalue=0, font=("Arial", 14, 'bold'))
checkBox_reglaSecante.place(x=240, y=100)

Steffensen = tk.IntVar()
checkBox_Steffensen = tk.Checkbutton(text='Steffensen', variable=Steffensen, onvalue=1, offvalue=0, font=("Arial", 14, 'bold'))
checkBox_Steffensen.place(x=450, y=100)

#Botones
cmdSolved = tk.Button(text='Resolver', bg='white', font=("Arial", 14, 'bold'), command=cmd)
cmdSolved.place(x=650, y= 10, width=100,height=27)

cmdGraficar = tk.Button(text='Graficar', bg='white', font=("Arial", 14, 'bold'), command=Grafica)
cmdGraficar.place(x=755, y= 10, width=100,height=27)

cmdreporte = tk.Button(text='Reporte', bg='white', font=("Arial", 14, 'bold'), command=reporte)
cmdreporte.place(x=860, y= 10, width=100,height=27)

#Carga
window.mainloop()
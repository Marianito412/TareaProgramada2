from tkinter import *
import tkinter as tk
import funciones

raiz = Tk()
raiz.title("Sistema electoral")
raiz.configure(bg="white")
raiz.iconbitmap("logo-TEC.ico")
raiz.resizable(False, False)
raiz.geometry("650x600")

padron = []

def CrearPadron():
    WCrearPadron = tk.Toplevel(raiz)
    FCantidad = tk.Entry(WCrearPadron, width=20, font=("Arial", 10))
    FCantidad.insert()
    FCantidad.pack()
    
    BTCrear = tk.Button(WCrearPadron, text="Reportar Ganador", width=20, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=lambda: funciones.crearPadron(padron, int(FCantidad.get())))
    BTCrear.pack()
    
    print(padron)

def reporteTotal():
    repTotal = tk.Toplevel()
    repTotal.title("Reportes")
    repTotal.configure(bg="white")
    repTotal.iconbitmap("logo-TEC.ico")
    repTotal.resizable(False, False)
    repTotal.geometry("540x500")

    height = 5
    width = 5
    padron = sorted(padron, key = lambda x: int(str(x[2])+str(x[3])))
    for i, persona in enumerate(padron): #Rows
        for j, atributo in enumerate(persona): #Columns
            b = Entry(repTotal, text=f"{atributo}")
            b.grid(row=i, column=j)

def abrirReportes():
    reportes = tk.Toplevel()
    reportes.title("Reportes")
    reportes.configure(bg="white")
    reportes.iconbitmap("logo-TEC.ico")
    reportes.resizable(False, False)
    reportes.geometry("540x500")

    texto = Label(reportes, text="Reportes", bg="white", font=("Arial", 20))
    texto.grid(row=0, column=1, padx=200, pady=30)

    bGanador = Button(reportes, text="Reportar Ganador", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue")
    bGanador.configure(cursor="hand2")
    bGanador.grid(row=1, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=2, column=1, padx=15)
    
    bRol = Button(reportes, text="Listado por rol", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue")
    bRol.configure(cursor="hand2")
    bRol.grid(row=3, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=2, column=1, padx=15)

    bSede = Button(reportes, text="Padrón por cada sede", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue")
    bSede.configure(cursor="hand2")
    bSede.grid(row=5, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=4, column=1, padx=15)

    bEstudiantil = Button(reportes, text="Padrón estudiantil por sede", width=20, height=2, font=("Arial", 10), activebackground="lightgreen", bg="lightblue")
    bEstudiantil.configure(cursor="hand2")
    bEstudiantil.grid(row=7, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=6, column=1, padx=15)

    bCarrera = Button(reportes, text="Padrón de votantes por carrera", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue")
    bCarrera.configure(cursor="hand2")
    bCarrera.grid(row=9, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=8, column=1, padx=15)

    bAsociaciones = Button(reportes, text="Representantes de asociaciones", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue")
    bAsociaciones.configure(cursor="hand2")
    bAsociaciones.grid(row=9, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=8, column=1, padx=15)

    bReporteBD = Button(reportes, text="Reporte total de la BD", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=reporteTotal)
    bReporteBD.configure(cursor="hand2")
    bReporteBD.grid(row=9, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=8, column=1, padx=15)

    bSalir = Button(reportes, text="Salir", width=20, height=2, font=("Arial", 10), activebackground="lightgreen", bg="lightblue",command=reportes.destroy)
    bSalir.configure(cursor="hand2")
    bSalir.grid(row=11, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=10, column=1, padx=15)

# Ventana principal

texto = Label(raiz, text="Elecciones de rectoria", bg="white", font=("Arial", 20))
texto.grid(row=0, column=1, padx=200, pady=30)

bPadron = Button(raiz, text="Crear padron", width=20, height=3, font=("Arial", 10), activebackground="lightpink",bg="lightblue", command=CrearPadron)
bPadron.configure(cursor="hand2")
bPadron.grid(row=1, column=1)

bCandidato = Button(raiz, text="Insertar candidato", width=20, height=3, font=("Arial", 10), activebackground="lightpink",bg="lightblue")
bCandidato.configure(cursor="hand2")
bCandidato.grid(row=3, column=1)

texto = Label(raiz, text="", bg="white")
texto.grid(row=2, column=1, padx=15)

bRector = Button(raiz, text="Elegir rector(a)", width=20, height=3, font=("Arial", 10), activebackground="lightpink",bg="lightblue")
bRector.configure(cursor="hand2")
bRector.grid(row=5, column=1)

texto = Label(raiz, text="", bg="white")
texto.grid(row=4, column=1, padx=15)

bDB = Button(raiz, text="Respaldar BD", width=20, height=3, font=("Arial", 10), activebackground="lightpink", bg="lightblue")
bDB.configure(cursor="hand2")
bDB.grid(row=7, column=1)

texto = Label(raiz, text="", bg="white")
texto.grid(row=6, column=1, padx=15)

bReportes = Button(raiz, text="Reportes", width=20, height=3, font=("Arial", 10), activebackground="lightpink",
                   bg="lightblue", command=abrirReportes)
bReportes.configure(cursor="hand2")
bReportes.grid(row=9, column=1)

texto = Label(raiz, text="", bg="white")
texto.grid(row=8, column=1, padx=15)

bSalir = Button(raiz, text="Salir", width=20, height=3, font=("Arial", 10), activebackground="lightpink", bg="lightblue")
bSalir.configure(cursor="hand2")
bSalir.grid(row=11, column=1)

texto = Label(raiz, text="", bg="white")
texto.grid(row=10, column=1, padx=15)

#def updateButtons():
#    print("hola")
#    raiz.after(1000, updateButtons)

#raiz.after(2000, lambda: print("hola"))
#raiz.after(1000, updateButtons)
raiz.mainloop()

#Reportes


  

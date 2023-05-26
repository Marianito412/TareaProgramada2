from tkinter import *
import tkinter as tk
from tkinter import ttk
import funciones
import re
from tkinter import messagebox

raiz = Tk()
raiz.title("Sistema electoral")
raiz.configure(bg="white")
raiz.iconbitmap("logo-TEC.ico")
raiz.resizable(False, False)
raiz.geometry("650x600")

padron = []

def CrearPadron():
    Cpadron = tk.Toplevel()
    Cpadron.title("Reportes")
    Cpadron.configure(bg="white")
    Cpadron.iconbitmap("logo-TEC.ico")
    Cpadron.resizable(False, False)
    Cpadron.geometry("400x200")
    Cpadron.grab_set()

    frame = Frame(Cpadron, width=100, height=100, bg="white")
    frame.grid(row=0, column=0, pady=20)

    texto = Label(frame, text="Padron:", bg="white", font=("Arial", 15))
    texto.grid(row=0, column=0, pady=10)

    texto = Label(Cpadron, text="", bg="white")
    texto.grid(row=1, column=0)

    textoPadron = Label(Cpadron,pady=15, text="Ingrese el numero de personas", bg="white", font=("Arial", 10),)
    textoPadron.grid(row=1, column=0,padx=15)


    FCantidad = Entry(Cpadron)

    def limpiarDatos2():
        FCantidad.delete(0, tk.END)

    def activarBotonCrear(event):
        print("gggg")
        if FCantidad.get().isdigit():
            BTCrear.configure(state=tk.NORMAL)
            etiquetaPadron.config(text="")
        else:
            etiquetaPadron.config(text="Debe digitar un número",fg="gray")
            BTCrear.configure(state=tk.DISABLED)

    etiquetaPadron=Label(Cpadron,bg="white")
    etiquetaPadron.grid(row=2, column=2)
    
    FCantidad.bind("<KeyRelease>", activarBotonCrear)
    
    FCantidad.grid(row=1, column=2, padx=20)

    def procesoPadron(padron,pNumero):
        funciones.crearPadron(padron, int(pNumero))
        messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
        limpiarDatos2()
        
    
    BTCrear = Button(Cpadron, text="Registrar",width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightblue", command=lambda: procesoPadron(padron, int(FCantidad.get())))
    BTCrear.configure(cursor="hand2")
    BTCrear.grid(row=3, column=0)
    BTCrear.configure(state=tk.DISABLED)
    print(padron)







def reporteTotal():
    columnas = ("Cédula", "Nombre", "Sede", "Carrera", "Rol", "Detalle de rol", "Carnet", "Voto", "Candidatura")

    repTotal = tk.Toplevel()
    repTotal.title("Reporte Total")
    repTotal.configure(bg="white")
    repTotal.iconbitmap("logo-TEC.ico")
    repTotal.resizable(False, False)

    tabla = ttk.Treeview(repTotal, columns=columnas, show='headings')
    for columna in columnas:
        tabla.heading(columna, text=columna)
    
    fPadron = padron
    fPadron = sorted(fPadron, key = lambda x: int(str(x[2])+str(x[3])))

    for persona in fPadron:
        tabla.insert('', tk.END, values=funciones.sanitizarInfo(persona))
        
    tabla.grid(row=0,column=0, sticky="nsew")

def generarTabla(pVentana, pLista, pColumnas):
    tablaEstudiantes = ttk.Treeview(repTotal, columns=columnas, show='headings')
    for columna in pColumnas:
        tabla.heading(columna, text=columna)
    for persona in funciones.filtrarPadron(fPadron, [lambda x: x[4] == 1]):
        tablaEstudiantes.insert('', tk.END, values=funciones.sanitizarInfo(persona))
    tablaEstudiantes.grid(row=0,column=0, sticky="nsew")

def reporteRoles():
    columnas = ("Cédula", "Nombre", "Sede", "Carrera", "Rol", "Detalle de rol", "Carnet", "Voto", "Candidatura")

    repTotal = tk.Toplevel()
    repTotal.title("Reporte por roles")
    repTotal.configure(bg="white")
    repTotal.iconbitmap("logo-TEC.ico")
    repTotal.resizable(False, False)

    fPadron = padron
    fPadron = sorted(fPadron, key = lambda x: int(str(x[2])+str(x[3])))

    tablaEstudiantes = ttk.Treeview(repTotal, columns=columnas, show='headings')
    for columna in columnas:
        tablaEstudiantes.heading(columna, text=columna)
    for persona in funciones.filtrarPadron(fPadron, [lambda x: x[4] == 1]):
        tablaEstudiantes.insert('', tk.END, values=funciones.sanitizarInfo(persona))
    tablaEstudiantes.grid(row=0,column=0, sticky="nsew")

    

def abrirReportes():
    reportes = tk.Toplevel()
    reportes.title("Reportes")
    reportes.configure(bg="white")
    reportes.iconbitmap("logo-TEC.ico")
    reportes.resizable(False, False)
    reportes.geometry("540x500")
    reportes.grab_set()

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



def candidatos():
    candidatos = tk.Toplevel()
    candidatos.title("Candidatos")
    candidatos.configure(bg="white")
    candidatos.iconbitmap("logo-TEC.ico")
    candidatos.resizable(False, False)
    candidatos.geometry("540x500")
    candidatos.grab_set()
    frame = Frame(candidatos, width=100, height=100, bg="white")
    frame.grid(row=0, column=0, padx=5, pady=20)

    texto = Label(frame, text="Candidatos:", bg="white", font=("Arial", 15))
    texto.grid(row=0, column=0, padx=15, pady=10)

    texto = Label(raiz, text="", bg="white")
    texto.grid(row=1, column=0)

    textoCedula = Label(candidatos,pady=15, text="Cédula", bg="white", font=("Arial", 10))
    textoCedula.grid(row=1, column=1)

    cedula = Entry(candidatos)
    cedula.grid(row=1, column=2, padx=40)

    def activarBotonBuscar(event):
        print("gggg")
        if validarCedula(cedula.get()):
            bBuscar.configure(state=tk.NORMAL)
            etiquetaCedula.config(text="")
        else:
            etiquetaCedula.config(text="Formato: 0-0000-0000",fg="gray")
            bBuscar.configure(state=tk.DISABLED)

    etiquetaCedula=Label(candidatos,bg="white")
    etiquetaCedula.grid(row=2, column=2)
    
    cedula.bind("<KeyRelease>", activarBotonBuscar)

    periodo = None
    print(padron)

    varOpcion=IntVar()
    encontrado = False



    def validarCedula(pCedula):
        """
        Funcionalidad: valida una cédula contra regex
        Entradas:
        -pCedula(str): la cedula a validar
        Salidas:
        -pCedula: la cédula si cumple con las validaciones
        """
        if re.match(r"^\d{1}-\d{4}-\d{4}$", pCedula):
            return True
        else:
            return False

    def buscarCandidato():
        flag = False
        generarPeriodo(flag)
        lecturaNombre.configure(state=tk.NORMAL)  # Habilitar el modo de edición
        lecturaNombre.delete("1.0", tk.END)
        print(cedula.get())
        print(padron)
        resultado = funciones.insertarCandidato(padron, cedula.get())
        print(resultado)
        texto = resultado[1] if resultado!= [] else "Esta persona no está en el padrón"
        if resultado!= []:
            encontrado=True
            opcion(encontrado) 

        else:
            encontrado = False
            opcion(encontrado)
        print(texto)
        lecturaNombre.insert(tk.END, texto)
        lecturaNombre.configure(state=tk.DISABLED)
    
    bBuscar = Button(candidatos, text="Buscar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightblue",command=buscarCandidato)
    bBuscar.configure(state=tk.DISABLED)    
    bBuscar.configure(cursor="hand2")
    bBuscar.grid(row=3, column=2)

    texto = Label(candidatos, text="", bg="white")
    texto.grid(row=4, column=0)

    textoNombre = Label(candidatos,pady=15,padx=18, text="Nombre", bg="white", font=("Arial", 10))
    textoNombre.grid(row=5, column=1)   
    
    lecturaNombre= Text(candidatos,width=26, height=2)
    lecturaNombre.grid(row=5, column=2)

    

    def generarPeriodo(flag):
        textoPeriodo = Label(candidatos, pady=15, text="Periodo", bg="white", font=("Arial", 10))
        textoPeriodo.grid(row=10, column=1)
        nonlocal periodo
        periodo = Entry(candidatos)
        periodo.bind("<KeyRelease>", activar)
        periodo.grid(row=10, column=2, padx=40)
        periodo.configure(state=tk.NORMAL)
        periodo.delete(0, tk.END)
        if flag:
            periodo.delete(0, tk.END)
            periodo.configure(state=tk.NORMAL)
            #activar()
        else:
            periodo.delete(0, tk.END)
            periodo.configure(state=tk.DISABLED)

    def imprimir():
        if varOpcion.get() == 1:
            print("Si")
            flag = True
            generarPeriodo(flag)
        elif varOpcion.get() == 2:
            print("No")
            flag = False
            generarPeriodo(flag)
        else:
            flag = False
            generarPeriodo(flag)

    def opcion(encontrado):
        Label(candidatos, text="", bg="white").grid(row=5, column=2)
        Label(candidatos, text="Sera candidato?", bg="white", font=("Arial", 10)).grid(row=6, column=2)
        Label(candidatos, text="", bg="white").grid(row=7, column=2)
        rbSi = Radiobutton(candidatos, text="Si", variable=varOpcion, font=("Arial", 10), value=1, bg="white", command=imprimir)
        rbSi.grid(row=8, column=2)
        rbNo = Radiobutton(candidatos, text="No", variable=varOpcion, font=("Arial", 10), value=2, bg="white", command=imprimir)
        rbNo.grid(row=9, column=2)
        varOpcion.set(0)
        rbSi.configure(state=tk.DISABLED)
        rbNo.configure(state=tk.DISABLED)
        if encontrado:
            rbSi.configure(state=tk.NORMAL)
            rbNo.configure(state=tk.NORMAL)
        else:
            varOpcion.set(0)
            flag = False
            generarPeriodo(flag)
            rbSi.configure(state=tk.DISABLED)
            rbNo.configure(state=tk.DISABLED)

    def limpiarDatos():
        flag = False
        generarPeriodo(flag)
        lecturaNombre.configure(state=tk.NORMAL)  # Habilitar el modo de edición
        lecturaNombre.delete("1.0", tk.END)
        lecturaNombre.configure(state=tk.DISABLED)
        varOpcion.set(0)
        cedula.delete(0, tk.END)


    texto = Label(candidatos, text="", bg="white")
    texto.grid(row=11, column=1, padx=15)
    
    bLimpiar = Button(candidatos, text="Limpiar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightblue",command=limpiarDatos)
    bLimpiar.configure(cursor="hand2")
    bLimpiar.grid(row=12, column=1)

    cedula.get()

    def proceso(pPadron,pCedula,pPeriodo):
        funciones.registrarCandidato(pPadron,pCedula,pPeriodo)
        messagebox.showinfo(title="Verificacion",message="Se ha registrado el candidato con exito")
        print(padron)
        limpiarDatos()
    
    bRegistrar = Button(candidatos, text="Registrar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightblue", command=lambda: proceso(padron, cedula.get(), periodo.get()))
    bRegistrar.configure(cursor="hand2")
    bRegistrar.grid(row=12, column=2)
    bRegistrar.configure(state=tk.DISABLED)

    def validarPeriodo(pPeriodo):
        """
        Funcionalidad: valida una cédula contra regex
        Entradas:
        -pCedula(str): la cedula a validar
        Salidas:
        -pCedula: la cédula si cumple con las validaciones
        """
        if re.match(r"^\d{4}-\d{4}$", pPeriodo):
            return True
        else:
            return False

    def activar(event):
        print("Alooo")
        if validarPeriodo(periodo.get()):
            bRegistrar.configure(state=tk.NORMAL)
            etiquetaPeriodo.config(text="")
        else:
            etiquetaPeriodo.config(text="Formato:0000-0000",fg="gray")
            bRegistrar.configure(state=tk.DISABLED)

    etiquetaPeriodo=Label(candidatos,bg="white")
    etiquetaPeriodo.grid(row=11, column=2)

def procesoRector(pPadron):
        print("a")
        funciones.elegirRector(pPadron)
        messagebox.showinfo(title="Verificacion",message="Fue elegido con exito")
        print(padron)

    
# Ventana principal

texto = Label(raiz, text="Elecciones de rectoria", bg="white", font=("Arial", 20))
texto.grid(row=0, column=1, padx=200, pady=30)

bPadron = Button(raiz, text="Crear padron", width=20, height=3, font=("Arial", 10), activebackground="lightpink",bg="lightblue", command=CrearPadron)
bPadron.configure(cursor="hand2")
bPadron.grid(row=1, column=1)

bCandidato = Button(raiz, text="Insertar candidato", width=20, height=3, font=("Arial", 10), activebackground="lightpink",bg="lightblue", command=candidatos)
bCandidato.configure(cursor="hand2")
bCandidato.grid(row=3, column=1)

texto = Label(raiz, text="", bg="white")
texto.grid(row=2, column=1, padx=15)

bRector = Button(raiz, text="Elegir rector(a)", width=20, height=3, font=("Arial", 10), activebackground="lightpink",bg="lightblue",command=lambda: procesoRector(padron))
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


  

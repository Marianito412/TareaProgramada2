from tkinter import *
import tkinter as tk
from tkinter import ttk
import funciones
import archivos
import re
from tkinter import messagebox

raiz = Tk()
raiz.title("Sistema electoral")
raiz.configure(bg="white")
raiz.iconbitmap("logo-TEC.ico")
raiz.resizable(False, False)
raiz.geometry("650x600")

padron = archivos.lee("padron")

def CrearPadron():
    """
    Funcionalidad: Menú para crear una cantidad de personas e incluirlas en el padrón
    """
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

def generarTabla(pVentana, pLista, pColumnas, pSanitizar, filtros=[]):
    """
    Funcionalidad: Genera una tabla de TKinter con la forma especificada
    Entradas:
    -pVentana: La ventana en la que agregar la tabla
    -pLista: La lista de personas a incluir en la tabla
    -pColumnas: La lista de encabezados de la tabla
    -pSanitizar: Una función que prepara cada elemento de pPadron para ser agregado a la tabla
    -filtros: Lista de criterios a usar al recorrer el padrón
    Salidas:
    -tablaEstudiantes: Una referencia a la tabla generada
    """
    
    tablaEstudiantes = ttk.Treeview(pVentana, columns=pColumnas, show='headings')
    for columna in pColumnas:
        tablaEstudiantes.heading(columna, text=columna)
    for persona in funciones.filtrarPadron(pLista, filtros):
        tablaEstudiantes.insert('', tk.END, values=pSanitizar(persona))
    #tablaEstudiantes.grid(row=0,column=0, sticky="nsew")
    return tablaEstudiantes

def reporteGanador():
    """
    Funcinalidad: Muestra el ganador y el conteo de las votaciones
    """
    repGanador = tk.Toplevel()
    repGanador.title("Reporte Ganador")
    repGanador.configure(bg="white")
    repGanador.iconbitmap("logo-TEC.ico")
    repGanador.resizable(True, True)
    repGanador.grab_set()

    votacion = {}
    for candidato in funciones.filtrarPadron(padron, [lambda x: x[-1] != None]):
        votacion[candidato[0]] = 0
    
    for votante in padron:
        if votante[-1] == None:
            return
        if votante[4] == 1:
            votacion[votante[-2]]+=0.7
        elif votante[4] == 2:
            votacion[votante[-2]]+=1
        elif votante[4] == 3:
            votacion[votante[-2]]+=0.33

    tablaCandidatos = ttk.Treeview(repGanador, columns=("Candidato", "Votacion"), show="headings")
    for columna in ("Candidato", "Votacion"):
        tablaCandidatos.heading(columna, text=columna)
        tablaCandidatos.column(columna, width=10, stretch=False)
    for candidato in votacion:
        tablaCandidatos.insert("", tk.END, values=[candidato, votacion[candidato]])
    tablaCandidatos.grid(row=0, column=0, sticky="nsew")
    ganador = funciones.determinarGanador(votacion)
    TGanador = ttk.Label(repGanador, text=ganador)
    TGanador.grid(row=1, column=0)
    print(votacion)

def reporteTotal():
    """
    Funcionalidad: Muestar una tabla con la información de todas las personas de la base de datos
    """
    columnas = ("Cédula", "Nombre", "Sede", "Carrera", "Rol", "Detalle de rol", "Carnet", "Voto", "Candidatura")

    repTotal = tk.Toplevel()
    repTotal.title("Reporte Total")
    repTotal.configure(bg="white")
    repTotal.iconbitmap("logo-TEC.ico")
    repTotal.resizable(True, True)
    repTotal.grab_set()

    fPadron = sorted(padron, key = lambda x: int(str(x[2])+str(x[3])))
    scroll = ttk.Scrollbar(repTotal, orient=tk.HORIZONTAL)
    tablaTotal = generarTabla(repTotal, fPadron, columnas, funciones.sanitizarInfo)
    repTotal.update_idletasks()
    scroll.configure(command = tablaTotal.xview)
    scroll.grid(row=1, column=0, sticky='nsew')
    tablaTotal.configure(xscrollcommand=scroll.set)
    tablaTotal.grid(row=0, column=0, sticky="nsew")

    archivos.guardarTexto("reporteTotal", ".html", funciones.generarHTML(fPadron, columnas, funciones.sanitizarInfo, []))

def reporteAso():
    """
    Funcionalidad: Muestra una tabla con todas las personas relacionadas a la asociación de estudiantes
    """
    def prepararInfo(persona):
        """
        Funcionalidad: Genera una lista con el formato requerido para este reporte
        Entradas:
        -pPersona: La persona sobre la cual generar la lista
        Salidas:
        -return: La lista generada
        """
        return[funciones.traducirCodigo(persona[2]), funciones.traducirCodigo(persona[3]), persona[6], " ".join(persona[1]), funciones.traducirDetalleRol(persona[4], persona[5])]
    columnas = ("Sede", "Carrera", "Carnet", "Nombre", "Detalle del rol")

    repAso = tk.Toplevel()
    repAso.title("Reporte Total")
    repAso.configure(bg="white")
    repAso.iconbitmap("logo-TEC.ico")
    repAso.resizable(False, False)
    repAso.grab_set()

    fPadron = sorted(padron, key = lambda x: int(str(x[2])+str(x[3])))
    tablaAso = generarTabla(repAso, fPadron, columnas, prepararInfo, filtros=[lambda persona: persona[4] == 1])
    tablaAso.grid(row=0, column=0, sticky="nsew")

    archivos.guardarTexto("reporteAso", ".html", funciones.generarHTML(fPadron, columnas, prepararInfo, [lambda persona: persona[4] == 1]))

def reporteRoles():
    """
    Funcionalidad: Muestar 3 tablas, una por cada tipo de rol en la unversidad
    """
    columnas = ("Cédula", "Nombre", "Sede", "Carrera", "Rol", "Detalle de rol", "Carnet", "Voto", "Candidatura")

    repRoles = tk.Toplevel()
    repRoles.title("Reporte por roles")
    repRoles.configure(bg="white")
    repRoles.iconbitmap("logo-TEC.ico")
    repRoles.resizable(False, False)
    repRoles.grab_set()

    fPadron = sorted(padron, key = lambda x: int(str(x[2])+str(x[3])))

    tablaEstudiantes = generarTabla(repRoles, fPadron, columnas, funciones.sanitizarInfo,[lambda x: x[4]==1])
    tablaEstudiantes.grid(row=0, column=0, sticky="nsew")
    archivos.guardarTexto("reporteEstudiantes", ".html", funciones.generarHTML(fPadron, columnas, funciones.sanitizarInfo, [lambda x: x[4] == 1]))

    tablaDocentes = generarTabla(repRoles, fPadron, columnas, funciones.sanitizarInfo, [lambda x: x[4]==2])
    tablaDocentes.grid(row=1, column=0, sticky="nsew")
    archivos.guardarTexto("reporteDocentes", ".html", funciones.generarHTML(fPadron, columnas, funciones.sanitizarInfo, [lambda x: x[4] == 2]))

    tablaAdmins = generarTabla(repRoles, fPadron, columnas, funciones.sanitizarInfo, [lambda x: x[4]==3])
    tablaAdmins.grid(row=2, column=0, sticky="nsew")
    archivos.guardarTexto("reporteAdministrativos", ".html", funciones.generarHTML(fPadron, columnas, funciones.sanitizarInfo, [lambda x: x[4] == 3]))


def reporteSedes():
    """
    Funcionalidad: Muestra una tabla por cada sede con la información de los estudiantes de esa sede
    """
    sedes, codigos = archivos.leerSedes()

    def limpiarEntrada(persona):
        """
        Funcionalidad: Genera una lista con el formato requerido para este reporte
        Entradas:
        -pPersona: La persona sobre la cual generar la lista
        Salidas:
        -return: La lista generada
        """
        return [funciones.traducirCodigo(persona[2]), funciones.traducirCodigo(persona[3]), persona[0], " ".join(persona[1])]

    columnas = ("Sede", "Carrera", "Cédula", "Nombre")

    repSedes = tk.Toplevel()
    repSedes.title("Reporte por cada sede")
    repSedes.configure(bg="white")
    repSedes.iconbitmap("logo-TEC.ico")
    repSedes.resizable(True, True)
    repSedes.grab_set()

    fPadron = sorted(padron, key = lambda x: int(str(x[2])+str(x[3])))
    
    numTabla = 0
    for codigoSede in codigos:
        if codigoSede in sedes.keys():
            tabla = generarTabla(repSedes, fPadron, columnas, limpiarEntrada, [lambda x: x[2] == codigoSede])
            tabla.grid(row=numTabla, column=0, sticky="nsew")
            archivos.guardarTexto(funciones.traducirCodigo(codigoSede).replace(" ", "_"), ".html", funciones.generarHTML(fPadron, columnas, limpiarEntrada, [lambda x: x[2] == codigoSede]))
            numTabla +=1

def tablaRepSede(pSede):
    """
    Funcionalidad: Muestra una tabla con la información de la sede proveida
    Entradas:
    -pSede: El nombre de la sede cuyo reporte se desea
    """
    columnas = ("Sede", "Carrera", "Cédula", "Nombre")

    repSede = tk.Toplevel()
    repSede.title("Reporte por sede")
    repSede.configure(bg="white")
    repSede.iconbitmap("logo-TEC.ico")
    repSede.resizable(True, True)
    repSede.grab_set()

    fPadron = sorted(padron, key = lambda x: int(str(x[2])+str(x[3])))

    tablaSede = generarTabla(repSede, padron, columnas, lambda x: [funciones.traducirCodigo(x[2]), funciones.traducirCodigo(x[3]), x[0], x[1]], [lambda x: funciones.traducirCodigo(x[2])==pSede])
    tablaSede.grid(row=0, column=0)
    archivos.guardarTexto(f"RepSede{pSede}".replace(" ", "_"), ".html", 
                          funciones.generarHTML(fPadron, columnas, lambda x: [funciones.traducirCodigo(x[2]), funciones.traducirCodigo(x[3]), x[0], " ".join(x[1])], [lambda x: funciones.traducirCodigo(x[2])==pSede]))

def reporteSede():
    """
    Funcionalidad: Muestar un menú para poder solicitar un reporte de una sede específica
    """
    def activarBotonSede(event):
        """
        Funcionalidad: Activa el botón para buscar solo si la sede a buscar no es vacía
        """
        if event.widget.get() != "":
            bConsultar.configure(state=tk.NORMAL)
        else:
            bConsultar.configure(state=tk.DISABLED)

    repSede = tk.Toplevel()
    repSede.title("Reporte por sede")
    repSede.configure(bg="white")
    repSede.iconbitmap("logo-TEC.ico")
    repSede.resizable(True, True)
    repSede.grab_set()

    sedes, codigos = archivos.leerSedes()

    opciones = [funciones.traducirCodigo(sede) for sede in sedes.keys()]
    cajaOpciones= ttk.Combobox(repSede, values=opciones)
    cajaOpciones.bind("<<ComboboxSelected>>", activarBotonSede)
    cajaOpciones.grid(row=0, column=0)
    bConsultar = Button(repSede, text="Consultar", state=tk.DISABLED ,width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=lambda : tablaRepSede(cajaOpciones.get()))
    bConsultar.grid(row=0,column=1)

def tablaRepCarrera(pCarrera):
    """
    Funcionalidad: Muestra una tabla con la información de la carrera proveida
    Entradas:
    -pSede: El nombre de la carrera cuyo reporte se desea
    """
    columnas = ("Sede", "Carrera", "Cédula", "Nombre")

    repCarrera = tk.Toplevel()
    repCarrera.title("Reporte por carrera")
    repCarrera.configure(bg="white")
    repCarrera.iconbitmap("logo-TEC.ico")
    repCarrera.resizable(True, True)
    repCarrera.grab_set()

    fPadron = sorted(padron, key = lambda x: int(str(x[2])+str(x[3])))

    tablaSede = generarTabla(repCarrera, padron, columnas, lambda x: [funciones.traducirCodigo(x[2]), funciones.traducirCodigo(x[3]), x[0], x[1]], [lambda x: funciones.traducirCodigo(x[3])==pCarrera])
    tablaSede.grid(row=0, column=0)
    archivos.guardarTexto(f"RepSede{pCarrera}".replace(" ", "_"), ".html", 
                          funciones.generarHTML(fPadron, columnas, lambda x: [funciones.traducirCodigo(x[2]), funciones.traducirCodigo(x[3]), x[0], " ".join(x[1])], [lambda x: funciones.traducirCodigo(x[3])==pCarrera]))

def reporteCarrera():
    """
    Funcionalidad: Muestar un menú para poder solicitar un reporte de una carrera específica
    """
    def activarBotonCarrera(event):
        """
        Funcionalidad: Activa el botón para buscar solo si la carrera a buscar no es vacía
        """
        if event.widget.get() != "":
            bConsultar.configure(state=tk.NORMAL)
        else:
            bConsultar.configure(state=tk.DISABLED)

    repCarrera = tk.Toplevel()
    repCarrera.title("Reporte por carrera")
    repCarrera.configure(bg="white")
    repCarrera.iconbitmap("logo-TEC.ico")
    repCarrera.resizable(True, True)
    repCarrera.grab_set()

    sedes, codigos = archivos.leerSedes()
    opciones = [funciones.traducirCodigo(carrera) for carreras in list(sedes.values()) for carrera in carreras]
    cajaOpciones= ttk.Combobox(repCarrera, values=opciones)
    cajaOpciones.bind("<<ComboboxSelected>>", activarBotonCarrera)
    cajaOpciones.grid(row=0, column=0)
    bConsultar = Button(repCarrera, text="Consultar", state = tk.DISABLED, width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=lambda : tablaRepCarrera(cajaOpciones.get()))
    bConsultar.grid(row=0,column=1)

def abrirReportes():
    """
    Muestra un menú con acceso a todos los posibles reportes
    """
    reportes = tk.Toplevel()
    reportes.title("Reportes")
    reportes.configure(bg="white")
    reportes.iconbitmap("logo-TEC.ico")
    reportes.resizable(False, False)
    reportes.geometry("540x650")
    reportes.grab_set()

    texto = Label(reportes, text="Reportes", bg="white", font=("Arial", 20))
    texto.grid(row=0, column=1, padx=200, pady=30)

    bGanador = Button(reportes, text="Reportar Ganador", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=reporteGanador)
    bGanador.configure(cursor="hand2")
    bGanador.grid(row=1, column=1)

    if len(padron)==0:
        bGanador.configure(state=tk.DISABLED)
    for persona in padron:
        if persona[-2] == None:
            bGanador.configure(state=tk.DISABLED)
            print("Disabled")
            break

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=2, column=1, padx=15)
    
    bRol = Button(reportes, text="Listado por rol", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=reporteRoles)
    bRol.configure(cursor="hand2")
    bRol.grid(row=3, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=2, column=1, padx=15)

    bSede = Button(reportes, text="Padrón por cada sede", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=reporteSedes)
    bSede.configure(cursor="hand2")
    bSede.grid(row=5, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=4, column=1, padx=15)

    bEstudiantil = Button(reportes, text="Padrón estudiantil por sede", width=20, height=2, font=("Arial", 10), activebackground="lightgreen", bg="lightblue", command=reporteSede)
    bEstudiantil.configure(cursor="hand2")
    bEstudiantil.grid(row=7, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=6, column=1, padx=15)

    bCarrera = Button(reportes, text="Padrón de votantes por carrera", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=reporteCarrera)
    bCarrera.configure(cursor="hand2")
    bCarrera.grid(row=9, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=8, column=1, padx=15)

    bAsociaciones = Button(reportes, text="Representantes de asociaciones", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=reporteAso)
    bAsociaciones.configure(cursor="hand2")
    bAsociaciones.grid(row=11, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=10, column=1, padx=15)

    bReporteBD = Button(reportes, text="Reporte total de la BD", width=20, height=2, font=("Arial", 10), activebackground="lightgreen",bg="lightblue", command=reporteTotal)
    bReporteBD.configure(cursor="hand2")
    bReporteBD.grid(row=13, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=12, column=1, padx=15)

    bSalir = Button(reportes, text="Salir", width=20, height=2, font=("Arial", 10), activebackground="lightgreen", bg="lightblue",command=reportes.destroy)
    bSalir.configure(cursor="hand2")
    bSalir.grid(row=15, column=1)

    texto = Label(reportes, text="", bg="white")
    texto.grid(row=14, column=1, padx=15)

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
        etiquetaPeriodo.config(text="",fg="gray")


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
            if int(pPeriodo[:4])>int(pPeriodo[5:]):
                return 2
            else:
                return 1
        else:
            return 3

    def activar(event):
        print("Alooo")
        etiquetaPeriodo.config(text="",fg="gray")
        if validarPeriodo(periodo.get())==1:
            bRegistrar.configure(state=tk.NORMAL)
            etiquetaPeriodo.config(text="")
        elif validarPeriodo(periodo.get())==3:
            etiquetaPeriodo.config(text="Formato:0000-0000",fg="gray")
            bRegistrar.configure(state=tk.DISABLED)
        else:
            etiquetaPeriodo.config(text="El primer año debe ser menor que el segundo",fg="gray")
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

bDB = Button(raiz, text="Respaldar BD", width=20, height=3, font=("Arial", 10), activebackground="lightpink", bg="lightblue", command= lambda: archivos.graba("padron", padron))
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

def salir():
    continuar=False

bSalir = Button(raiz, text="Salir", width=20, height=3, font=("Arial", 10), activebackground="lightpink", bg="lightblue", command=raiz.destroy)
bSalir.configure(cursor="hand2")
bSalir.grid(row=11, column=1)

texto = Label(raiz, text="", bg="white")
texto.grid(row=10, column=1, padx=15)

#def updateButtons():
#    print("hola")
#    raiz.after(1000, updateButtons)

#raiz.after(2000, lambda: print("hola"))
#raiz.after(1000, updateButtons)
#raiz.mainloop()

def activarCrearPadron():
    if padron != []:
        bPadron.configure(state=tk.DISABLED)
    else:
        bPadron.configure(state=tk.NORMAL)

def activarRector(pPadron,pBoton):
    contador=0
    for i in pPadron:
        if i[8]!=None:
            contador+=1
    if contador>=2:
        pBoton.configure(state=tk.NORMAL)
    else:
        pBoton.configure(state=tk.DISABLED)

def activarInsertar(pBoton):
    if padron != []:
        pBoton.configure(state=tk.NORMAL)
    else:
        pBoton.configure(state=tk.DISABLED)

raiz.protocol("WM_DELETE_WINDOW", lambda: print(""))
while True:
    #tk.tk.update_idletasks()
    if raiz.winfo_exists():
        raiz.update_idletasks()
        #estado de botones
        activarCrearPadron()
        activarInsertar(bCandidato)
        activarRector(padron,bRector)

        raiz.update()

#Reportes


  

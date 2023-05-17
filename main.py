import tkinter as tk

def CrearPadron():
    ...

def InsertarCandidato():
    ...

def ElegirRector():
    ...

def RespaldarBD():
    ...

def Reportes():
    ...

def Salir():
    exit()

window = tk.Tk()
window.geometry("400x400")

BTCrearPadron = tk.Button(text="Crear padrón", command=CrearPadron, )
BTCrearPadron.pack()

BTInsertarCandidato = tk.Button(text="Insertar Candidato", command=InsertarCandidato, state="disabled")
BTInsertarCandidato.pack()

BTElegirRector = tk.Button(text="Elegir Rector(a)", command=ElegirRector, state="disabled")
BTElegirRector.pack()

BTRespaldarBD = tk.Button(text="RespaldarBD", command=RespaldarBD, state="disabled")
BTRespaldarBD.pack()

BTReportes = tk.Button(text="Reportes", command=Reportes, state="disabled")
BTReportes.pack()

BTSalir = tk.Button(text="Salir", command=Salir)
BTSalir.pack()

window.mainloop()
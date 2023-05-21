from tkinter import *

raiz = Tk()
raiz.title("Sistema electoral")
raiz.configure(bg="white")
raiz.iconbitmap("logo-TEC.ico")
raiz.resizable(False,False)
raiz.geometry("650x600")

##frame1 = Frame(raiz)
##frame1.pack()
##frame1.pack(fill="both",expand="True")
##frame1.config(bg="white")

texto=Label(raiz,text="Elecciones de rectoria",bg="white",font=("Arial", 20))
texto.grid(row=0,column=1,padx=200,pady=30)

bPadron= Button(raiz,text="Crear padron",width=20, height=3,font=("Arial", 10),activebackground="lightpink",bg="lightblue")
bPadron.configure(cursor="hand2")
bPadron.grid(row=1,column=1)

bCandidato= Button(raiz,text="Insertar candidato",width=20, height=3,font=("Arial", 10),activebackground="lightpink",bg="lightblue")
bCandidato.configure(cursor="hand2")
bCandidato.grid(row=3,column=1)

texto=Label(raiz,text="",bg="white")
texto.grid(row=2,column=1,padx=15)

bCandidato= Button(raiz,text="Elegir rector(a)",width=20, height=3,font=("Arial", 10),activebackground="lightpink",bg="lightblue")
bCandidato.configure(cursor="hand2")
bCandidato.grid(row=5,column=1)

texto=Label(raiz,text="",bg="white")
texto.grid(row=4,column=1,padx=15)

bCandidato= Button(raiz,text="Respaldar BD",width=20, height=3,font=("Arial", 10),activebackground="lightpink",bg="lightblue")
bCandidato.configure(cursor="hand2")
bCandidato.grid(row=7,column=1)

texto=Label(raiz,text="",bg="white")
texto.grid(row=6,column=1,padx=15)

bCandidato= Button(raiz,text="Reportes",width=20, height=3,font=("Arial", 10),activebackground="lightpink",bg="lightblue")
bCandidato.configure(cursor="hand2")
bCandidato.grid(row=9,column=1)

texto=Label(raiz,text="",bg="white")
texto.grid(row=8,column=1,padx=15)

bCandidato= Button(raiz,text="Salir",width=20, height=3,font=("Arial", 10),activebackground="lightpink",bg="lightblue")
bCandidato.configure(cursor="hand2")
bCandidato.grid(row=11,column=1)

texto=Label(raiz,text="",bg="white")
texto.grid(row=10,column=1,padx=15)
raiz.mainloop()
  

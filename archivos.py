import pickle

def leerSedes():
    sedesDicc = {}
    codigos = {}
    with open("sedes.txt", encoding="utf-8") as sedes:
        for codigo, linea in enumerate(sedes.readlines()):
            linea = linea.replace("\n", "")
            codigos[codigo] = linea.replace("*", "")
            if linea[0] == "*":
                sede = codigo
                sedesDicc[sede] = []
            else:
                sedesDicc[sede].append(codigo)
    return sedesDicc, codigos

def leerAso():
    with open("RolesAso.txt", encoding="utf-8") as roles:
        return tuple([rol.replace("\n", "") for rol in roles.readlines()])

def leerAdm():
    with open("rolAdm.txt", encoding="utf-8") as roles:
        return [rol.replace("\n", "") for rol in ["Representante estudiantil"]+roles.readlines()]

def guardarTexto(pNombre, pExtension, pContenido):
    """
    Funcionalidad: Guarda un archivo de texto
    Entradas:
    -pNombre(str): El nombre del archivo
    -pExtension(str): La extensión del archivo
    -pContenido(str): El texto a guardar en el archivo
    Salidas:NA
    """
    with open(f"{pNombre}{pExtension}", "w", encoding="utf-8") as archivo:
        archivo.write(pContenido)

def cargarTexto(pNombre, pExtension):
    """
    Funcionalidad: Lee un archivo de texto
    Entradas:
    -pNombre(str): El nombre del archivo
    -pExtension(str): La extensión del archivo
    Salidas:
    -contenido(str): El contenido del archivo
    """
    with open(f"{pNombre}{pExtension}", "r", encoding="utf-8") as archivo:
        contenido=archivo.read()
    return contenido

def graba(nomArchGrabar, varGuardar):
    """
    Funcionalidad: Graba un archivo
    Entradas:
    -nomArchGrabar(str): Nombre del archivo a escribir
    -varGuardar(any): La variable a guardar
    Salidas: NA
    """
    try:
        f=open(nomArchGrabar,"wb")
        print("Grabando archivo: ", nomArchGrabar)
        pickle.dump(varGuardar,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee(nomArchLeer):
    #Función que lee un archivo con una lista de estudiantes
    """
    Funcionalidad: Lee un archivo
    Entradas:
    -nomArchGrabar(str): Nombre del archivo a leer
    Salidas: NA
    """
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        print("Leyendo archivo: ", nomArchLeer)
        lista = pickle.load(f)
        f.close()
    except FileNotFoundError:
        print("Archivo no encontrado: ", nomArchLeer)
    return lista

if __name__=="__main__":
    print(leerSedes())
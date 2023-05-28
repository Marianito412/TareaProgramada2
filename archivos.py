
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

if __name__=="__main__":
    print(leerSedes())
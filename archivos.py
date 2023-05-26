

def leerSedes():
    sedesDicc = {}
    codigos = {}
    with open("sedes.txt", encoding="utf-8") as sedes:
        for codigo, linea in enumerate(sedes.readlines()):
            linea = linea.replace("\n", "")
            codigos[codigo] = linea
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

if __name__=="__main__":
    print(leerSedes())
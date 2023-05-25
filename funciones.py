import random
import names
import archivos

DEBUG = True

def crearCedula(pPadron):
    cedulas = [persona[0] for persona in pPadron]
    while True:
        cedula = f"{random.randint(0,9)}-{random.randint(0, 9999):04}-{random.randint(0, 9999):04}"
        if cedula not in cedulas:
            return cedula

def crearCarnet(pPadron, pSede):
    carnets = [persona[6] for persona in pPadron]
    while True:
        carnet = f"{random.randint(2019, 2023)}{pSede:02}{random.randint(0,9999):04}"
        if int(carnet) not in carnets:
            return int(carnet)

def crearPadron(pPadron, pCantidad):
    sedes = archivos.leerSedes()[0]
    rolesAso = archivos.leerAso()
    rolesAdm = archivos.leerAdm()

    for i in range(pCantidad):
        cedula = crearCedula(pPadron)
        nombre = (names.get_first_name(), names.get_last_name(), names.get_last_name())
        sede = random.choice(list(sedes.keys()))
        carrera = random.choice(sedes[sede])
        rol = random.randint(1,3)
        
        if rol == 1:
            detalleRol = random.randint(0, len(rolesAso))
            carnet = crearCarnet(pPadron, sede)
        elif rol == 3:
            detalleRol = random.randint(0, len(rolesAdm))
            carnet = None
        else:
            detalleRol = None
            carnet = None
        voto = None
        candidato = None

        if DEBUG:
            print([cedula, nombre, sede, carrera, rol, detalleRol, carnet, voto, candidato])
        pPadron.append([cedula, nombre, sede, carrera, rol, detalleRol, carnet, voto, candidato])
    print(pPadron)
    return pPadron

def insertarCandidato(pPadron, pCedula):
    candidatos=[]
    flag=False
    for i in pPadron:
        if pCedula==i[0]:
            flag=True
            nombre=(f"{i[1][0]} {i[1][1]} {i[1][2]}")
            periodo="2022-2024"
            candidatos.append(pCedula)
            candidatos.append(nombre)
            candidatos.append(periodo)
    if flag==False:
         print("Esta persona no esta en el padron") 
    return candidatos



if __name__ == "__main__":
    crearPadron([], 10)
        
        



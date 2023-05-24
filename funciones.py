import random
import names
import archivos

DEBUG = False

codigosSedes = {}

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
    sedes, codigos = archivos.leerSedes()
    codigosSedes = codigos
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
    return pPadron

def filtrarPadron(pPadron, pCriterios: list = []):
    for persona in pPadron:
        if all([criterio(persona) for criterio in pCriterios]):
            yield persona

def traducirCodigo(pCodigo):
    return codigosSedes[pCodigo]

if __name__ == "__main__":
    test = crearPadron([], 10)
    codigosSedes = archivos.leerSedes()[1]
    #[lambda x: x[4] == 1]
    test = list(filtrarPadron(test))
    test = sorted(test, key = lambda x: int(str(x[2])+str(x[3])))
    for persona in test:    
        print(persona[0], traducirCodigo(persona[2]), traducirCodigo(persona[3]))


        
        



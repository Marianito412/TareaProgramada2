import random
import names
import archivos

DEBUG = False

codigosSedes = {}

codigosSedes = archivos.leerSedes()[1]
codigoRoles = archivos.leerAdm

def crearCedula(pPadron):
    """
    Funcionalidad: Crea una cédula única
    Entradas:
    -pPadron: El padron para verificar que la cédula sea única
    Salidas:
    -cedula: La cédula generada
    """
    cedulas = [persona[0] for persona in pPadron]
    while True:
        cedula = f"{random.randint(0,9)}-{random.randint(0, 9999):04}-{random.randint(0, 9999):04}"
        if cedula not in cedulas:
            return cedula

def crearCarnet(pPadron, pSede):
    """
    Funcionalidad: Crea un carnet único
    Entradas:
    -pPadron: El padron para verificar que el carnet sea único
    Salidas:
    -cedula: La cédula generada
    """
    carnets = [persona[6] for persona in pPadron]
    while True:
        carnet = f"{random.randint(2019, 2023)}{pSede:02}{random.randint(0,9999):04}"
        if int(carnet) not in carnets:
            return int(carnet)

def crearPadron(pPadron, pCantidad):
    """
    Funcionalidad: Crea un carnet único
    Entradas:
    -pPadron: El al cual agregar
    -pCantidad: La cantidad de personas a generar
    Salidas:
    -pPadron: el padrón modificado
    """
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
    print(pPadron)
    return pPadron

def elegirRector(pPadron):
    """
    Funcionalidad: Genera votaciones por cada candidato y guarda el voto en su respectiva celda
    Entradas:
    -pPadron: La lista de votantes
    Salidas:
    -pPadron: La lista de vontantes actualizada
    """
    candidatos=[]
    for i in pPadron:
        if i[8]!=None:
            candidatos.append(i[0])
    candidatos=tuple(candidatos)
    print(candidatos)
    for j in pPadron:
        elegido = random.choice(candidatos)
        print(elegido)
        j[7]=elegido
    return pPadron

def traducirCodigo(pCodigo):
    """
    Funcionalidad: Traduce los códigos de las sedes y carreras
    Entradas:
    -pCodigo: El código a traducir
    Salidas:
    -return: el código traducido
    """
    return codigosSedes[pCodigo]

def traducirDetalleRol(rol, detalleRol):
    """
    Funcionalidad: Traduce los detalles de roles
    Entradas:
    -pCodigo: El código a traducir
    Salidas:
    -return: el código traducido
    """
    if rol == 3:
        detalleRoles = archivos.leerAdm()
    elif rol == 1:
        detalleRoles = archivos.leerAso()
    else:
        return ""
    return detalleRoles[detalleRol-1]

def sanitizarInfo(pPersona):
    """
    Funcionalidad: Cambia la información de una persona a una forma facil de leer
    Entradas:
    -pPersona: La información a limpiar
    Salidas:
    -return: La información limpia
    """
    rol = ["Estudiante", "Docente", "Administrativo"][pPersona[4]-1]
    detalleRol = traducirDetalleRol(pPersona[4], pPersona[5])
    return [pPersona[0], " ".join(pPersona[1]), traducirCodigo(pPersona[2]), traducirCodigo(pPersona[3]), rol, detalleRol, pPersona[6], pPersona[7], pPersona[8]]

def filtrarPadron(pPadron, pCriterios: list = []):
    """
    Funcionalidad: Filtra el padrón basado en criterions
    Entradas:
    -pPadron: El padrón a filtrar
    -pCriterios: La lista de criterios a aplicar
    Salidas:
    -persona: una persona que cumple con los criterios
    """
    for persona in pPadron:
        if all([criterio(persona) for criterio in pCriterios]):
            yield persona

def insertarCandidato(pPadron, pCedula):
    """
    Funcionalidad: Registra una persona dada como candidato
    Entradas:
    -pPadron: La lista en la que buscar el posible candidato
    -pCedula: La cédula del candidato a registrar
    Salidas:
    -candidatos: La Persona registrada como candidato
    """
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

def registrarCandidato(pPadron, pCedula, pPeriodo):
    """
    Funcionalidad: Registra una persona como candidato
    Entradas:
    -pPadron: La lista en la que buscar el posible candidato
    -pCedula: La cédula del candidato a registrar
    -pPeriodo: El periodo en el que se servirá
    Salidas:NA
    """
    for persona in pPadron:
        if persona[0] == pCedula:
            persona[-1] = pPeriodo

def crearTag(pEtiqueta, pContenido, pAtributo=""):
    """
    Funcionalidad: Crea un string con formato html/xml válido
    Entradas:
    -pEtiqueta(str): El nombre de la etiqueta
    -pContenido(str): El contenido de esa etiqueta
    -pAtributo(str): Cualquier atributo deseado
    """
    pContenido = pContenido.replace("\n", "\n\t")
    return f"<{pEtiqueta} {pAtributo}>\n\t{pContenido}\n</{pEtiqueta}>"

def generarHTML(pPadron, pColumnas, limpiarAtributos, pFiltros):
    """
    Funcionalidad: Genera una tabla HTML
    Entradas:
    -pPadron: La lista de personas a incluir en la tabla
    -pColumnas: La lista de encabezados de la tabla
    -limpiarAtributos: Una función que prepara cada elemento de pPadron para ser agregado a la tabla
    -pFiltros: Lista de criterios a usar al recorrer el padrón
    Salidas:
    -plantilla: El HTML genedado
    """
    plantilla = archivos.cargarTexto("static/index", ".html")
    cabezeras = ""
    for columna in pColumnas:
        cabezeras+=crearTag("th", columna)
    tabla=""
    for persona in filtrarPadron(pPadron, pFiltros):
        fila = ""
        for atrubuto in limpiarAtributos(persona):
            fila += crearTag("td", str(atrubuto))
        fila=crearTag("tr", fila)
        tabla+=fila
    plantilla = plantilla.format(columnas = cabezeras, body=tabla)
    print(plantilla)
    return plantilla

def determinarGanador(pVotacion):
    """
    Funcionalidad: Determina el ganador de las votaciones
    Entradas:
    -pVotacion: El diccionario con los candidatos y sus respectivos votos
    Salidas:
    -return: El texto que indica el ganador o declara el empate
    """
    votacion = sorted(list(pVotacion.items()), key= lambda x: x[1], reverse=True)
    print(votacion[0])
    if votacion[0][1] >= sum(candidato[1] for candidato in votacion)*0.4:
        return f"Ganador: {votacion[0][0]}"
    else:
        return "Empate!"

if __name__ == "__main__":
    test = crearPadron([], 10)
    
    test = list(filtrarPadron(test))
    test = sorted(test, key = lambda x: int(str(x[2])+str(x[3])))
    for persona in test:    
        print(persona[0], traducirCodigo(persona[2]), traducirCodigo(persona[3]))
    generarHTML(test, ("Cédula", "Nombre", "Sede", "Carrera"), sanitizarInfo, [])


        
        



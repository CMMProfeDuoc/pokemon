def crearPkm (nombre:str,tipo:str,especie:str) -> dict:
    pkm = {
        'nombre':nombre,
        'tipo':tipo,
        'especie':especie,
        'hambre':50,
        'felicidad':50
    }
    return pkm

def savePkm (pkm:dict) -> None:
    nombre_archivo = str(pkm['nombre'])+'_'+str(pkm['especie'])+'_datos.pkm' 
    archivo = open(nombre_archivo, 'w')
    for v in pkm.values():
        archivo.write(str(v)+'\n')
    archivo.close()

def initPkm (nombre:str,tipo:str,especie:str) -> dict:
    pkm = crearPkm(nombre,tipo,especie)
    savePkm(pkm)
    return pkm

def loadPkm (nombre_archivo:str) -> dict:
    pass

def alimentar (pkm:dict, comida:int) -> None:
    pkm['hambre'] -= comida
    if (pkm['hambre'] < 0):
        pkm['hambre'] = 0
        

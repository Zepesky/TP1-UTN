# Consigna: Especializar las funciones de los puntos 1, 2 y 3 para hacerlas
# reutilizables. Agregar validaciones.
#
# Prototipo de referencia:
#   get_int(mensaje, mensaje_error, minimo, maximo, reintentos) -> int | None
#   get_float(mensaje, mensaje_error, minimo, maximo, reintentos) -> float | None
#   get_string(mensaje, mensaje_error, longitud_min, longitud_max) -> str | None
#
# - mensaje: texto que se imprime antes de pedir el dato.
# - mensaje_error: texto que se muestra si el dato es inválido.
# - minimo / maximo: valores límite admitidos (inclusive).
# - reintentos: cantidad de intentos antes de retornar None.


def pedir_entero(mensaje, mensaje_error, minimo, maximo, reintentos):
    intentos = 0
    
    while intentos < reintentos:
        
        entrada = input(mensaje)
        intentos += 1
        
        
        valido = True

        if len(entrada) == 0:
            valido = False

        inicio = 0
        if valido and entrada[0] == "-":
            inicio = 1
            if len(entrada) == 1:
                valido = False

        if valido:
            for i in range(inicio, len(entrada)):
                if entrada[i] < '0' or entrada[i] > '9':
                    valido = False
                    numero = int(entrada)
        
        if numero < minimo or numero > maximo:
            return False
        if valido :
            return int(entrada)
        else:
            print(mensaje_error)
            
    return None
        

def get_float(mensaje, mensaje_error, minimo, maximo, reintentos):
    pass

def get_string(mensaje, mensaje_error, longitud_min, longitud_max):
    pass

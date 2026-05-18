# Módulo Input.py
# Consigna: Crear las siguientes funciones para pedir datos por consola con
# validación. Utilizar las funciones de Validate.py para las validaciones.
#
# Prototipo:
#   get_int(mensaje, mensaje_error, minimo, maximo, reintentos) -> int | None
#   get_float(mensaje, mensaje_error, minimo, maximo, reintentos) -> float | None
#   get_string(mensaje, mensaje_error, longitud_min, longitud_max) -> str | None
#
# Parámetros:
#   mensaje       : texto que se imprime antes de pedir el dato.
#   mensaje_error : texto de error si el dato es inválido.
#   minimo        : valor mínimo admitido (inclusive).
#   maximo        : valor máximo admitido (inclusive).
#   reintentos    : cantidad de intentos antes de retornar None.
#
# Si no se obtiene un valor válido tras los reintentos, retornar None.

from Validate import validate_number, validate_length, validate_float

def get_int(mensaje, mensaje_error, minimo, maximo, reintentos) -> int | None:
    intentos = 0
    while intentos < reintentos:
        numero = input(mensaje)
        if validate_number(numero) == False:
            print(mensaje_error)
            intentos += 1
            continue
        if int(numero) < minimo or int(numero) > maximo:
            print(mensaje_error)
            intentos += 1
            continue
        return int(numero)
    return None

def get_float(mensaje, mensaje_error, minimo, maximo, reintentos):
    intentos = 0
    while intentos < reintentos:
        numero = input(mensaje)
        if validate_float(numero) == False:
            print(mensaje_error)
            intentos += 1
            continue
        if float(numero) < minimo or float(numero) > maximo:
            print(mensaje_error)
            intentos += 1
            continue
        return float(numero)
    return None

def get_string(mensaje, mensaje_error, longitud_min, longitud_max):
    while True:
        cadena = input(mensaje)
        if validate_length(cadena, longitud_min, longitud_max) == False:
            print(mensaje_error)
            continue
        return str(cadena)
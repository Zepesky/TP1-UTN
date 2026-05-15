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

from Validate import validate_number, validate_length

def get_int(mensaje, mensaje_error, minimo, maximo, reintentos):
    pass

def get_float(mensaje, mensaje_error, minimo, maximo, reintentos):
    pass

def get_string(mensaje, mensaje_error, longitud_min, longitud_max):
    pass

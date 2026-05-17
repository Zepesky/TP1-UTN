# Módulo Validate.py
# Consigna: Crear las siguientes funciones de validación que serán utilizadas
# por Input.py para verificar los datos ingresados por el usuario.


def validate_number(numero):
    
    if numero == "":
        return False
    inicio = 0
    if numero[0] == "-":
        inicio = 1
        if len(numero) == 1:
            return False
    
    for i in range(inicio, len(numero)):
        c = numero[i]
        if c < "0" or c > "9":
            return False
    return True

def validate_float(numero):
    
    if numero == "":
        return False

    inicio = 0
    if numero[0] == "-":
        inicio = 1 
        if len(numero) == 1:
            return False

    puntos = 0
    for i in range(inicio , len(numero)):
        if numero[i]== ".":
            puntos += 1
            if puntos > 1 or i == len(numero) - 1:
                return False
        elif numero[i] < "0" or numero[i] > "9":
            return False
    return True

def validate_length(cadena,longitud_min,longitud_max):
    
    if cadena == "":
        return False
    
    for i in range(len(cadena)):
        if not (("a" <= cadena[i] <= "z") or ("A" <= cadena[i] <= "Z") or cadena[i] == " "):
            return False
    
    if len(cadena) >= longitud_min and len(cadena) <= longitud_max:
        return True
    return False
    
    
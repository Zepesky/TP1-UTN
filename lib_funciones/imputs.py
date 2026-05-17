
def get_entero(mensaje, mensaje_error, minimo, maximo, reintentos):
    intentos = 0

    # repetir hasta agotar los reintentos
    while intentos < reintentos:

        entrada = input(mensaje)
        intentos += 1

        # inocente hasta que se demuestre lo contrario
        valido = True

        # validar que no esté vacío
        if len(entrada) == 0:
            valido = False

        # si empieza con '-', saltearlo al recorrer los dígitos
        inicio = 0
        if valido and entrada[0] == "-":
            inicio = 1
            if len(entrada) == 1:  # solo "-" no es válido
                valido = False

        # validar que todos los caracteres sean dígitos
        if valido:
            for i in range(inicio, len(entrada)):
                if entrada[i] < '0' or entrada[i] > '9':
                    valido = False

        # validar que el número esté dentro del rango
        if valido:
            numero = int(entrada)
            if numero < minimo or numero > maximo:
                valido = False

        # retornar si todo está bien, sino mostrar error y reintentar
        if valido:
            return numero
        else:
            print(mensaje_error)

    # se agotaron los intentos
    return None
        

def get_float(mensaje, mensaje_error, minimo, maximo, reintentos):
    intentos = 0
    # repetir hasta agotar los reintentos
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

        puntos = 0

        if valido:
            for i in range(inicio, len(entrada)):
                if entrada[i] == '.':
                    puntos += 1
                    if puntos > 1:
                        valido = False
                elif entrada[i] < "0" or entrada[i] > '9':
                    valido = False

        if valido:
            numero = float(entrada)
            if numero < minimo or numero > maximo:
                valido = False

        if valido:
            return numero
        else:
            print(mensaje_error)

    return None

def get_string(mensaje, mensaje_error, longitud_min, longitud_max):
    while True:
        entrada = input(mensaje)
        valido = True

        if len(entrada) == 0:
            valido = False

        if valido:
            for i in range(len(entrada)):
                if not (("a" <= entrada[i] <= "z") or ("A" <= entrada[i] <= "Z") or entrada[i] == " "):
                    valido = False
        
        if valido:
            if len(entrada) < longitud_min or len(entrada) > longitud_max:
                valido = False
        
        if valido:
            return str(entrada)
        else:
            print(mensaje_error)

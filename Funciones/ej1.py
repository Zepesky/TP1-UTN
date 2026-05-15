# Consigna: Crear una función que le solicite al usuario el ingreso de un número
# entero y lo retorne.

def pedir_entero(mensaje):
    
    while True:
        entrada = input(mensaje)

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

        if valido:
            return int(entrada)
        else:
            print("Error: ingresa un numero valido")
# Consigna: Crear una función que le solicite al usuario el ingreso de un número
# flotante y lo retorne.

def pedir_float(mensaje):
    while True:
        entrada = input(mensaje)

        valido = True #inocente hasta q de demuestre lo contrario

        if len(entrada) == 0 or entrada == '' or entrada == '-' or entrada == '.':
            valido = False

        inicio = 0

        if valido and entrada[0] == '-':
            inicio = 1
            
        puntos = 0 
        
        if valido:
            for i in range(inicio , len(entrada)):
                if entrada[i] == ".":
                    puntos += 1
                    if puntos > 1:
                        valido = False
                elif entrada[i] < '0' or entrada[i] > '9':
                    valido = False
        
        if valido:
            return float(entrada)
        else:
            print("Error: ingresá un float válido.")
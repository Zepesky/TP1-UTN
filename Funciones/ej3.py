# Consigna: Crear una función que le solicite al usuario el ingreso de una cadena
# y la retorne.

def pedir_cadena(mensaje):
    
    while True:
        entrada = input(mensaje)

        valido = True

        if entrada == "":
            valido = False
            
        if valido:
            for i in range(len(entrada)):
                if not (("a" <= entrada[i] <= "z") or ("A" <= entrada[i] <= "Z") or entrada[i] == ' '):
                    valido = False
        
        if valido:
            return str(entrada)
        else:
            print("Error: ingresá solo letras.")
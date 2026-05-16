# Consigna: Crear una función que imprima la tabla de multiplicar de un núm   ero
# recibido como parámetro. La función debe aceptar parámetros opcionales (inicio
# y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

def tabla_multiplicar(numero, inicio=1, fin=10):
    for i in range(inicio, fin + 1):
        print(numero, "x" , i , "=", numero * i)

tabla_multiplicar(5)
tabla_multiplicar(3, 3, 7)
tabla_multiplicar(7, fin=15)

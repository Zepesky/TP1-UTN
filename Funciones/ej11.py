# Consigna: Crear una función que (utilizando el algoritmo del ejercicio de la
# guía de for), muestre todos los números primos comprendidos entre la unidad y
# un número ingresado como parámetro. La función retorna la cantidad de números
# primos encontrados. Modularizar todo lo posible.
#
# Tip: reutilizar la función es_primo() del ejercicio anterior.

from ej10 import es_primo
from Funciones import pedir_entero

def mostrar_primos(limite):
    contador_primos = 0

    for numero in range(1, limite + 1):
        if es_primo(numero):
            print(numero)
            contador_primos += 1 

        return contador_primos        
    

limite = pedir_entero("Ingrese un limite")
total = mostrar_primos(limite)

print(f"la cantidad de primos ingresados: {total}")
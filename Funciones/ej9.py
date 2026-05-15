# Consigna: Diseña una función que calcule la potencia de un número.
# La función debe recibir la base y el exponente como argumentos y devolver el resultado.

from funciones import pedir_entero

def potencia(base, exponente):
    return base ** exponente


base = int(pedir_entero("Ingrese un valor para la base:"))
exponente = int(pedir_entero("Ingrese un valor para el exponente "))

respuesta = potencia(base, exponente)

print(f"la base {base} elevado a la {exponente} es igual a: {respuesta}")
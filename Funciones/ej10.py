# Consigna: Crear una función que reciba un número y retorne True si el número
# es primo, False en caso contrario.

from funciones import pedir_entero

def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0: 
            return False
    

    return True

# Consigna: Escribe una función que calcule el área de un círculo.
# La función debe recibir el radio como parámetro y devolver el área.

from funciones import pedir_float 

def area_circulo(radio):
    
    pi = 3.14149
    
    radio = float(pedir_float("Ingrese el radio: "))
    
    area = pi * float(radio) ** 2
    
    print(f"el area es {area}")
    
    

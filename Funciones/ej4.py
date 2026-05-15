# Consigna: Escribir una función que calcule el área de un rectángulo.
# La función recibe la base y la altura y retorna el área.

from funciones import pedir_float 

def area_rectangulo(base, altura):
    
    base = float(pedir_float("Base: "))
    
    altura = float(pedir_float("Altura: "))
    
    area = base * altura
    
    print(f"El area es: {area}")

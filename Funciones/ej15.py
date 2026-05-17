# Consigna: Realizar una función recursiva que calcule la potencia de un número.
#
# Ejemplo:
#   potencia(2, 3) -> 2^3 = 8
#
# Caso base: potencia(base, 0) = 1
# Caso recursivo: potencia(base, exp) = base * potencia(base, exp - 1)

def potencia(base, exponente):
    
    if exponente == 0:
        return 1
    
    return base * potencia(base, exponente - 1)


resultado = potencia(2, 4)

print(resultado)
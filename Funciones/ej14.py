# Consigna: Realizar una función recursiva que calcule la suma de los primeros
# n números naturales.
#
# Ejemplo:
#   suma_naturales(5) -> 1 + 2 + 3 + 4 + 5 = 15
#
# Caso base: suma_naturales(1) = 1
# Caso recursivo: suma_naturales(n) = n + suma_naturales(n - 1)

def suma_naturales(n: int) -> int:
    
    if n == 1:
        return 1
    return n + suma_naturales(n - 1)

resultado = suma_naturales(5)

print(resultado)

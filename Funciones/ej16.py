# Consigna: Realizar una función recursiva que permita realizar la suma de los
# dígitos de un número.
#
# Ejemplo:
#   suma_digitos(1234) -> 1 + 2 + 3 + 4 = 10
#
# Caso base: suma_digitos(n) = n  cuando n < 10
# Caso recursivo: suma_digitos(n) = (n % 10) + suma_digitos(n // 10)



def suma_digitos(numero):
    
    if numero < 10:
        return numero
    
    return (numero % 10) + suma_digitos(numero // 10)
        

resultado = suma_digitos(1234)

print(resultado)
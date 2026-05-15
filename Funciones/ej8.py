# Consigna: Define una función que encuentre el máximo de tres números.
# La función debe aceptar tres argumentos y devolver el número más grande.

def maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c



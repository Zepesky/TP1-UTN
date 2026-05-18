# Consigna: Realizar una función para calcular el número de Fibonacci de un
# número ingresado por consola.
#
# Definición:
#   La sucesión de Fibonacci comienza con los números 0 y 1, y cada número
#   subsecuente es la suma de los dos anteriores:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# Prototipo:
#   fibonacci(n) -> int
#
# Caso base: fibonacci(0) = 0 | fibonacci(1) = 1
# Caso recursivo: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

resultado = fibonacci(10)

print(resultado)

# Consigna: Crea una función que verifique si un número dado es par o impar.
# La función debe IMPRIMIR un mensaje indicando si el número es par o impar.

def es_par_o_impar(numero):
    
    if numero %2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

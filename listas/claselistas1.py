# lista = [5,9,7]

# print(id(lista))

# for i in range(len(lista)):
#     print(id(lista[i]))

#################################################

def cargar_lista(lista: list, limite: int) -> bool:
    cargo = False
    if type(lista) == list and type(limite) == int and limite > 0:
        cargo = True
        for i in range(0, limite, 1):
            numero = int(input("ingrese numero: "))
            lista.append(numero)
        return cargo

def mostrar_lista(lst):
    for i in range(len(lst)):
        print(lst[i])

def sumar_lista(lista: list):
    suma = None 
    if type(lista) == list and verificar_tipo_entero(lista) == True:
        suma = 0
        for i in range(len(lista)):
            suma += lista[i]
    return suma

def verificar_tipo_entero(lista: list):
    exito = True
    for i in range(len(lista)):
        if type(lista[i]) != int:
            exito = False
            break
    return exito

#################################################

lista = []
suma = sumar_lista(lista)
if suma != None:
    print(suma)
else:
    print("No se pudo sumar")

###################################################

# if cargar_lista(lista, 3) == True: 
#     mostrar_lista(lista)
#     suma = sumar_lista(lista)
#     print(f"La suma es {suma}")
# else:
#     print("error.")

###################################################

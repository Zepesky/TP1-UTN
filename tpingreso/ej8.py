#Cree un programa que permite ingresar el nombre de un producto, el
#precio y que calcule el IVA.

producto = str(input("Nombre del producto: "))

precio = float(input("Precio del producto: "))

iva = 1.21

print("su producto es", (producto), "con un precio de", (precio))

calulo = input("¿Desea calcular el IVA(21%) del mismo? (s/n): ")

if calulo == "s":
    print("Su producto con el IVA(21%) es:", precio * iva)
else:
    print("Adios!")
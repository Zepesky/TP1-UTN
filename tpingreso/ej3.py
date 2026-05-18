#Cree un programa que pida el nombre, el apellido, edad del usuario y luego muestre por consola los datos ingresados

print("""
=============
    DATOS
=============
 1. NOMBRE
 2. APELLIDO
 3. EDAD
=============
""")

nombre = str(input("Escribe tu nombre: "))

apellido = str(input("Escribe tu apellido: "))

edad = int(input("Escribe tu edad: "))

print("tus datos son:")

print(nombre)
print(apellido)
print(edad)

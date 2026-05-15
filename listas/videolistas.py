
def mostrar_un_empleado(nombre, apellido, sueldo, legajo):
            print(f"{nombre[i]:<10}{apellido[i]:<10}{sueldo[i]:7}{legajo[i]:5}")


def mostrar_empleados(nombres: list, apellidos: list, suedos: list, legajos: list):
    for i in range(len(nombres)):
        mostrar_empleados(nombres[i], apellidos[i], suedos[i], legajos[i])

def buscar_empleado(legajo_buscado, nombre, apellido, sueldos, legajo):
    for i in range(len(legajo)):
        if legajo[i] == legajo_buscado:
            print("Empleado encontrado")
            mostrar_empleados(nombres[i], apellidos[i], sueldos[i], legajos[i])
            break

def contar_empleados(puesto):
    cont_programador = 0
    cont_analista = 0
    cont_qa = 0
    
    for i in range(puesto):
        if puesto[i] == "Programador":
            cont_programador += 1
        elif puesto[i] == "Analista":
            cont_analista += 1
        elif puesto[i] == "QA":
            cont_qa += 1
        else:
            
    

    
nombres = ["Ana", "Luis", "Carla"]

apellidos = ["Gomez", "Perez", "Lopez",]

sueldos = ["25000", "35000", "28000"]

legajos = ["1355", "1342", "1003"]

puesto = ["Analista", "programador", "QA"]

# for i in range(3):
#     nombres = input("nombre: ")
#     apellidos =  input("apellido: ")
#     sueldos = int(input("sueldo: "))
#     legajos = int(input("legajos: "))
    
#     nombres.append(nombres)
#     apellidos.append(apellidos)
#     sueldos.append(sueldos)
#     legajos.appedn(legajos)
        


buscando = int(input("legajo: "))

for i in range(len(legajos)):
    
    if legajos[i] == buscando:
        print(nombres[i], apellidos[i])
        print(sueldos[i])
        break
    
# ventajas

# facil de entender
# refuerza el uso de indices 
# de alguna manera mas eficiente en memoria, no usa tanta
# contol total

# deventajas

# riesgo de disincronacion
# dificilies de mantener
# poca flexibilidad
# propensa a errores
# no escala bien
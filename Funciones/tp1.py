def get_nombre_disciplina(disciplina):
    if disciplina == 1:
        return "Atletismo"
    elif disciplina == 2:
        return "Natacion"
    return "Ciclismo"

def calcular_imc(peso, altura):
    return peso / (altura * altura)

def categoria_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    return "Obesidad"

def determinar_condicion(puntaje, edad, imc):
    if puntaje >= 80 and edad >= 18 and edad <= 30 and imc >= 18.5 and imc <= 27:
        return "Apto directo"
    elif puntaje >= 60 and ((edad >= 31 and edad <= 40) or (imc > 27 and imc <= 30) or (puntaje >= 60 and puntaje <= 79)):
        return "Apto con seguimiento"
    return "No apto"

def imprimir_resultado(nombre, disciplina, imc, categoria, condicion):
    print("\n--- RESULTADO DEL ASPIRANTE ---")
    print("Nombre:", nombre)
    print("Disciplina:", disciplina)
    print("IMC:", round(imc, 2))
    print("Categoria corporal:", categoria)
    print("Condicion final:", condicion)

def informe(total, suma_edad, suma_puntaje, cant_apto_directo, cant_apto_seguimiento,
            cant_no_apto, mayor_puntaje, nombre_mayor, disciplina_mayor,
            cant_atletismo, cant_natacion, cant_ciclismo, cant_peso_normal, cant_mayores25_y_70):
    print("\n========== INFORME FINAL ==========")

    if total == 0:
        print("No se ingresaron aspirantes.")
        return

    promedio_edad = suma_edad / total
    promedio_puntaje = suma_puntaje / total

    porcentaje_atletismo = cant_atletismo * 100 / total
    porcentaje_natacion = cant_natacion * 100 / total
    porcentaje_ciclismo = cant_ciclismo * 100 / total

    print("Total de aspirantes:", total)
    print("Promedio de edad:", round(promedio_edad, 2))
    print("Promedio de puntaje fisico:", round(promedio_puntaje, 2))

    print("Cantidad de aptos directos:", cant_apto_directo)
    print("Cantidad de aptos con seguimiento:", cant_apto_seguimiento)
    print("Cantidad de no aptos:", cant_no_apto)

    print("Mayor puntaje:", mayor_puntaje)
    print("Nombre del mayor puntaje:", nombre_mayor)
    print("Disciplina del mayor puntaje:", disciplina_mayor)

    print("Porcentaje Atletismo:", round(porcentaje_atletismo, 2), "%")
    print("Porcentaje Natacion:", round(porcentaje_natacion, 2), "%")
    print("Porcentaje Ciclismo:", round(porcentaje_ciclismo, 2), "%")

    print("Cantidad con peso normal:", cant_peso_normal)
    print("Mayores de 25 con mas de 70 puntos:", cant_mayores25_y_70)

    print("\n--- GRAFICOS TEXTUALES ---")
    print("Aptos directos:", end=" ")
    for i in range(cant_apto_directo):
        print("*", end="")
    print()

    print("Aptos con seguimiento:", end=" ")
    for i in range(cant_apto_seguimiento):
        print("*", end="")
    print()

    print("No aptos:", end=" ")
    for i in range(cant_no_apto):
        print("*", end="")
    print()


# Acumuladores
total_aspirantes = 0
suma_edad = 0
suma_puntaje = 0
cant_apto_directo = 0
cant_apto_seguimiento = 0
cant_no_apto = 0
cant_atletismo = 0
cant_natacion = 0
cant_ciclismo = 0
cant_peso_normal = 0
cant_mayores25_y_70 = 0
mayor_puntaje = -1
nombre_mayor_puntaje = ""
disciplina_mayor_puntaje = ""

continuar = "si"

while continuar == "si":
    print("\n--- INGRESO DE ASPIRANTE ---")

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (F/M/X): ")
    altura = float(input("Altura en metros: "))
    peso = float(input("Peso en kg: "))
    disciplina = int(input("Disciplina (1-Atletismo, 2-Natacion, 3-Ciclismo): "))
    puntaje = int(input("Puntaje fisico (0 a 100): "))

    nombre_disc = get_nombre_disciplina(disciplina)
    if disciplina == 1:
        cant_atletismo += 1
    elif disciplina == 2:
        cant_natacion += 1
    else:
        cant_ciclismo += 1

    imc = calcular_imc(peso, altura)
    categoria = categoria_imc(imc)
    condicion = determinar_condicion(puntaje, edad, imc)

    if categoria == "Peso normal":
        cant_peso_normal += 1

    if condicion == "Apto directo":
        cant_apto_directo += 1
    elif condicion == "Apto con seguimiento":
        cant_apto_seguimiento += 1
    else:
        cant_no_apto += 1

    if edad > 25 and puntaje > 70:
        cant_mayores25_y_70 += 1

    if puntaje > mayor_puntaje:
        mayor_puntaje = puntaje
        nombre_mayor_puntaje = nombre
        disciplina_mayor_puntaje = nombre_disc

    total_aspirantes += 1
    suma_edad += edad
    suma_puntaje += puntaje

    imprimir_resultado(nombre, nombre_disc, imc, categoria, condicion)

    continuar = input("\nDesea ingresar otro aspirante? (si/no): ")

informe(total_aspirantes, suma_edad, suma_puntaje, cant_apto_directo, cant_apto_seguimiento,
        cant_no_apto, mayor_puntaje, nombre_mayor_puntaje, disciplina_mayor_puntaje,
        cant_atletismo, cant_natacion, cant_ciclismo, cant_peso_normal, cant_mayores25_y_70)

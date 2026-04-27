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

    # Determinar nombre de disciplina y acumular
    if disciplina == 1:
        nombre_disciplina = "Atletismo"
        cant_atletismo += 1
    elif disciplina == 2:
        nombre_disciplina = "Natacion"
        cant_natacion += 1
    else:
        nombre_disciplina = "Ciclismo"
        cant_ciclismo += 1

    # Calculo IMC
    imc = peso / (altura * altura)

    
    def categoria():
        # Categoria corporal
        if imc < 18.5:
            categoria = "Bajo peso"
        elif imc < 25:
            categoria = "Peso normal"
            cant_peso_normal += 1
        elif imc < 30:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"

        return categoria

    # Condicion final
    if puntaje >= 80 and edad >= 18 and edad <= 30 and imc >= 18.5 and imc <= 27:
        condicion = "Apto directo"
        cant_apto_directo += 1
    elif puntaje >= 60 and ((edad >= 31 and edad <= 40) or (imc > 27 and imc <= 30) or (puntaje >= 60 and puntaje <= 79)):
        condicion = "Apto con seguimiento"
        cant_apto_seguimiento += 1
    else:
        condicion = "No apto"
        cant_no_apto += 1

    # Contador especial
    if edad > 25 and puntaje > 70:
        cant_mayores25_y_70 += 1

    # Mayor puntaje
    if puntaje > mayor_puntaje:
        mayor_puntaje = puntaje
        nombre_mayor_puntaje = nombre
        disciplina_mayor_puntaje = nombre_disciplina



    # Acumuladores generales
    total_aspirantes += 1
    suma_edad += edad
    suma_puntaje += puntaje

    # Salida individual
    print("\n--- RESULTADO DEL ASPIRANTE ---")
    print("Nombre:", nombre)
    print("Disciplina:", nombre_disciplina)
    print("IMC:", round(imc, 2))
    print("Categoria corporal:", categoria)
    print("Condicion final:", condicion)

    continuar = input("\nDesea ingresar otro aspirante? (si/no): ")

# Informe final
def informe():
    print("\n========== INFORME FINAL ==========")

    if total_aspirantes > 0:
        promedio_edad = suma_edad / total_aspirantes
        promedio_puntaje = suma_puntaje / total_aspirantes

        porcentaje_atletismo = cant_atletismo * 100 / total_aspirantes
        porcentaje_natacion = cant_natacion * 100 / total_aspirantes
        porcentaje_ciclismo = cant_ciclismo * 100 / total_aspirantes

        print("Total de aspirantes:", total_aspirantes)
        print("Promedio de edad:", round(promedio_edad, 2))
        print("Promedio de puntaje fisico:", round(promedio_puntaje, 2))

        print("Cantidad de aptos directos:", cant_apto_directo)
        print("Cantidad de aptos con seguimiento:", cant_apto_seguimiento)
        print("Cantidad de no aptos:", cant_no_apto)

        print("Mayor puntaje:", mayor_puntaje)
        print("Nombre del mayor puntaje:", nombre_mayor_puntaje)
        print("Disciplina del mayor puntaje:", disciplina_mayor_puntaje)

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

    else:
        print("No se ingresaron aspirantes.")
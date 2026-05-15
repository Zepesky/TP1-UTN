from colorama import *

init(autoreset=True)
ancho = 36
bandera = True
pacientes = 0
masculinos = 0
femeninos = 0
#variables maximas
max_temperatura = 0
temp_max_edad = 0
temp_max_nombre = ""
temp_max_genero = ""
temp_max_ingreso = ""

max_presion = 0
pres_max_edad = 0
pres_max_nombre = ""
pres_max_genero = ""
pres_max_ingreso = ""

max_dolor = 0
dolor_max_edad = 0
dolor_max_nombre = ""
dolor_max_genero = ""
dolor_max_ingreso = ""

max_frec_cardiaca = 0
frec_cardiaca_max_edad = 0
frec_cardiaca_max_nombre = ""
frec_cardiaca_max_genero = ""
frec_cardiaca_max_ingreso = ""

#variables minimas
min_temperatura = 0
temp_min_edad = 0
temp_min_nombre = ""
temp_min_genero = ""
temp_min_ingreso = ""

min_presion = 0
pres_min_edad = 0
pres_min_nombre = ""
pres_min_genero = ""
pres_min_ingreso = ""

min_dolor = 0
dolor_min_edad = 0
dolor_min_nombre = ""
dolor_min_genero = ""
dolor_min_ingreso = ""

min_frec_cardiaca = 0
frec_min_edad = 0
frec_min_nombre = ""
frec_min_genero = ""
frec_min_ingreso = ""

#contadores
suma_temperatura = 0
suma_presion = 0
suma_dolor = 0
suma_frec_cardiaca = 0
suma_edades = 0
casos_criticos_pediatricos = 0
casos_criticos = 0
A_pos = 0
A_neg = 0
B_pos = 0
B_neg = 0
AB_pos = 0
AB_neg = 0
O_pos = 0
O_neg = 0

#Entradas...
while bandera:
    print(f"┌{'─' * ancho}┐")
    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")
    print(f"│  {'Bienvenido!':<34}│")
    print(f"└{'─' * ancho}┘")
    
    print(f"┌{'─' * ancho}┐")
    print(f"│  {'Cantidad de pacientes':<9} →  {(pacientes):<9}│")
    print(f"├{'─' * ancho}┤")
    print(f"│  {'Pediatria Urgencia':<9} →  {(casos_criticos_pediatricos):<12}│")
    print(f"│  {'Guardia urgencia':<9} →  {(casos_criticos):<14}│")
    print(f"└{'─' * ancho}┘")

    print(f"┌{'─' * ancho}┐")
    print(f"│ {Fore.GREEN} {'1'} →  {"Archivo de pacientes":<28} {Style.RESET_ALL}│")
    print(f"│ {Fore.GREEN} {'2'} →  {"Estadisticas":<28} {Style.RESET_ALL}│")
    print(f"└{'─' * ancho}┘")
    
    while True:
        try:
            operacion = int(input(f"{Fore.GREEN}|>Que operacion desea realizar: {Style.RESET_ALL}"))
            if operacion < 1 or operacion > 2:
                print(f"{Back.RED} |⚠ -Ingrese una opcion valida del menu. {Style.RESET_ALL}")
                continue
            break  
        
        except ValueError:
            print(f"{Back.RED} |⚠ -Ingrese un valor valido. {Style.RESET_ALL}")
    
    if operacion == 1:
        #archivo de paciente:
        while True:
            
            #Datos doctor
            doctor = input(Fore.MAGENTA + "|>Doctor a cargo: " + Style.RESET_ALL)

            #paciente
            ingreso = input(Fore.GREEN + "|>Hora de ingreso 24HS: "+ Style.RESET_ALL)
            nombre_paciente = input(Fore.GREEN + "|>Nombre del paciente: "+ Style.RESET_ALL)
            apellido_paciente = input(Fore.GREEN + "|>Apellido: "+ Style.RESET_ALL)
            while True:
                try:
                    edad_paciente = int(input(Fore.GREEN + "|>Edad: " + Style.RESET_ALL))
                    if edad_paciente <= 0:
                        print(f"{Back.RED} |⚠ -La edad debe ser mayor a 0. {Style.RESET_ALL}")
                        continue
                    break
                except ValueError:
                    print(f"{Back.RED} |⚠ -¡Ingrese un número válido para la edad! {Style.RESET_ALL}")
                    
            genero = input(Fore.GREEN + "|-Género: (Femenino/Masculino/Otro): "+ Style.RESET_ALL)
            sangre = input(Fore.GREEN + "|-Tipo de Sangre: [A,B,AB,0][+ -]: "+ Style.RESET_ALL)
            while True:
                try:
                    kilos = float(input(Fore.GREEN + "|-Ingrese su peso: " + Style.RESET_ALL))
                    if kilos <= 0:
                        print(f"{Back.RED} El peso debe ser mayor a 0 {Style.RESET_ALL}")
                        continue   
                    break
                except ValueError:
                    print(f"{Back.RED} |⚠ -¡Ingrese un peso válido! {Style.RESET_ALL}")      

            while True:
                try:
                    temperatura = float(input(Fore.YELLOW +"|Temperatura del paciente: "+ Style.RESET_ALL))
                    if temperatura < 0:
                        print(f"{Back.RED} |⚠ -¡La temperatura no puede ser negativa! {Style.RESET_ALL}")
                        
                        continue
                    break
                except ValueError:
                    print(f"{Back.RED} |⚠ -¡Ingrese una temperatura válida! {Style.RESET_ALL}")    

            while True:
                try:
                    frecuencia_cardiaca = float(input(Fore.YELLOW +"|Frecuencia cardíaca: "+ Style.RESET_ALL))
                    if frecuencia_cardiaca == 0:
                        print(f"{Back.RED} |⚠ -La frecuencia cardíaca no puede ser 0 {Style.RESET_ALL}") 
                        continue    
                    break
                except ValueError:
                    print(f"{Back.RED} |⚠ -Ingrese un valor numérico válido {Style.RESET_ALL}") 

            while True:
                try:
                    presion = float(input(Fore.YELLOW +"|Presión arterial: "+ Style.RESET_ALL))
                    if presion <= 0:
                        print(f"{Back.RED} |⚠ -La presión arterial no puede ser 0 {Style.RESET_ALL}")
                        continue
                    break
                except ValueError:
                    print(f"{Back.RED} |⚠ -Ingrese un valor numérico válido {Style.RESET_ALL}")

            while True:
                try:
                    dolor = int(input(Fore.YELLOW +"|Escala de dolor (0-10): "+ Style.RESET_ALL))
                    if 0 <= dolor <= 10:
                        break
                except ValueError:
                    print(f"{Back.RED} |⚠ -Ingrese un valor numérico válido {Style.RESET_ALL}")

            #Categoricas
            tos = str(input(Fore.YELLOW +"|-¿Presenta tos? (sí/no): "+ Style.RESET_ALL))
            
            while True:
                try:
                    respiracion = int(input(Fore.YELLOW + """|-Respiración:  
|   1. Normal
|   2. Agitada
|   3. Irregular
|   4. Dolor
|--> """ + Style.RESET_ALL))

                    if respiracion < 1 or respiracion > 4:
                        print(f"{Back.RED} |⚠ -Ingrese un número entre 1 y 4 {Style.RESET_ALL}")
                        continue
                    break 
                except ValueError:
                    print(f"{Back.RED} |⚠ -Ingrese un valor numérico válido {Style.RESET_ALL}")

            vomitos = str(input(Fore.YELLOW +"|-Vómitos: (sí/no): "+ Style.RESET_ALL))
            medicamentos = str(input(Fore.YELLOW +"|-Toma medicación? (sí/no): "+ Style.RESET_ALL))
            ejercicio = str(input(Fore.YELLOW + "|-¿Hace ejercicio? (sí/no): "+ Style.RESET_ALL))
            #calculos

            fiebre = temperatura >= 38
            taquicardia = frecuencia_cardiaca > 100
            presion_alta = presion > 140

            riesgo_edad = edad_paciente > 60
            dolor_alto = dolor >= 7
            dolor_extremo = dolor >= 9

            resp_agitada = respiracion == 2
            resp_dolorosa = respiracion == 4

            posible_infeccion = fiebre and tos in ["s","si","sí"]
            estado_critico = fiebre and taquicardia
            riesgo_cardiovascular = presion_alta and edad_paciente > 50
            agua_por_peso = kilos * 30
            agua_act_fisica = 0
            clima_agua = 0

            #-------------------
            if respiracion == 1:
                respiracion_str = "Normal"
            elif respiracion == 2:
                respiracion_str = "Agitada"
            elif respiracion == 3:
                respiracion_str = "Irregular"
            elif respiracion == 4:
                respiracion_str = "Con dolor"
            else:
                respiracion_str = "Desconocida"
            #--------------------
            #contadores
            if genero == "masculino" or genero == "m":
                masculinos += 1
            if genero == "femenino" or genero == "f":
                femeninos += 1
            #--------------------
            #Maximos
            if temperatura > max_temperatura:
                max_temperatura = temperatura
                temp_max_nombre = nombre_paciente + " " + apellido_paciente
                temp_max_genero = genero
                temp_max_edad = edad_paciente
                temp_max_ingreso = ingreso

            if presion > max_presion:
                max_presion = presion
                pres_max_nombre = nombre_paciente + " " + apellido_paciente
                pres_max_genero = genero
                pres_max_edad = edad_paciente
                pres_max_ingreso = ingreso

            if dolor > max_dolor:
                max_dolor = dolor
                dolor_max_nombre = nombre_paciente + " " + apellido_paciente
                dolor_max_genero = genero
                dolor_max_edad = edad_paciente
                dolor_max_ingreso = ingreso

            if frecuencia_cardiaca > max_frec_cardiaca:
                max_frec_cardiaca = frecuencia_cardiaca
                frec_cardiaca_max_nombre = nombre_paciente + " "+ apellido_paciente
                frec_cardiaca_max_genero = genero
                frec_cardiaca_max_edad = edad_paciente
                frec_cardiaca_max_ingreso = ingreso
            #--------------------
            #Minimos
            if min_temperatura == 0 or temperatura < min_temperatura:
                min_temperatura = temperatura
                temp_min_nombre = nombre_paciente + " " + apellido_paciente
                temp_min_genero = genero
                temp_min_edad = edad_paciente
                temp_min_ingreso = ingreso

            if min_presion == 0 or presion < min_presion:
                min_presion = presion
                pres_min_nombre = nombre_paciente + " "+apellido_paciente
                pres_min_genero = genero
                pres_min_edad = edad_paciente
                pres_min_ingreso = ingreso

            if min_dolor == 0 or dolor < min_dolor:
                min_dolor = dolor
                dolor_min_nombre = nombre_paciente + " " +apellido_paciente
                dolor_min_genero = genero
                dolor_min_edad = edad_paciente
                dolor_min_ingreso = ingreso

            if min_frec_cardiaca == 0 or frecuencia_cardiaca < min_frec_cardiaca:
                min_frec_cardiaca = frecuencia_cardiaca
                frec_min_nombre = nombre_paciente + " " +apellido_paciente
                frec_min_genero = genero
                frec_min_edad = edad_paciente
                frec_min_ingreso = ingreso
            #--------------------
            #Contadores de promedios
            suma_temperatura += temperatura
            suma_presion += presion
            suma_dolor += dolor
            suma_frec_cardiaca += frecuencia_cardiaca
            suma_edades += edad_paciente
            #--------------------
            if sangre == "A+" or sangre == "a+":
                A_pos += 1
            if sangre == "A-" or sangre == "a-":
                A_neg += 1
            if sangre == "B+" or sangre == "b+":
                B_pos += 1
            if sangre == "B-" or sangre == "b-":
                B_neg += 1
            if sangre == "AB+" or sangre == "ab+":
                AB_pos += 1
            if sangre == "AB-" or sangre == "ab-":
                AB_neg += 1
            if sangre == "O+" or sangre == "o+":
                O_pos += 1
            if sangre == "O-" or sangre == "o-":
                O_neg += 1
            #--------------------
            #REGLAS

            print(Back.CYAN +"""
    ====================================
    ✙---------Recomendaciones---------✙ 
    ====================================
            """+ Style.RESET_ALL)

            if estado_critico and dolor_alto:
                print(Back.LIGHTRED_EX +"⚠ -Atención urgente."+ Style.RESET_ALL)

            if posible_infeccion and resp_agitada:
                print(Fore.GREEN +"⚠ -Posible afección respiratoria."+ Style.RESET_ALL)

            if dolor <= 3 and not fiebre and presion < 140:
                print(Fore.YELLOW +"△ -Condiciones leves control ambulatorio."+ Style.RESET_ALL)

            if 36 <= temperatura <= 37.5:
                print(Fore.YELLOW +"✔ -Temperatura normal"+ Style.RESET_ALL)

            if edad_paciente > 65 and fiebre and presion_alta:
                print(Back.RED +"⚠ -Posible problema "+ Style.RESET_ALL)

            if vomitos in ["s", "si", "sí"] and dolor <= 5:
                print(Fore.YELLOW +"△ -Posible problema digestivo" + Style.RESET_ALL)

            if resp_dolorosa and taquicardia:
                print(Fore.YELLOW +"⚠ -Evaluar oxigenación"+ Style.RESET_ALL)

            if posible_infeccion and dolor_alto:
                print(Fore.YELLOW +"⚠ -Posible afeccion respiratoria"+ Style.RESET_ALL)

            if riesgo_cardiovascular:
                print(Fore.YELLOW +"⚠ -Control cardiovascular"+ Style.RESET_ALL)

            if dolor_extremo and (fiebre or taquicardia):
                print(Back.RED + "⚠ -Dolor crítico acompañado de signos vitales alterados.\nSe recomienda atención médica urgente."+ Style.RESET_ALL)

            if estado_critico and riesgo_edad:
                print(Back.RED + "⚠ -Fiebre alta con taquicardia en paciente mayor.\n Se recomienda evaluación médica urgente."+ Style.RESET_ALL)

            if edad_paciente <= 12 and fiebre:
                print(Fore.YELLOW + "⚠ -Paciente pediátrico con fiebre"+ Style.RESET_ALL)

            if ejercicio in ["s","si","sí"]:
                while True:
                    try:
                        cuantas_veces = int(input(Fore.YELLOW + "|-¿Cuántas veces a la semana haces ejercicio? 1/5: " + Style.RESET_ALL))
                        if cuantas_veces < 1 or cuantas_veces > 5:
                            print(f"{Back.RED} |⚠ -Ingrese un valor numérico válido {Style.RESET_ALL}")
                            continue
                        break  

                    except ValueError:
                        print(f"{Back.RED} |⚠ -Ingrese un valor numérico válido {Style.RESET_ALL}")

                clima_agua = input(Fore.YELLOW +"|-¿En que clima se encuentra,cuando entrena? frio/templado/calor: "+ Style.RESET_ALL)
                if clima_agua == "frio":
                    clima_agua = 0
                elif clima_agua == "templado":
                    clima_agua = 250
                else:
                    clima_agua = 1000

                if cuantas_veces < 3:
                    agua_act_fisica = 400
                else:
                    agua_act_fisica = 800
                if not 1 <= cuantas_veces <= 7:
                    print("Valor inválido")
                else:    
                    if  cuantas_veces <= 2:
                        print(Fore.GREEN + "✔ -Podria incrementar a tres veces por semana para lograr una buena forma fisica"+ Style.RESET_ALL)
                    elif cuantas_veces <=4:
                        print(Fore.GREEN + "✔ -Esta en buena forma física"+ Style.RESET_ALL)
                    else:
                        print(Fore.LIGHTGREEN_EX +"✔ -El nivel de actividad fisica es muy bueno" + Style.RESET_ALL)

            if ejercicio in ["n","no","nó"]:
                agua_act_fisica = 0
                clima_agua = 0
                print(Fore.YELLOW +" ✘ -Deberia practicar 3 veces por semana en lo posible"+ Style.RESET_ALL)

            if edad_paciente < 18:
                agua_por_edad = 200
            elif edad_paciente < 59:
                agua_por_edad = 100
            else:
                agua_por_edad = 300

            agua_total_mililitros = agua_por_peso + agua_por_edad + clima_agua + agua_act_fisica

            agua_paciente = (agua_total_mililitros/1000)

            print(f"┌{'─' * ancho}┐")
            print(f"│ {Fore.RED}{'✙ MEDICPY':<35}{Style.RESET_ALL}│")
            print(f"├{'─' * ancho}┤")

            print(f"│ {Fore.GREEN}{'Paciente':<12} →  {nombre_paciente:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Edad':<12} →  {edad_paciente:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Genero':<12} →  {genero:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Sangre':<12} →  {sangre:<19}{Style.RESET_ALL}│")

            print(f"├{'─' * ancho}┤")

            print(f"│ {Fore.GREEN}{'Medicación':<12} →  {medicamentos:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Respiración':<12} →  {respiracion_str:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Presión':<12} →  {presion:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Temperatura':<12} →  {temperatura:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Dolor':<12} →  {dolor:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Frecuencia':<12} →  {frecuencia_cardiaca:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Ejercicio':<12} →  {ejercicio:<19}{Style.RESET_ALL}│")
            print(f"│ {Fore.GREEN}{'Agua':<12} →  {agua_total_mililitros:<19}{Style.RESET_ALL}│")

            print(f"└{'─' * ancho}┘")

            pacientes += 1
            
            if dolor_alto and fiebre and riesgo_edad:
                casos_criticos += 1
            
            if dolor_alto and fiebre and edad_paciente < 12:
                casos_criticos_pediatricos += 1
                
            continuar = input(Fore.GREEN + f"|>Desea realizar otro archivo? (s/n): "+ Style.RESET_ALL)

            if continuar != "s":
                print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                break

    elif operacion == 2:
        
        print("""
    ====================================
    |          -OPERACIONES-           |
    |**********************************|
    |           [Graficos]             |
    |-[1.Cantidad de generos]          |
    |-[2.Tipos de sangre]              |
    |**********************************|
    |-3.Estadisticas Generales         |
    ====================================
        """)
        while True:
            try:
                estadisticas = int(input(Fore.GREEN + f"Que gráfico quiere ver [1,2,3]: "+ Style.RESET_ALL))
                break
            
            except ValueError:
                print(f"{Back.RED} |⚠ -Ingrese un valor numérico válido {Style.RESET_ALL}")

        
        if estadisticas == 1 and pacientes == 0:
            print(f"{Back.RED} |⚠ -No hay datos para graficar... {Style.RESET_ALL}")   


        elif estadisticas == 1:
            #Generos
            total = masculinos + femeninos
            
            if total == 0:
                print(f"{Back.RED} |⚠ -No hay datos para graficar... {Style.RESET_ALL}")   
            
            else:
                porcentaje_m = (masculinos / total) * 100
                porcentaje_f = (femeninos / total) * 100 
                
                largo_barra = 30
                
                #masculinos
                llenos_m = int((porcentaje_m / 100) * largo_barra)
                vacios_m = largo_barra - llenos_m
                barra_m = "█" * llenos_m + "░" * vacios_m
                
                #femeninos
                llenos_f = int((porcentaje_f / 100) * largo_barra)
                vacios_f = largo_barra - llenos_f
                barra_f = "█" * llenos_f + "░" * vacios_f
                
                print("""
    ====================================
    |            -Generos-             |
    ====================================
                """)

                print(f"Maculinos: {masculinos} {porcentaje_m}%")
                print(Fore.BLUE + f"M|{barra_m}|\n" + Style.RESET_ALL)

                print(f"Femeninos: {femeninos} {porcentaje_f}%")
                print(Fore.MAGENTA + f"F|{barra_f}|" + Style.RESET_ALL)
                
                volver = input("volver? (s/n): ")
                if volver != "s":
                    print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                    bandera = False


        elif estadisticas == 2:
                #Sangres
                total = A_pos + A_neg + B_pos + B_neg + AB_pos + AB_neg + O_pos + O_neg

                if total == 0:
                    print(f"{Back.RED} |⚠ -No hay datos para graficar... {Style.RESET_ALL}")   
                else:    
                    print("""
    ====================================
    |            -Sangres-             |
    ====================================
                """)
                    if A_pos > 0:
                        porcentaje_A_pos = (A_pos / total) * 100
                        largo_barra = 30
                        lleno = int((porcentaje_A_pos / 100) * largo_barra)
                        vacio = largo_barra - lleno
                        barra = "█" * lleno + "░" * vacio
                        print(f"|A+|{porcentaje_A_pos:.1f}%| |{barra}|")

                    if A_neg > 0:
                        porcentaje_A_neg = (A_neg / total) * 100
                        largo_barra = 30
                        lleno = int((porcentaje_A_neg / 100) * largo_barra)
                        vacio = largo_barra - lleno
                        barra = "█" * lleno + "░" * vacio
                        print(f"|A-|{porcentaje_A_neg:.1f}%| |{barra}|")

                    if B_pos > 0:
                        porcentaje_B_pos = (B_pos / total) * 100
                        largo_barra = 30
                        lleno = int((porcentaje_B_pos / 100) * largo_barra)
                        vacio = largo_barra - lleno
                        barra = "█" * lleno + "░" * vacio
                        print(f"|B+|{porcentaje_B_pos:.1f}%| |{barra}|")

                    if B_neg > 0:
                        porcentaje_B_neg = (B_neg / total) * 100
                        largo_barra = 30
                        lleno = int((porcentaje_B_neg / 100) * largo_barra)
                        vacio = largo_barra - lleno
                        barra = "█" * lleno + "░" * vacio
                        print(f"|B-|{porcentaje_B_neg:.1f}%| |{barra}|")

                    if AB_pos > 0:
                        porcentaje_AB_pos = (AB_pos / total) * 100
                        largo_barra = 30
                        lleno = int((porcentaje_AB_pos / 100) * largo_barra)
                        vacio = largo_barra - lleno
                        barra = "█" * lleno + "░" * vacio
                        print(f"|AB+|{porcentaje_AB_pos:.1f}%| |{barra}|")

                    if AB_neg > 0:
                        porcentaje_AB_neg = (AB_neg / total) * 100
                        largo_barra = 30
                        lleno = int((porcentaje_AB_neg / 100) * largo_barra)
                        vacio = largo_barra - lleno
                        barra = "█" * lleno + "░" * vacio
                        print(f"|AB-|{porcentaje_AB_neg:.1f}%| |{barra}|")

                    if O_pos > 0:
                        porcentaje_O_pos = (O_pos / total) * 100
                        largo_barra = 30
                        lleno = int((porcentaje_O_pos / 100) * largo_barra)
                        vacio = largo_barra - lleno
                        barra = "█" * lleno + "░" * vacio
                        print(f"|O+|{porcentaje_O_pos:.1f}%| |{barra}|")

                    if O_neg > 0:
                        porcentaje_O_neg = (O_neg / total) * 100
                        largo_barra = 30
                        lleno = int((porcentaje_O_neg / 100) * largo_barra)
                        vacio = largo_barra - lleno
                        barra = "█" * lleno + "░" * vacio
                        print(f"|O-|{porcentaje_O_neg:.1f}%| |{barra}|")

                volver = input(Fore.YELLOW + f"|>volver? (s/n): "+ Style.RESET_ALL)
                if volver != "s":
                    print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                    bandera = False

        elif estadisticas == 3:
            print("""
    ====================================
    |          -ESTADISTICAS-          |
    |**********************************|
    |-1.Casos Criticos                 |
    |-2.Casos Leves                    |
    |-3.Promedios en guardia           |
    |-4.                               |
    |-5.                               |
    ====================================
            """)
            casos = int(input(Fore.GREEN + f"|>Que estadisticas presisas ver: "+ Style.RESET_ALL))
            
            if casos == 1:
                print("""
    ====================================
    |              -Casos-             |
    |**********************************|
    |1.Mayor temperatura               |
    |2.Mayor presion                   |
    |3.Mayor Dolor                     |
    |4.Mayor frecuencia cardíaca       |
    ====================================
                """)
                caso_critico = input(Fore.GREEN + f"|>Que caso critico desea ver: "+ Style.RESET_ALL)
                if caso_critico == "1":
                                
                    print(f"┌{'─' * ancho}┐")
                    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Mayor temperatura registrada':<34}│")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Ingreso':<9} →  {temp_max_ingreso:<21}│")
                    print(f"│  {'Nombre':<9} →  {temp_max_nombre:<21}│")
                    print(f"│  {'Edad':<9} →  {str(temp_max_edad) + ' años':<21}│")
                    print(f"│  {'Genero':<9} →  {temp_max_genero:<21}│")
                    print(f"│  {'Temp':<9} →  {str(max_temperatura) + ' °C  ⚠':<21}│")
                    print(f"└{'─' * ancho}┘")
                    
                    volver = input(Fore.YELLOW + f"|>volver? (s/n): "+ Style.RESET_ALL)
                    if volver != "s":
                        print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                        bandera = False
                        
                elif caso_critico == "2":
                
                    print(f"┌{'─' * ancho}┐")
                    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Mayor Presion registrada':<34}│")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Ingreso':<9} →  {pres_max_ingreso:<21}│")
                    print(f"│  {'Nombre':<9} →  {pres_max_nombre:<21}│")
                    print(f"│  {'Edad':<9} →  {str(pres_max_edad) + ' años':<21}│")
                    print(f"│  {'Genero':<9} →  {pres_max_genero:<21}│")
                    print(f"│  {'Presion':<9} →  {str(max_presion):<21}│")
                    print(f"└{'─' * ancho}┘")
                    
                    volver = input(Fore.YELLOW + f"|>volver? (s/n): "+ Style.RESET_ALL)
                    if volver != "s":
                        print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                        bandera = False
                    
                elif caso_critico == "3":
                
                    print(f"┌{'─' * ancho}┐")
                    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")                    
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Mayor Dolor registrada':<34}│")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Ingreso':<9} →  {dolor_max_ingreso:<21}│")
                    print(f"│  {'Nombre':<9} →  {dolor_max_nombre:<21}│")
                    print(f"│  {'Edad':<9} →  {str(dolor_max_edad) + ' años':<21}│")
                    print(f"│  {'Genero':<9} →  {dolor_max_genero:<21}│")
                    print(f"│  {'Dolor':<9} →  {str(max_dolor):<21}│")
                    print(f"└{'─' * ancho}┘")

                    volver = input(Fore.YELLOW + f"|>volver? (s/n): "+ Style.RESET_ALL)
                    if volver != "s":
                        print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                        bandera = False
                        
                elif caso_critico == "4":
                
                    print(f"┌{'─' * ancho}┐")
                    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Mayor Frecuencia cardiaca':<34}│")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Ingreso':<9} →  {frec_cardiaca_max_ingreso:<21}│")
                    print(f"│  {'Nombre':<9} →  {frec_cardiaca_max_nombre:<21}│")
                    print(f"│  {'Edad':<9} →  {str(frec_cardiaca_max_edad) + ' años':<21}│")
                    print(f"│  {'Genero':<9} →  {frec_cardiaca_max_genero:<21}│")
                    print(f"│  {'Frecuencia':<9} →  {str(max_frec_cardiaca):<21}│")
                    print(f"└{'─' * ancho}┘")
                
                volver = input(Fore.YELLOW + f"|>volver? (s/n): "+ Style.RESET_ALL)
                if volver != "s":
                    print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                    bandera = False
                        
            if casos == 2:
                print("""
    ====================================
    |              -Casos-             |
    |**********************************|
    |1.Menor temperatura               |
    |2.Menor presion                   |
    |3.Menor dolor                     |
    |4.Menor Frecuencia cardiaca       |
    ====================================
                """)
                caso_leve = input(Fore.GREEN + f"|>Que caso desea ver: "+ Style.RESET_ALL)
                if caso_leve == "1":
                    print(f"┌{'─' * ancho}┐")
                    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Menor Temperatura':<34}│")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Ingreso':<9} →  {temp_min_ingreso:<21}│")
                    print(f"│  {'Nombre':<9} →  {temp_min_nombre:<21}│")
                    print(f"│  {'Edad':<9} →  {str(temp_min_edad) + ' años':<21}│")
                    print(f"│  {'Genero':<9} →  {temp_min_genero:<21}│")
                    print(f"│  {'Temp':<9} →  {str(min_temperatura) + ' °C ':<21}│")
                    print(f"└{'─' * ancho}┘")

                    volver = input(Fore.YELLOW + f"|>volver? (s/n): "+ Style.RESET_ALL)
                    if volver != "s":
                        print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                        bandera = False
                        
                elif caso_leve == "2":

                    print(f"┌{'─' * ancho}┐")
                    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")                        
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Menor Presion':<34}│")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Ingreso':<9} →  {pres_min_ingreso:<21}│")
                    print(f"│  {'Nombre':<9} →  {pres_min_nombre:<21}│")
                    print(f"│  {'Edad':<9} →  {str(pres_min_edad) + ' años':<21}│")
                    print(f"│  {'Genero':<9} →  {pres_min_genero:<21}│")
                    print(f"│  {'Presion':<9} →  {str(min_presion):<21}│")
                    print(f"└{'─' * ancho}┘")
                    
                    volver = input(Fore.YELLOW + f"|>volver? (s/n): "+ Style.RESET_ALL)
                    if volver != "s":
                        print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                        bandera = False
                        
                elif caso_leve == "3":

                    print(f"┌{'─' * ancho}┐")
                    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")                    
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Menor Dolor':<34}│")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Ingreso':<9} →  {dolor_min_ingreso:<21}│")
                    print(f"│  {'Nombre':<9} →  {dolor_min_nombre:<21}│")
                    print(f"│  {'Edad':<9} →  {str(dolor_min_edad) + ' años':<21}│")
                    print(f"│  {'Genero':<9} →  {dolor_min_genero:<21}│")
                    print(f"│  {'Dolor':<9} →  {str(min_dolor):<21}│")
                    print(f"└{'─' * ancho}┘")

                    volver = input(Fore.YELLOW + f"|>volver? (s/n): "+ Style.RESET_ALL)
                    if volver != "s":
                        print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                        bandera = False
                
                elif caso_leve == "4":

                    print(f"┌{'─' * ancho}┐")
                    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")                   
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Menor Frecuencia cardiaca':<34}│")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Ingreso':<9} →  {frec_min_ingreso:<21}│")
                    print(f"│  {'Nombre':<9} →  {frec_min_nombre:<21}│")
                    print(f"│  {'Edad':<9} →  {str(frec_min_edad) + ' años':<21}│")
                    print(f"│  {'Genero':<9} →  {frec_min_genero:<21}│")
                    print(f"│  {'Frecuencia':<9} →  {str(min_frec_cardiaca):<21}│")
                    print(f"└{'─' * ancho}┘")
                    
                    volver = input(Fore.YELLOW + f"|>volver? (s/n): "+ Style.RESET_ALL)
                    if volver != "s":
                        print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
                        bandera = False
                        
            elif casos == 3:
                if pacientes > 0:
                    promedio_temperatura = suma_temperatura / pacientes
                    promedio_dolor = suma_dolor / pacientes
                    promedio_presion = suma_presion / pacientes
                    promedio_frec_cardiaca = suma_frec_cardiaca / pacientes
                    promedio_edades = suma_edades / pacientes

                    print(f"┌{'─' * ancho}┐")
                    print( f"│ {Fore.RED} {'✙ MEDICPY':<{ancho - 3}} {Style.RESET_ALL}│ ")                    
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {"Promedios Generales":<34}│")
                    print(f"├{'─' * ancho}┤")
                    print(f"│  {'Temperatura':<9} →  {promedio_temperatura:<21.2f}│")
                    print(f"│  {'Presion':<9} →  {promedio_presion:<21.2f}│")
                    print(f"│  {'Edades':<9} →  {f'{promedio_edades:.0f} años':<21}│")
                    print(f"│  {'Frecuencia':<9} →  {promedio_frec_cardiaca:<21.2f}│")
                    print(f"│  {'Dolor':<9} →  {promedio_dolor:<21.2f}│")
                    print(f"└{'─' * ancho}┘")
                else:
                    print(f"{Back.RED} |⚠ -No hay pacientes ingresados. {Style.RESET_ALL}")   
        else:
            print(f"{Back.RED} |⚠ -Ingrese un valor valido. {Style.RESET_ALL}")   
            operacion = int(input(Fore.GREEN + f"|>Que operacion desea realizar: "+ Style.RESET_ALL))
        
    continuar_menu = input(Fore.GREEN + f"|>Desea realizar alguna otra operacion? (s/n): "+ Style.RESET_ALL)
    if continuar_menu != "s":
        print(Fore.YELLOW + f"|>Saliendo..."+ Style.RESET_ALL)
        bandera = False
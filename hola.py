from colorama import *

ancho = 36

max_frec_cardiaca = 123
frec_cardiaca_max_edad = 34
frec_cardiaca_max_nombre = "Fabrizo"
frec_cardiaca_max_genero = "Zepesky"
frec_cardiaca_max_ingreso = "123"

# print(f"┌{'─' * ancho}┐")
# print(f"│  {'✙ MEDICPY':<{ancho - 2}}│ ")
# print(f"│  {'Mayor Frecuencia cardiaca':<34}│")
# print(f"├{'─' * ancho}┤")
# print(f"│  {'Ingreso':<9} →  {frec_cardiaca_max_ingreso:<21}│")
# print(f"│  {'Nombre':<9} →  {frec_cardiaca_max_nombre:<21}│")
# print(f"│  {'Edad':<9} →  {str(frec_cardiaca_max_edad) + ' años':<21}│")
# print(f"├{'─' * ancho}┤")
# print(f"│  {'Temp':<9} →  {str(max_frec_cardiaca) + ' °C  ⚠':<21}│")
# print(f"└{'─' * ancho}┘")

edad_paciente = 0 
genero = ""
sangre = ""
ancho = 35
respiracion = 0
presion = 0 
temperatura = 0 
dolor = 10
frecuencia_cardiaca = 0 
ejercicio = ""
agua_total_mililitros = 0 
nombre_paciente = ""
medicamentos = ""
    
print(f"┌{'─' * ancho}┐")

print(f"│ {Fore.RED}{'✙ MEDICPY':<35}{Style.RESET_ALL}│")

print(f"├{'─' * ancho}┤")

print(f"│ {Fore.GREEN}{'Paciente':<12} →  {nombre_paciente:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Edad':<12} →  {edad_paciente:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Genero':<12} →  {genero:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Sangre':<12} →  {sangre:<19}{Style.RESET_ALL}│")

print(f"├{'─' * ancho}┤")

print(f"│ {Fore.GREEN}{'Medicación':<12} →  {medicamentos:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Respiración':<12} →  {respiracion:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Presión':<12} →  {presion:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Temperatura':<12} →  {temperatura:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Dolor':<12} →  {dolor:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Frecuencia':<12} →  {frecuencia_cardiaca:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Ejercicio':<12} →  {ejercicio:<19}{Style.RESET_ALL}│")

print(f"│ {Fore.GREEN}{'Agua':<12} →  {agua_total_mililitros:<19}{Style.RESET_ALL}│")

print(f"└{'─' * ancho}┘")
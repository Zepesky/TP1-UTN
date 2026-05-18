from colorama import *

masculinos = 10

femeninos = 30

total = masculinos + femeninos

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
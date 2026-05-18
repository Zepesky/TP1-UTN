
lado_chico = float(input("Lado chico (cm): "))
diagonal_chica = float(input("Diagonal chica (cm): "))
lado_grande = float(input("Lado grande (cm): "))

# diagonal grande
diagonal_grande = 2 * (lado_grande**2 - (diagonal_chica/2)**2)

# varillas para 10 cometas (en metros)
varillas = (2*lado_chico + 2*lado_grande + diagonal_grande + diagonal_chica) * 10 / 100

# papel para 10 cometas (en m2)
papel = ((diagonal_grande * diagonal_chica)/2) * 1.10 * 10 / 10000

print("Varillas necesarias:", round(varillas,2), "m")
print("Papel necesario:", round(papel,2), "m2")
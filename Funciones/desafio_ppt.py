# Desafío: Piedra, Papel o Tijera
#
# Reglas:
#   - Piedra aplasta Tijera  → Gana Piedra
#   - Tijera corta Papel     → Gana Tijera
#   - Papel envuelve Piedra  → Gana Papel
#   - Mismo elemento         → Empate
#
# La partida se juega al mejor de 3 rondas.
# Si un jugador logra dos aciertos SEGUIDOS, la partida finaliza automáticamente.
# En caso de empate en las 3 rondas, el juego continúa hasta que haya un ganador.
#
# Elecciones: 1 = Piedra | 2 = Papel | 3 = Tijera
#
# Usar: import random  →  random.randint(1, 3)  para la elección de la máquina.
from Input import *

import random

# ─────────────────────────────────────────────
# Función 1
# verificar_ganador_ronda(jugador, maquina) -> str
#   Retorna: "Jugador" | "Máquina" | "Empate"
# ─────────────────────────────────────────────
def verificar_ganador_ronda(jugador, maquina):
    
    if jugador == 1 and maquina == 3:
        return "Jugador"
    elif jugador == 3 and maquina == 2:
        return "Jugador"
    elif jugador == 2 and maquina == 1:
        return "Jugador"
    else:
        if jugador == maquina:
            return "Empate"
        return "Maquina"


# ─────────────────────────────────────────────
# Función 2
# verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) -> bool
#   Retorna True si la partida sigue en curso, False si ya finalizó.
#   Finaliza si alguien ganó dos veces seguidas o se jugaron todas las rondas.
# ─────────────────────────────────────────────
def verificar_estado_partida(ronda_actual, ultimo_ganador, ganador_ronda):
    
    if ganador_ronda == ultimo_ganador and ganador_ronda != "Empate":
        return False
    elif ronda_actual == 3:
        return False
    else:
        return True
    
# ─────────────────────────────────────────────
# Función 3
# verificar_ganador_partida(aciertos_jugador, aciertos_maquina) -> str
#   Retorna: "Jugador" | "Máquina"
# ─────────────────────────────────────────────
def verificar_ganador_partida(aciertos_jugador, aciertos_maquina):
    
    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    else:
        return "Maquina"
        


# ─────────────────────────────────────────────
# Función 4
# mostrar_elemento(eleccion) -> str
#   Convierte la elección numérica en texto legible.
#   1 -> "Piedra" | 2 -> "Papel" | 3 -> "Tijera"
# ─────────────────────────────────────────────
def mostrar_elemento(eleccion):
    
    if eleccion == 1:
        elemento = "Piedra"
    elif eleccion == 2:
        elemento = "Papel"
    elif eleccion == 3:
        elemento = "Tijera"
    
    return elemento

# ─────────────────────────────────────────────
# Función 5
# jugar_piedra_papel_tijera() -> str
#   Gestiona toda la lógica del juego usando las funciones anteriores.
#   Retorna: "Jugador" o "Máquina" según quién ganó la partida.
#
#   Flujo:
#     - El jugador elige 1, 2 o 3 (validar entrada).
#     - La máquina elige aleatoriamente con random.randint(1, 3).
#     - Se determina el ganador de la ronda.
#     - Se verifica si la partida continúa o finalizó.
#     - Al terminar, mostrar quién ganó la partida.
# ─────────────────────────────────────────────
def jugar_piedra_papel_tijera():
    ancho = 30
    ronda = 0
    ultimo_ganador = ""
    aciertos_jugador = 0
    aciertos_maquina = 0
    
    while True:
        
        print(f"┌{'─' * ancho}┐")
        print(f"│  {'Piedra Papel o Tijera':<{ancho - 2}}│ ")
        print(f"├{'─' * ancho}┤")
        print(f"│  {'1':<9} →  {"Piedra":<21}│")
        print(f"│  {'2':<9} →  {"Papel":<21}│")
        print(f"│  {'3':<9} →  {"Tijera":<21}│")
        print(f"└{'─' * ancho}┘")
        
        jugador = int(input("Elegi [1,2,3]"))
        maquina = random.randint(1, 3)
        
        ganador_ronda = verificar_ganador_ronda(jugador, maquina)
        if ganador_ronda == "Jugador":
            aciertos_jugador += 1
            ultimo_ganador = ganador_ronda 
        elif ganador_ronda == "Maquina":
            aciertos_maquina += 1
            ultimo_ganador = ganador_ronda
        else:
            ultimo_ganador = ""
            
        ronda += 1
        
        if not verificar_estado_partida(ronda , ultimo_ganador , ganador_ronda):
            break
    return verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    



# Punto de entrada
if __name__ == "__main__":
    ganador = jugar_piedra_papel_tijera()
    print(f"Ganador de la partida: {ganador}")

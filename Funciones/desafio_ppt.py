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

import random

# ─────────────────────────────────────────────
# Función 1
# verificar_ganador_ronda(jugador, maquina) -> str
#   Retorna: "Jugador" | "Máquina" | "Empate"
# ─────────────────────────────────────────────
def verificar_ganador_ronda(jugador, maquina):
    pass


# ─────────────────────────────────────────────
# Función 2
# verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) -> bool
#   Retorna True si la partida sigue en curso, False si ya finalizó.
#   Finaliza si alguien ganó dos veces seguidas o se jugaron todas las rondas.
# ─────────────────────────────────────────────
def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
    pass


# ─────────────────────────────────────────────
# Función 3
# verificar_ganador_partida(aciertos_jugador, aciertos_maquina) -> str
#   Retorna: "Jugador" | "Máquina"
# ─────────────────────────────────────────────
def verificar_ganador_partida(aciertos_jugador, aciertos_maquina):
    pass


# ─────────────────────────────────────────────
# Función 4
# mostrar_elemento(eleccion) -> str
#   Convierte la elección numérica en texto legible.
#   1 -> "Piedra" | 2 -> "Papel" | 3 -> "Tijera"
# ─────────────────────────────────────────────
def mostrar_elemento(eleccion):
    pass


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
    pass


# Punto de entrada
if __name__ == "__main__":
    ganador = jugar_piedra_papel_tijera()
    print(f"Ganador de la partida: {ganador}")

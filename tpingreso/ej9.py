#cree un programa que calcule el promedio de un alumno, ingresando su
#nombre apellido, 3 notas, que muestre al final las leyendas pertinentes

nombre = input("Nombre del alumno: ")

apellido = input("Apellido del alumno: ")

estudiante = nombre + apellido

programacion = int(input("Nota de Programacion: "))

matematicas = int(input("Nota de Matematica: "))

lectura = int(input("Nota de Lectura.c: "))

promedio = (programacion + matematicas + lectura) / 3 

print(f"""
============================
          Materias
============================
|Alumno: {estudiante}|
============================
1. Programación: {programacion}
2. Matemáticas: {matematicas}
3. Lectura C: {lectura}
------------------------
[PROMEDIO: {promedio}]
------------------------
""")
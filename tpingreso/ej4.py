#Cree un programa que pida el nombre, número de comisión, asignatura,
#docente y si el usuario estuvo presente, luego que muestre los datos por
#consola con las leyendas pertinentes

nombre = input("Nombre: ")

comision = input("N° de comision: ")

asignatura = input("Asignatira: ")

docente = input("Docente: ")

presentismo = input("Presente o Ausennte (P/A): ")

print("Tu usuario se llama", nombre,
    "\npertenece a la comicion n° y asignatura", comision , asignatura, 
    "\ncon el docente a cargo", docente, 
    "\nSe encuentra:", presentismo)  
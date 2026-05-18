
basico = 5000
estandar = 8000
premium = 12000
precio_dispositivo = 500
iva_porcentaje = 0.21

print("""
|==============|
|    Planes    |
|--------------|
|1.Basico      |
|2.Estandar    |
|3.Premium     |
|--------------|
|==============|
""")

plan = int(input("Que plan desea seleccionar: "))

cantidad_dis = float(input("Cuantos dispositivos vas a tener: "))

meses = int(input("Meses de subcripcion:"))

usuario = str(input("Es estudiante? (s/n): ")).lower()

if plan == 1:
    precio_base = basico
elif plan == 2:
    precio_base = estandar
elif plan == 3:
    precio_base = premium
else:
    print("Selecciones una opcion valida")
    
    
recargo_disp = cantidad_dis * 500

subtotal = precio_base + recargo_disp

#plan basico
if usuario == "s" and plan == 1:
    if cantidad_dis >= 6:
        descuento = subtotal * 0.10
    elif cantidad_dis >= 3:
        descuento = subtotal * 0.07
    elif cantidad_dis in (1,2):
        descuento = subtotal * 0.03

#plan estandar
elif plan == 2:
    if usuario == "s":
        descuento = subtotal * 0.15
    elif usuario == "n":
        if cantidad_dis == 1:
            descuento = subtotal * 0.15

#plan premium
elif plan == 3:
    if usuario == "s":
        if 5 <= cantidad_dis <= 9:
            descuento = subtotal * 0.20
    else:
        descuento = subtotal * 0.05
        

antiguedad = 0 

if meses >= 24:
    descuento += subtotal * 0.10

total = subtotal - descuento
iva = total * iva_porcentaje
total_fin = total + iva 

print("=" * 30) 
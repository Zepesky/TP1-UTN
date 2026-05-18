cargo_fijo = 7000
costo_metro = 200

consumidos = int(input(("Cantidad de metros consumidos: ")))

print("""
==================
1.Residencial
2.Comercial
3.Industrial
===================
""")

tipo_cliente = input(("tipo de cliente: "))

total_base = cargo_fijo + (consumidos * costo_metro)
total = total_base

print(f"Tu total sin descuentos ni impuestos es", total_base)

#Bonificaciones y Recargos

#Cliente Residencial
if tipo_cliente == "1":
    if consumidos < 30:
        descuento = total * 0.10
        total = total - descuento
        print(f"Se te aplico un descuento del 10%")
    elif consumidos > 80:
        recargo = total * 0.15
        total = total + recargo
        print(f"Se te aplico un recargo del 15%")

#Cliente Comercial
elif tipo_cliente == "2":
    if consumidos > 300:
        descuento = total * 0.12
        total = total - descuento
        print(f"Se te aplico un descuento del 12%")
    elif consumidos > 150:
        descuento = total * 0.08
        total = total - descuento
        print(f"Se te aplico un descuento del 8%")
    elif consumidos < 50:
        descuento = total * 0.05
        total = total - descuento
        print(f"Se te aplico un descuento del 5%")

#Cliente Industrial
elif tipo_cliente == "3":
    if consumidos > 1000:
        descuento = total * 0.30
        total = total - descuento
        print(f"Se te aplico un descuento del 30%")
    elif consumidos > 500 :
        descuento = total * 0.20
        total = total - descuento
        print(f"Se te aplico un descuento del 20% ")
    elif consumidos < 200:
        recargo = total * 0.10
        total = total + recargo
        print(f"Se te aplico un recargo del 10%")
        
print(f"Su saldo sin inpuestos:", total)

if tipo_cliente == "1" and total_base < 35000:
    descuento = total * 0.05
    total -= descuento
    print(f"Tenes un descuento adicional del 5%")

iva = total * 0.21

total_final = total + iva

print(f"Su total a pagar con IVA(21%):", total_final)


def buscar_Intececcion(lista_a, lista_b):
    interseccion = []
    for i in range(len(lista_a)):
        for j in range(len(lista_b)):
            if lista_a[i] == lista_b[j] and lista_a[i] not in intercesccion:
                interseccion.append(lista_a[i])
                break
    
    return interseccion

lista_a  = [5,9,4,3,5]

lista_b = [2,4,6,3,7]

intercesccion = buscar_Intececcion(lista_a, lista_b)

print(intercesccion)

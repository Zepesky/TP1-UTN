lista = [4,6,3,7,1,65,2]

for i in range (0, len(lista)- 1, 1):
    for j in range(i + 1, len(lista), 1):
        if lista[i] < lista[j]:
            auxiliar = lista[j]
            lista[i] = lista[j]
            lista[j] = auxiliar
            

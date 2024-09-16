def ordenamiento_fusion(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        # Llamada recursiva a la función de ordenamiento en ambas mitades
        ordenamiento_fusion(izquierda)
        ordenamiento_fusion(derecha)

        i = j = k = 0

        # Mezcla de las dos mitades
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Verifica si queda algún elemento en la mitad izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Verifica si queda algún elemento en la mitad derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista
mi_lista = [11, 2, 32, 4]
lista_ordenada = ordenamiento_fusion(mi_lista)
print("Lista ordenada por MergeSort:", lista_ordenada)
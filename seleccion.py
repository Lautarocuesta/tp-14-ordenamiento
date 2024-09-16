def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista
lista = [21, 2, 34, 4]
lista_ordenada = ordenamiento_seleccion(lista)
print("Lista ordenada por Selección:", lista_ordenada)
def ordenamiento_rapido(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return ordenamiento_rapido(izquierda) + centro + ordenamiento_rapido(derecha)

mi_lista = [11, 32, 93, 4]
lista_ordenada = ordenamiento_rapido(mi_lista)
print("Lista ordenada por QuickSort:", lista_ordenada)
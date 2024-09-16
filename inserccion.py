def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i-1
        while j >= 0 and clave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = clave
    return lista
lista = [11, 52, 3, 4]
lista_ordenada = ordenamiento_insercion(lista)
print("Lista ordenada por Inserción:", lista_ordenada)
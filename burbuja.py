def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = [11, 22, 3, 4]
lista_ordenada = ordenamiento_burbuja(lista)
print("Lista ordenada:", lista_ordenada)

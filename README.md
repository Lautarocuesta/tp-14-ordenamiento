# tp-14-ordenamiento
Algoritmos de Ordenamiento
1. Ordenamiento Burbuja (Bubble Sort)
Ventajas:
-Fácil de implementar y comprender.
-Requiere poca memoria adicional ya que se realiza en el lugar (in-place).

Desventajas:
-Tiene una complejidad temporal de O(n²), lo que lo hace ineficiente para listas grandes.
-Comparativamente más lento que otros algoritmos para grandes conjuntos de datos.
-Se realizan muchas comparaciones y movimientos incluso si la lista está casi ordenada.

2. Ordenamiento por Selección (Selection Sort)
Ventajas:
-Fácil de implementar y comprender.
-Requiere pocas operaciones de intercambio en comparación con el Ordenamiento Burbuja.

Desventajas:
-Tiene una complejidad temporal de O(n²), lo que lo hace ineficiente para listas grandes.
-No es adaptativo; siempre realiza el mismo número de comparaciones independientemente de si la lista ya está ordenada.

3. Ordenamiento por Inserción (Insertion Sort)
Ventajas:
-Eficiente para listas pequeñas o casi ordenadas.
-Se realiza in-place y requiere poca memoria adicional.
-Es estable (mantiene el orden de los elementos iguales).

Desventajas:
-Tiene una complejidad temporal de O(n²) en el peor caso.
-No es adecuado para listas grandes, ya que el tiempo de ejecución aumenta rápidamente.

4. Ordenamiento Rápido (QuickSort)
Ventajas:
-Muy eficiente en la práctica para la mayoría de los conjuntos de datos.
-Tiene una complejidad temporal promedio de O(n log n).
-Se realiza en el lugar (in-place) y requiere poca memoria adicional.

Desventajas:
-En el peor de los casos (cuando la lista ya está ordenada o casi ordenada), tiene una complejidad de O(n²), aunque esto puede evitarse con buenas estrategias de pivote.
-No es estable.

5. Ordenamiento por Fusión (MergeSort)
Ventajas:
-Siempre tiene una complejidad temporal de O(n log n), independientemente del estado inicial de la lista.
-Es estable.
-Ideal para ordenar listas muy grandes o datos almacenados en dispositivos externos.

Desventajas:
-Requiere memoria adicional proporcional al tamaño de la lista, ya que no se realiza en el lugar.
-Aunque eficiente, es más lento que QuickSort en la práctica debido a la sobrecarga de mezclar las sublistas.
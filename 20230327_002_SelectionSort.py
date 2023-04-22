# -*- coding: utf-8 -*-
"""


@author: Omar
"""


def selectionSort(arr):
    n = len(arr)
    # Recorre todos los elementos del array
    for i in range(n):
        # Encuentra el elemento mínimo en la porción no ordenada del array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambia el elemento mínimo encontrado con el primer elemento de la porción no ordenada
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
selectionSort(arr)
print("Lista ordenada:")
for i in range(len(arr)):
    print("%d" % arr[i]),

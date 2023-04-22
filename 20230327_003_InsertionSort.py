# -*- coding: utf-8 -*-
"""


@author: Omar
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Elemento actual a ser insertado en su posición correcta
        j = i - 1
        # Desplazar los elementos mayores a la derecha para hacer espacio para el elemento actual
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insertar el elemento actual en su posición correcta
    return arr

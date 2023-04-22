# -*- coding: utf-8 -*-
"""


@author: Omar
"""





def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # Elegir el pivote como el elemento en la mitad de la lista
   
    left = [x for x in arr if x < pivot]  # Elementos menores que el pivote
    
    middle = [x for x in arr if x == pivot]  # Elementos iguales al pivote
   
    right = [x for x in arr if x > pivot]  # Elementos mayores que el pivote
   
    # Llamada recursiva para ordenar los subarreglos izquierdo y derecho
    
    return quick_sort(left) + middle + quick_sort(right)

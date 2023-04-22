# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 20:00:28 2023

@author: Omar
"""

def radix_sort(arr):
   
    # Encuentra el valor máximo en la lista
    max_value = max(arr)

   
 # Determina el número de dígitos en el valor máximo
    max_exponent = len(str(max_value))

   
 # Inicializa el cubo con 10 baldes de vacío
    buckets = [[] for _ in range(10)]

   
 # Ordena los números según el dígito correspondiente
    for exponent in range(max_exponent):
        for num in arr:
           
            # Determina el dígito correspondiente
            digit = (num // 10**exponent) % 10
           
            # Agrega el número al balde correspondiente
            buckets[digit].append(num)
       
        # Combina los números de los baldes en una lista
        arr = [num for bucket in buckets for num in bucket]
       
        # Vacía los baldes para el siguiente dígito
        buckets = [[] for _ in range(10)]

    return arr

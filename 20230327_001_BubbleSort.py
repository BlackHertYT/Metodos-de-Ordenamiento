# -*- coding: utf-8 -*-
"""


@author: Omar
"""


#se define la función bubbleSort(arr) que toma una lista de elementos arr como argumento. La función determina la longitud de la lista con n = len(arr)
def bubbleSort(arr):
    n = len(arr)
    
    #Dentro del bucle interno, se compara cada elemento de la lista con su siguiente elemento adyacente. Si el elemento actual es mayor que su siguiente elemento, se intercambian los dos elementos utilizando la asignación múltiple de Python 
    for i in range(n):
        # Últimos i elementos ya están ordenados
        
        for j in range(n - i - 1):
            # Compara los elementos adyacentes
           
            if arr[j] > arr[j + 1]:
                # Intercambia los elementos si están en el orden incorrecto
                # Una vez que se han ordenado todos los elementos de la lista, la función
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


#Lista desordenada
arr = [45,34,87,56,123,34,89,54,29]
bubbleSort(arr)
print("Lista ordenada:")
for i in range(len(arr)):
    print("%d" % arr[i]),

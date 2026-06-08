import numpy as np

# arregloNumeros = np.array( [2,34,5,7,8,434,23,87] ) #0
# arregloNumerosDos = np.array( [2,34,5,7,8,434,23,87,32,545,43,78,56,89,9] ) #1


# print(arregloNumeros)


# print ("numero mayor: ", np.max(arregloNumeros))        
# print ("numero menor: ", np.min(arregloNumeros))      

# totlatres = np.sum(arregloNumeros)
# print("El total es:", totlatres)

# print("El promedio es:", np.mean(arregloNumeros))


# # arregloNumeros = [2,34,5,7,8,434,23,87]
# # totlatres = sum(arregloNumeros)
# # cantidad = len(arregloNumeros)
# # print("El total es:", totlatres)

# # print(totlatres/cantidad)


# matriz = np.array([
#     [2,34,5],
#     [6,5,44] #fila1 #columna 1
# ])


# print(matriz)
# print(matriz[0][2])
# print(matriz[0, 2])



# print(arregloNumeros)
# print(arregloNumeros*2)



# # Generar por rango
# numerosRango = np.arange(5,80)

# print(numerosRango)

# # Generar por aleatorios
# numerosAleatorio = np.random.randint(5,80,10)

# print(numerosAleatorio)

arregloEdades = np.array( [2,34,5,7,8,43,55,90,102,23,87] )
print("Cantidad:", len(arregloEdades))
print("Mayor:", np.max(arregloEdades))
print("Menor:", np.min(arregloEdades))
print("Promedio:", np.mean(arregloEdades))
print("Suma:", np.sum(arregloEdades))
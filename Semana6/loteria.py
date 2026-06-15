import numpy as np

numeros_loteria = np.array([
    [5, 12, 22, 33, 42, 49],
    [3, 15, 22, 28, 33, 45],
    [7, 12, 19, 25, 33, 40],
    [5, 18, 22, 28, 37, 42],
    [9, 12, 22, 33, 42, 48],
    [5, 15, 20, 28, 33, 45],
    [6, 12, 22, 34, 40, 49],
    [5, 17, 21, 28, 33, 42],
    [8, 12, 22, 29, 33, 47],
    [5, 14, 22, 30, 33, 41]
])

def contar_frecuencias(numeros):
    frecuencias = {}
    for fila in numeros:
        for numero in fila:
            if numero in frecuencias:
                frecuencias[numero] += 1
            else: 
                frecuencias[numero] = 1
    return frecuencias

def numeros_mas_frecuentes(frecuencias, top_n=5):
    numeros_ordenados = sorted(frecuencias.items(), key=lambda x: x[1], reverse= True)
    return numeros_ordenados[:top_n]

def generar_numeros_sugeridos(numeros_frecuentes, total_numeros=6):
    sugeridos = [numero[0] for numero in numeros_frecuentes]
    while len(sugeridos) < total_numeros:
        numero_aleatorio = np.random.randint(1, 50)
        if numero_aleatorio not in sugeridos:
            sugeridos.append(numero_aleatorio)
    return sugeridos

# Contar frecuencias de los números 
frecuencias = contar_frecuencias(numeros_loteria)

# Identificar los números más frecuentes
top_numeros = numeros_mas_frecuentes(frecuencias, top_n=5)

# Generar números sugeridos para el próximo sorteo
numeros_sugeridos = generar_numeros_sugeridos(top_numeros, total_numeros=6)

# Mostrar los resultados
np.set_printoptions(legacy='1.25')
print("Frecuencias de numeros:", frecuencias)
print("Numeros mas frecuentes:", top_numeros)
print("Numeros sugeridos para jugar:", numeros_sugeridos)
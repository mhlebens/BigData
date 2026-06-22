import os

import matplotlib.pyplot as plt
import pandas as pd
 
prov = ["SJ","Punt", "Cart"]
cantidad = [2,5,6]
ventas = [100,300,65,879,950,233,540]
notas=[70,75,80,85,90,95,100]
#Grafico de Barras
# plt.bar(prov, cantidad)
# plt.title("Personas por provincia")
# plt.xlabel("provincia")
# plt.ylabel("cantidad")
 
# plt.show()
#Por histogrmas
# plt.hist(cantidad)
# plt.title("Distribucion de cantidad")
# plt.show()
 
#Grafico lineal
# plt.plot(ventas)
# plt.title("graficos")
# plt.show()
 
 
#Boxplot, eso es para detectar valores similares
# plt.boxplot(notas)
# plt.title("Boxplot")
# plt.show()
 
nombreArchivo = "Semana 6\Personas.csv"
directorio = os.getcwd()
ruta = os.path.join(directorio, nombreArchivo)
print(ruta)

# Cargar Archivo
archivo = pd.read_csv("../Personas.csv")

# Contamos las personas de las provincias
provincias = archivo["Provincia"].value_counts()

print(provincias)

# Generar la gráfica
provincias.plot(kind="bar")
plt.title("cantidad de personas por provincia")
plt.xlabel("Provincias")
plt.ylabel("Cantidad de personas")
plt.show()
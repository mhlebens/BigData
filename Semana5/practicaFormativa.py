import numpy as np

# Temperaturas que en un inicio están en °F
arregloFarenheit = np.array( [32, 45, 64, 72, 95, 100] )

# Conversión a °C
ConversionCelsius = (arregloFarenheit - 32)* 5/9

print("Temperaturas en °C: ", ConversionCelsius)

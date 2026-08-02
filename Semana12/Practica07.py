# -----------------------------------------------------
# PARTE 1 – VARIABLES, ASIGNACIÓN Y TIPOS DE DATOS
# -----------------------------------------------------

# -----------------------------------------------------
# EJERCICIO 1 - CREACIÓN DE VARIABLES
# -----------------------------------------------------

# Enunciado:
# Cree variables para almacenar el nombre, la edad, la estatura
# y el estado estudiantil de una persona. Utilice distintos tipos
# de datos y muestre sus valores en consola.

# Creación de variables
edad = 20
estatura = 1.65
nombre = "María"
estudianteActivo = True

# Visualización de los valores de las variables
print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("¿Es estudiante activo?:", estudianteActivo)


# -----------------------------------------------------
# EJERCICIO 2 - CONVERSIÓN DE DECIMAL A ENTERO
# -----------------------------------------------------

# Enunciado:
# Convierta la estatura definida anteriormente de decimal a entero.
# Muestre el valor antes y después de realizar la conversión.

# Nueva variable que almacena la estatura convertida a un número entero
estaturaEntera = int(estatura)

# Visualización
print("\nEstatura original:", estatura)
print("Estatura convertida a entero:", estaturaEntera)

# Explicación:
# Al convertir 1.65 a entero, se elimina la parte decimal.
# El resultado es 1 porque int() no redondea el valor.

# -----------------------------------------------------
# EJERCICIO 3 - CONVERSIÓN DE ENTERO A DECIMAL
# -----------------------------------------------------

# Enunciado:
# Convierta la edad definida anteriormente de número entero
# a número decimal. Muestre ambos valores en consola.

# Variable que almacena la edad convertida a un número decimal
edadDecimal = float(edad)

# Visualización
print("\nEdad original:", edad)
print("Edad convertida a decimal:", edadDecimal)

# Explicación:
# Al convertir el entero 20 a decimal, el resultado es 20.0.
# El valor numérico no cambia, solamente su representación.

# -----------------------------------------------------
# EJERCICIO 4 - CONVERSIÓN DE NÚMERO A TEXTO
# -----------------------------------------------------

# Enunciado:
# Convierta la edad definida anteriormente de número entero
# a texto. Muestre ambos valores en consola.

# Variable que almacena la edad convertida a texto
edadTexto = str(edad)

# Visualización
print("\nEdad original:", edad)
print("Edad convertida a texto:", edadTexto)

# Explicación:
# Al utilizar str(), el número 20 se convierte en el texto "20".
# Visualmente parecen iguales, pero el texto no puede utilizarse
# directamente en operaciones matemáticas.

# -----------------------------------------------------
# EJERCICIO 5 - CONVERSIÓN DE TEXTO A ENTERO
# -----------------------------------------------------

# Enunciado:
# Convierta la edad almacenada como texto nuevamente a un número
# entero. Muestre el valor antes y después de la conversión.

# Se convierte el texto "20" en un número entero
edadConvertida = int(edadTexto)

# Visualización
print("\nEdad almacenada como texto:", edadTexto)
print("Edad convertida a entero:", edadConvertida)

# Explicación:
# La conversión es posible porque el texto "20" representa
# un número entero válido. Después de convertirlo, el resultado
# puede utilizarse en operaciones matemáticas.

# -----------------------------------------------------
# EJERCICIO 6 - CONVERSIÓN DE VALOR LÓGICO A TEXTO
# -----------------------------------------------------

# Enunciado:
# Convierta el estado estudiantil definido anteriormente
# de un valor lógico a texto. Muestre ambos valores en consola.

# Se convierte el valor lógico True a texto
estadoTexto = str(estudianteActivo)

# Visualización
print("\nEstado original:", estudianteActivo)
print("Estado convertido a texto:", estadoTexto)

# Explicación:
# La función str() convierte el valor lógico True en el texto "True".
# Aunque ambos se muestran de forma similar, el valor convertido
# deja de funcionar como un dato lógico y pasa a ser una cadena de texto.


# -----------------------------------------------------
# EJERCICIO 7 - CONVERSIÓN DE DATOS PARA UN CÁLCULO
# -----------------------------------------------------

# Enunciado:
# Una tienda almacena el precio de un producto y la cantidad comprada
# como datos de texto. Convierta el precio a decimal y la cantidad a
# entero para calcular el total de la compra.

# Datos almacenados originalmente como texto
precioTexto = "2500.50"
cantidadTexto = "3"

# Conversión del precio a decimal y la cantidad a entero
precioDecimal = float(precioTexto)
cantidadEntera = int(cantidadTexto)

# Cálculo del total de la compra
totalCompra = precioDecimal * cantidadEntera

# Visualización de los resultados
print("\nPrecio convertido:", precioDecimal)
print("Cantidad convertida:", cantidadEntera)
print("Total de la compra:", totalCompra)

# Explicación:
# Los valores almacenados como texto no deben utilizarse directamente
# en cálculos matemáticos. Por eso, el precio se convierte con float()
# y la cantidad con int() antes de calcular el total.

# -----------------------------------------------------
# EJERCICIO 8 - ERROR DE CONVERSIÓN
# -----------------------------------------------------

# Enunciado:
# Intente convertir el nombre definido anteriormente en un número
# entero. Detecte el error producido y explique por qué ocurre.

try:
    # Se intenta convertir el texto "María" a un número entero
    nombreEntero = int(nombre)
    print("\nNombre convertido:", nombreEntero)

except ValueError:
    # Este mensaje se muestra cuando el texto no representa
    # un número entero válido
    print("\nError: el nombre", nombre, "no puede convertirse a entero.")

# Explicación:
# La conversión genera un ValueError porque el texto "María"
# contiene letras y no representa un número entero válido.
# Un texto como "20" sí podría convertirse utilizando int().

# -----------------------------------------------------
# PARTE 2 - OPERACIONES ARITMÉTICAS Y LÓGICAS
# -----------------------------------------------------


# -----------------------------------------------------
# EJERCICIO 1 - SUMA Y RESTA
# -----------------------------------------------------

# -----------------------------------------------------
# PARTE 2 - OPERACIONES ARITMÉTICAS Y LÓGICAS
# -----------------------------------------------------


# -----------------------------------------------------
# EJERCICIO 1 - SUMA Y RESTA
# -----------------------------------------------------

# Enunciado:
# Una persona tiene ₡15 000 y gasta ₡7500.
# Luego recibe ₡5500. Calcule el dinero obtenido
# mediante la suma y el saldo final mediante la resta.

dineroInicial = 15000
dineroGastado = 7500
dineroRecibido = 5500

# Procedimiento
saldoDespuesGasto = dineroInicial - dineroGastado
saldoFinal = saldoDespuesGasto + dineroRecibido

# Visualización
print("\nSaldo después del gasto:", saldoDespuesGasto)
print("Saldo final:", saldoFinal)

# Explicación:
# Después de gastar ₡7 500 quedan ₡7 500.
# Al recibir ₡5 500, el saldo final aumenta a ₡13 000.

# -----------------------------------------------------
# EJERCICIO 2 - MULTIPLICACIÓN Y DIVISIÓN
# -----------------------------------------------------

# Enunciado:
# Un grupo compra 6 cuadernos con un precio de ₡2 500 cada uno.
# Calcule el costo total de la compra y determine cuánto debe
# pagar cada persona si el costo se divide entre 3 personas.

cantidadCuadernos = 6
precioPorCuaderno = 2500
cantidadPersonas = 3

# Procedimiento
costoTotal = cantidadCuadernos * precioPorCuaderno
pagoPorPersona = costoTotal / cantidadPersonas

# Visualización
print("\nCosto total de la compra:", costoTotal)
print("Pago por persona:", pagoPorPersona)

# Explicación:
# Los 6 cuadernos cuestan en total ₡15 000.
# Al dividir el costo entre 3 personas, cada una debe pagar ₡5 000

# -----------------------------------------------------
# EJERCICIO 3 - POTENCIA
# -----------------------------------------------------

# Enunciado:
# Un terreno cuadrado tiene lados de 12 metros.
# Calcule su área elevando la medida de uno de sus lados
# a la potencia de 2.

ladoTerreno = 12

# Procedimiento
areaTerreno = ladoTerreno ** 2

# Visualización del resultado
print("\nÁrea del terreno:", areaTerreno, "metros cuadrados")

# Explicación:
# Elevar 12 a la potencia de 2 equivale a multiplicar 12 por 12.
# Por lo tanto, el terreno tiene un área de 144 metros cuadrados

# -----------------------------------------------------
# EJERCICIO 4 - MÓDULO
# -----------------------------------------------------

# Enunciado:
# Una persona tiene 61 confites y desea distribuirlos
# en grupos de 7. Calcule cuántos confites sobran después
# de formar todos los grupos posibles.

cantidadConfites = 61
confitesPorGrupo = 7

# Procedimiento
confitesSobrantes = cantidadConfites % confitesPorGrupo

# Visualización
print("\nConfites sobrantes:", confitesSobrantes)

# Explicación:
# Al dividir 61 entre 7 se forman 8 grupos completos,
# utilizando 56 confites. Por lo tanto, quedan 5 confites
# sin agrupar.

# -----------------------------------------------------
# EJERCICIO 5 - DIVISIÓN ENTERA
# -----------------------------------------------------

# Enunciado:
# Una persona tiene 61 confites y desea distribuirlos
# en grupos de 7. Calcule cuántos grupos completos puede
# formar utilizando la división entera.

cantidadConfites = 61
confitesPorGrupo = 7

# Procedimiento
gruposCompletos = cantidadConfites // confitesPorGrupo

# Visualización
print("\nGrupos completos formados:", gruposCompletos)

# Explicación:
# Al dividir 61 entre 7 se obtienen 8 grupos completos.
# La división entera ignora la parte decimal del resultado
# y no incluye los 5 confites sobrantes

# -----------------------------------------------------
# EJERCICIO 6 - COMPARACIÓN DE VALORES
# -----------------------------------------------------

# Enunciado:
# Solicite al usuario el precio de dos productos.
# Indique cuál precio es mayor y cuál es menor.
# Si ambos precios son iguales, muestre un mensaje indicándolo.

# Procedimiento
precioProducto1 = float(input("\nDigite el precio del primer producto: "))
precioProducto2 = float(input("Digite el precio del segundo producto: "))

if precioProducto1 > precioProducto2:
    print("\nEl precio mayor es:", precioProducto1)
    print("El precio menor es:", precioProducto2)

elif precioProducto2 > precioProducto1:
    print("\nEl precio mayor es:", precioProducto2)
    print("El precio menor es:", precioProducto1)

else:
    print("\nAmbos precios son iguales:", precioProducto1)

# Explicación:
# El programa compara ambos precios.
# Si el primero es mayor, muestra primero ese valor.
# Si el segundo es mayor, invierte el orden.
# Cuando ninguno es mayor que el otro, significa que son iguales

# -----------------------------------------------------
# EJERCICIO 7 - OPERADORES LÓGICOS
# -----------------------------------------------------

# Enunciado:
# Determine si una persona puede ingresar a un evento considerando
# que debe tener una entrada y que el evento no esté lleno.
# También determine si recibe descuento por ser estudiante
# o una persona adulta mayor.

tieneEntrada = True
eventoLleno = False
esEstudiante = True
esAdultoMayor = False

# Procedimientos
puedeIngresar = tieneEntrada and not eventoLleno
recibeDescuento = esEstudiante or esAdultoMayor

# Visualización
print("\n¿Puede ingresar al evento?:", puedeIngresar)
print("¿Recibe descuento?:", recibeDescuento)

# Explicación:
# La persona puede ingresar porque tiene entrada y el evento no está lleno.
# También recibe descuento porque es estudiante, aunque no sea adulta mayor

# -----------------------------------------------------
# EJERCICIO 8 - EXPRESIÓN LÓGICA COMPLEJA
# -----------------------------------------------------

# Enunciado:
# Un centro deportivo permite el ingreso cuando la persona es mayor
# de edad y tiene membresía, o cuando tiene al menos 15 años y está
# acompañada por un adulto. En cualquiera de los casos, la cuenta
# no debe encontrarse suspendida.

edadPersona = int(input("\nDigite la edad de la persona: "))

# Procedimiento
tieneMembresia = input("¿Tiene membresía? (sí/no): ").lower() == "sí"
estaAcompanada = input("¿Está acompañada por un adulto? (sí/no): ").lower() == "sí"
cuentaSuspendida = input("¿La cuenta está suspendida? (sí/no): ").lower() == "sí"

puedeIngresar = (
    (edadPersona >= 18 and tieneMembresia)
    or (edadPersona >= 15 and estaAcompanada)
) and not cuentaSuspendida

# Visualización
if puedeIngresar:
    print("\nLa persona puede ingresar al centro deportivo.")
else:
    print("\nLa persona no puede ingresar al centro deportivo.")

# Explicación:
# Primero se comprueba si la persona es mayor de edad y tiene membresía.
# Como alternativa, puede tener al menos 15 años y estar acompañada.
# Finalmente, la cuenta no debe estar suspendida en ninguno de los casos.
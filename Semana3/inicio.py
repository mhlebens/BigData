print("Saludos clase") # mostrar mensajes en consola

# "()" pasar parámetros

textNombre = "mafeh" #Tipo de dato: texto
edad = 20 #Tipo de dato: numero entero
numeros = 0.13 #Tipo de dato: numero decimal
valores = True #Tipo de dato: boolean

print(textNombre)
print(edad)
print(numeros)
print(valores)

#todo lo que está antes de unos parentesís se les conoce como funciones
#soyUnaVariable = input("Ingrese su nombre: ")
# "," sirve para pasar varios parámetros
#print("Saludo usuario: ", soyUnaVariable)

#a = int(input("Ingrese su numero a: "))
#b = int(input("Ingrese su numero b: "))

#resultadoSuma = a + b
#print("El resultado de la suma es:", resultadoSuma)

#c = float(input("Ingrese su numero c: "))
#d = float(input("Ingrese su numero d: "))

#resultadoSumaDecimales = c + d

#print("El resultado de la suma con decimales es:", resultadoSumaDecimales)

# numeroA = 90
# numeroB = 100

# #Condicionales realizan pruebas con base a lo que le indiquemos
# if numeroA > numeroB:
#     print("El numero", numeroA, " es el mayor")
# else:
#     print("El numero", numeroB, " es el mayor")

# numeroC = float(input("Ingrese su numero c: "))
# numeroD = float(input("Ingrese su numero d: "))

# if numeroC == numeroD:
#     print("los números son iguales")
# elif numeroC > numeroD:
#     print("El numero", numeroC, " es el mayor")
# else:
#     print("El numero", numeroD, " es el mayor")

#Ciclos
print("while")
contador = 1
#mientras cumpla con las condiciones ingrese y haga sus operaciones
while contador < 10:
    print(contador)
    contador = contador +1

print("for")
for iContador in range(4,12):
    print(iContador)
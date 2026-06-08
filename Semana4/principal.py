from calculadora import calculadora

#Crear un objeto o instancia
#objetoCalculadora = calculadora(10,9)

while True:

    numeroA = float(input("Ingrese el primer número: "))
    numeroB = float(input("Ingrese el segundo número: "))

    objetoCalculadora = calculadora(numeroA, numeroB)
    preguntaOpcion = input("Elija una opcion\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\nOpción: ")

    if preguntaOpcion == "1":
        print("El resultado es:", objetoCalculadora.sumar())

    elif preguntaOpcion == "2":
        print("El resultado es:", objetoCalculadora.restar())

    elif preguntaOpcion == "3":
        print("El resultado es:", objetoCalculadora.multiplicar())

    elif preguntaOpcion == "4":
        print("El resultado es:", objetoCalculadora.dividir())

    elif preguntaOpcion == "5":
        print("Ha salido de la calculadora")
        break

    else:
        print("Opción inválida")
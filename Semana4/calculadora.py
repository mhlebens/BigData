#dos parámetros y debe tener funciones de sumer, restar, multiplicar

class calculadora: 
    def __init__(self, numeroA, numeroB):
        self.numeroA = numeroA
        self.numeroB = numeroB

    def sumar(self):
        #Return regresa una respuesta
        return self.numeroA + self.numeroB
    def restar(self):
            #Return regresa una respuesta
            return self.numeroA - self.numeroB
    def multiplicar(self):
        #Return regresa una respuesta
        return self.numeroA * self.numeroB
    def dividir(self):
        #Return regresa una respuesta
        return self.numeroA / self.numeroB
    
    

    

